import pandas as pd
from pathlib import Path

def load_data(filepath):
    """
    Load the data from the specified Excel file, skipping initial rows and setting no header initially.

    Args:
        filepath (Path): Path to the data file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    print("Loading data...")
    return pd.read_excel(filepath, sheet_name="Tabelle1", skiprows=3, header=None)

def clean_data(df):
    """
    Clean the DataFrame by renaming columns, setting headers, and indexing by date.

    Args:
        df (pd.DataFrame): Raw DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    print("Cleaning data...")
    
    # Rename top-left cell to "date"
    df.iloc[0, 0] = "date"
    
    # Drop the second column
    df.drop(df.columns[1], axis=1, inplace=True)
    
    # Set the fourth row as the header
    df.columns = df.iloc[0]
    df = df.drop(0)
    
    # Drop the first data row with "CURRENCY"
    df.drop(df.index[0], inplace=True)
    
    # Set "date" as the index and convert to datetime
    df.set_index("date", inplace=True)
    df.index = pd.to_datetime(df.index, format="%d.%m.%Y", errors='coerce')
    
    # Drop rows where date parsing failed
    df.dropna(subset=[df.index.name], inplace=True)
    
    return df

def load_and_clean_data():
    """
    Load and clean the data from the specified Excel file based on detailed requirements.
    
    Returns:
        pd.DataFrame: Cleaned DataFrame with 'date' as index and company names as columns.
    """
    # Define the path to the data file based on the known project structure
    base_path = Path(__file__).resolve().parents[2]
    filepath = base_path / "data" / "raw" / "SPI_Data_MK.xlsx"

    # Check if the file exists
    if not filepath.exists():
        raise FileNotFoundError(f"Data file not found at {filepath}. Please ensure the file is in the correct location.")

    # Load and clean data
    df = load_data(filepath)
    df = clean_data(df)

    return df

if __name__ == "__main__":
    try:
        # Load and clean the data
        cleaned_df = load_and_clean_data()
        
        # Define path to save the cleaned data
        base_path = Path(__file__).resolve().parents[2]
        save_path = base_path / "data" / "interim" / "interim_data.csv"
        
        # Save the cleaned data to a CSV
        cleaned_df.to_csv(save_path)
        print(f"Cleaned data saved at {save_path}")
        
    except FileNotFoundError as e:
        print(e)

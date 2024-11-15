from refinitiv_data_processing import load_and_clean_data
from bloomberg_data_processing import load_and_clean_bloomberg_data
from snb_data_processing import load_and_clean_snb_data
from pathlib import Path

if __name__ == "__main__":
    try:
        # Define the base path for file locations
        base_path = Path(__file__).resolve().parents[2]

        # Refinitiv Data Processing
        print("Processing Refinitiv data...")
        refinitiv_file_path = base_path / "data" / "raw" / "SPI_Data_Datastream_raw.xlsx"
        cleaned_refinitiv_df = load_and_clean_data(refinitiv_file_path)

        # Save Refinitiv data
        save_path_refinitiv = base_path / "data" / "interim" / "refinitiv_data.csv"
        cleaned_refinitiv_df.to_csv(save_path_refinitiv)
        print(f"Refinitiv data saved at {save_path_refinitiv}")

        # Bloomberg Data Processing
        print("\nProcessing Bloomberg data...")
        bloomberg_file_path = base_path / "data" / "raw" / "SPI_Index_Data.xlsx"
        cleaned_bloomberg_df = load_and_clean_bloomberg_data(bloomberg_file_path)

        # Save Bloomberg data
        save_path_bloomberg = base_path / "data" / "interim" / "bloomberg_data.csv"
        cleaned_bloomberg_df.to_csv(save_path_bloomberg)
        print(f"Bloomberg data saved at {save_path_bloomberg}")

        # SNB Yield Data Processing
        print("\nProcessing SNB yield data...")
        snb_file_path = base_path / "data" / "raw" / "snb_yield_data.csv"
        cleaned_snb_df = load_and_clean_snb_data(snb_file_path)

        # Save SNB data
        save_path_snb = base_path / "data" / "interim" / "snb_yield_data.csv"
        cleaned_snb_df.to_csv(save_path_snb, index=False)
        print(f"SNB yield data saved at {save_path_snb}")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

import pandas as pd
import argparse


parser = argparse.ArgumentParser(description="Convert Parquet to CSV")
parser.add_argument("input_file", help="Path to the input Parquet file")
parser.add_argument("output_file", help="Path to save the output CSV file")

# Parse arguments
args = parser.parse_args()

# Load Parquet file
df = pd.read_parquet(args.input_file)
# Save to CSV
df.to_csv(args.output_file, index=False)

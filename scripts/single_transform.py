import pandas as pd
import boto3

# Connect to S3 client
s3_client = boto3.client('s3')

# Specify bucket name and input file key
bucket_name = 'test-converted-pm'
excel_key = 'park/bkk_park_index.xlsx'

# Download Excel file from S3 bucket
response = s3_client.get_object(Bucket=bucket_name, Key=excel_key)
excel_data = response['Body'].read()

# Convert Excel data to DataFrame
df = pd.read_excel(excel_data)

# Convert DataFrame to CSV
csv_data = df.to_csv(index=False)
output_key = 'park/converted_bkk_park_index.csv'

# Upload CSV file to S3 bucket
s3_client.put_object(Body=csv_data, Bucket=bucket_name, Key=output_key)




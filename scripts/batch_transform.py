import pandas as pd
import boto3

s3_client = boto3.client('s3')

# List of input S3 object keys
input_keys = ['PM2.5/PM2.5(2011).xlsx', 'PM2.5/PM2.5(2012).xlsx', 'PM2.5/PM2.5(2013).xlsx', 'PM2.5/PM2.5(2014).xlsx', 'PM2.5/PM2.5(2015).xlsx', 'PM2.5/PM2.5(2016).xlsx', 'PM2.5/PM2.5(2017).xlsx', 'PM2.5/PM2.5(2018).xlsx', 'PM2.5/PM2.5(2019).xlsx', 'PM2.5/PM2.5(2020).xlsx', 'PM2.5/PM2.5(2021).xlsx', 'PM2.5/PM2.5(2022).xlsx']

# Specify bucket name and output file prefix
bucket_name = 'pm25-yearly'
output_prefix = 'output/converted_'

# Iterate over input keys
for input_key in input_keys:
    # Download Excel file from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=input_key)
    excel_data = response['Body'].read()

    # Read Excel file
    df = pd.read_excel(excel_data)

    # Convert DataFrame to CSV
    csv_data = df.to_csv(index=False)

    # Generate output file key
    output_key = output_prefix + input_key.split('/')[-1].replace('.xlsx', '.csv')

    # Upload CSV file to S3 bucket
    s3_client.put_object(Body=csv_data.encode(), Bucket=bucket_name, Key=output_key)
import pandas as pd
from sqlalchemy import create_engine

# Replace with your actual PostgreSQL password
DB_USER = "postgressor_inputyaownuser"
DB_PASS = "input_ya_own_pword"
DB_NAME = "ny_taxi"
DB_HOST = "localhost"
DB_PORT = "5432"

# Load sample data
url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
df = pd.read_csv(url, compression='gzip', nrows=1000)

# Select and rename columns to match your SQL table
df = df[[
    'VendorID',
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',
    'passenger_count',
    'trip_distance',
    'RatecodeID',
    'store_and_fwd_flag',
    'payment_type',
    'fare_amount'
]]

df = df.rename(columns={
    'VendorID': 'vendor_id',
    'tpep_pickup_datetime': 'pickup_datetime',
    'tpep_dropoff_datetime': 'dropoff_datetime',
    'RatecodeID': 'rate_code_id'
})

# Create connection to PostgreSQL
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Load into table
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append', index=False)

print("✅ Data loaded successfully!")

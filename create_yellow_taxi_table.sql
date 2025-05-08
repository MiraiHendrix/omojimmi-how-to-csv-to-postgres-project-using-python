-- Create the correct yellow_taxi_data table
CREATE TABLE IF NOT EXISTS yellow_taxi_data (
    vendor_id VARCHAR,
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    passenger_count INTEGER,
    trip_distance FLOAT,
    rate_code_id INTEGER,
    store_and_fwd_flag VARCHAR,
    payment_type VARCHAR,
    fare_amount FLOAT
);

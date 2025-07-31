import pandas as pd
import numpy as np

def clean_flights_data():
    """Clean and prepare flights data"""
    # Read the flights data
    flights = pd.read_csv(r'C:\Users\sejal\Downloads\flights.csv')
    
    # Clean column names
    flights.columns = flights.columns.str.strip()
    
    # Convert time columns to proper format
    time_columns = ['SCHEDULED_DEPARTURE', 'DEPARTURE_TIME', 'SCHEDULED_ARRIVAL', 'ARRIVAL_TIME']
    for col in time_columns:
        # Convert to string and handle missing values
        flights[col] = flights[col].astype(str).str.zfill(4)
        # Handle cases where time is not available
        flights[col] = np.where(flights[col] == '0000', np.nan, flights[col])
    
    # Convert delay columns to numeric
    delay_columns = ['DEPARTURE_DELAY', 'ARRIVAL_DELAY', 'AIR_SYSTEM_DELAY',
                     'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY']
    for col in delay_columns:
        flights[col] = pd.to_numeric(flights[col], errors='coerce')
    
    # Handle cancelled flights
    flights['CANCELLED'] = pd.to_numeric(flights['CANCELLED'], errors='coerce').fillna(0)
    
    # Save cleaned data
    flights.to_csv('cleaned_flights.csv', index=False)
    print("Cleaned flights data saved to cleaned_flights.csv")

if __name__ == "__main__":
    clean_flights_data()

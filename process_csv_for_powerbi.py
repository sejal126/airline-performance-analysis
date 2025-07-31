import pandas as pd
import os

def process_csv_files():
    """Process CSV files for Power BI"""
    # Create output directory
    output_dir = 'powerbi_data'
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Read airlines CSV
        airlines = pd.read_csv(r'C:\Users\sejal\Downloads\airlines.csv')
        airlines.to_csv(os.path.join(output_dir, 'Airlines.csv'), index=False)
        print("Processed Airlines.csv")
        
        # Read airports CSV
        airports = pd.read_csv(r'C:\Users\sejal\Downloads\airports.csv')
        airports.to_csv(os.path.join(output_dir, 'Airports.csv'), index=False)
        print("Processed Airports.csv")
        
        # Read flights CSV
        flights = pd.read_csv(r'C:\Users\sejal\Downloads\flights.csv')
        
        # Create Date table
        dates = pd.DataFrame({
            'Date': pd.date_range(start='2015-01-01', end='2015-12-31'),
            'Year': pd.date_range(start='2015-01-01', end='2015-12-31').year,
            'Month': pd.date_range(start='2015-01-01', end='2015-12-31').month,
            'Day': pd.date_range(start='2015-01-01', end='2015-12-31').day,
            'DayOfWeek': pd.date_range(start='2015-01-01', end='2015-12-31').dayofweek + 1,
            'MonthName': pd.date_range(start='2015-01-01', end='2015-12-31').strftime('%B'),
            'Quarter': pd.date_range(start='2015-01-01', end='2015-12-31').quarter,
            'QuarterName': pd.date_range(start='2015-01-01', end='2015-12-31').strftime('Q%q'),
            'YearMonth': pd.date_range(start='2015-01-01', end='2015-12-31').strftime('%Y-%m'),
            'YearQuarter': pd.date_range(start='2015-01-01', end='2015-12-31').strftime('%Y-Q%q')
        })
        dates.to_csv(os.path.join(output_dir, 'Date.csv'), index=False)
        print("Created Date.csv")
        
        # Create KPI tables
        # 1. OnTimePerformance
        on_time = flights.groupby(['AIRLINE', 'MONTH']).agg({
            'ARRIVAL_DELAY': lambda x: (x <= 15).sum(),
            'FLIGHT_NUMBER': 'count'
        }).reset_index()
        on_time['OnTimeRate'] = (on_time['ARRIVAL_DELAY'] / on_time['FLIGHT_NUMBER'] * 100).round(2)
        on_time.to_csv(os.path.join(output_dir, 'OnTimePerformance.csv'), index=False)
        print("Created OnTimePerformance.csv")
        
        # 2. AverageDelays
        avg_delays = flights.groupby(['AIRLINE', 'MONTH']).agg({
            'ARRIVAL_DELAY': 'mean',
            'DEPARTURE_DELAY': 'mean',
            'AIR_SYSTEM_DELAY': 'mean',
            'SECURITY_DELAY': 'mean',
            'AIRLINE_DELAY': 'mean',
            'LATE_AIRCRAFT_DELAY': 'mean',
            'WEATHER_DELAY': 'mean'
        }).reset_index()
        avg_delays.to_csv(os.path.join(output_dir, 'AverageDelays.csv'), index=False)
        print("Created AverageDelays.csv")
        
        # 3. CancellationAnalysis
        cancellations = flights.groupby(['AIRLINE', 'MONTH']).agg({
            'CANCELLED': 'sum',
            'FLIGHT_NUMBER': 'count'
        }).reset_index()
        cancellations['CancellationRate'] = (cancellations['CANCELLED'] / cancellations['FLIGHT_NUMBER'] * 100).round(2)
        cancellations.to_csv(os.path.join(output_dir, 'CancellationAnalysis.csv'), index=False)
        print("Created CancellationAnalysis.csv")
        
        # 4. AirportPerformance
        airport_perf = flights.groupby(['ORIGIN_AIRPORT', 'MONTH']).agg({
            'ARRIVAL_DELAY': lambda x: (x > 0).sum(),
            'FLIGHT_NUMBER': 'count'
        }).reset_index()
        airport_perf['DelayRate'] = (airport_perf['ARRIVAL_DELAY'] / airport_perf['FLIGHT_NUMBER'] * 100).round(2)
        airport_perf.to_csv(os.path.join(output_dir, 'AirportPerformance.csv'), index=False)
        print("Created AirportPerformance.csv")
        
        # 5. TimeOfDayAnalysis
        flights['TimeOfDay'] = pd.cut(
            flights['SCHEDULED_DEPARTURE'] % 2400,
            bins=[0, 600, 1200, 1800, 2400],
            labels=['Night', 'Morning', 'Afternoon', 'Evening'],
            right=False
        )
        
        time_analysis = flights.groupby(['MONTH', 'TimeOfDay']).agg({
            'ARRIVAL_DELAY': lambda x: (x > 0).sum(),
            'FLIGHT_NUMBER': 'count'
        }).reset_index()
        time_analysis['DelayRate'] = (time_analysis['ARRIVAL_DELAY'] / time_analysis['FLIGHT_NUMBER'] * 100).round(2)
        time_analysis.to_csv(os.path.join(output_dir, 'TimeOfDayAnalysis.csv'), index=False)
        print("Created TimeOfDayAnalysis.csv")
        
        print("\nAll files have been processed and saved to powerbi_data directory")
        
    except Exception as e:
        print(f"Error processing CSV files: {str(e)}")

if __name__ == "__main__":
    process_csv_files()

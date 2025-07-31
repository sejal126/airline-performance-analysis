import pandas as pd
import os

def create_kpi_files():
    """Create KPI files from cleaned flights data"""
    # Create output directory if it doesn't exist
    output_dir = 'powerbi_data'
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Read cleaned flights data
        flights = pd.read_csv(r'C:\Users\sejal\Downloads\cleaned_flights.csv')
        
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
        # Create time of day categories
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
        
        print("\nAll KPI files have been created in powerbi_data directory")
        
    except Exception as e:
        print(f"Error creating KPI files: {str(e)}")

if __name__ == "__main__":
    create_kpi_files()

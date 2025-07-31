import pandas as pd
import sqlite3
from datetime import datetime, timedelta

def create_date_table():
    """Create a date dimension table"""
    # Create SQLite connection
    conn = sqlite3.connect('airline_performance.db')
    
    try:
        # Create date table
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Date (
                DateKey INTEGER PRIMARY KEY,
                FullDate DATE,
                Year INTEGER,
                Month INTEGER,
                Day INTEGER,
                DayOfWeek INTEGER,
                MonthName TEXT,
                Quarter INTEGER,
                QuarterName TEXT,
                YearMonth TEXT,
                YearQuarter TEXT
            )
        """)
        
        # Generate dates for the year 2015
        start_date = datetime(2015, 1, 1)
        end_date = datetime(2015, 12, 31)
        current_date = start_date
        
        dates = []
        while current_date <= end_date:
            dates.append({
                'DateKey': current_date.toordinal(),
                'FullDate': current_date,
                'Year': current_date.year,
                'Month': current_date.month,
                'Day': current_date.day,
                'DayOfWeek': current_date.weekday() + 1,  # 1=Monday, 7=Sunday
                'MonthName': current_date.strftime('%B'),
                'Quarter': (current_date.month - 1) // 3 + 1,
                'QuarterName': f'Q{((current_date.month - 1) // 3 + 1)}',
                'YearMonth': f'{current_date.year}-{current_date.month:02d}',
                'YearQuarter': f'{current_date.year}-Q{((current_date.month - 1) // 3 + 1)}'
            })
            current_date += timedelta(days=1)
        
        # Insert dates into table
        df = pd.DataFrame(dates)
        df.to_sql('Date', conn, if_exists='replace', index=False)
        
        print("Date table created successfully!")
        
    except Exception as e:
        print(f"Error creating date table: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_date_table()

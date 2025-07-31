import pandas as pd
import sqlite3
import os

def export_tables():
    """Export all tables and views to CSV files"""
    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'powerbi_data')
    os.makedirs(output_dir, exist_ok=True)
    
    # Connect to SQLite database
    conn = sqlite3.connect('airline_performance.db')
    
    try:
        # Get list of tables
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        tables = cursor.fetchall()
        
        # Get list of views
        cursor.execute("SELECT name FROM sqlite_master WHERE type='view'")
        views = cursor.fetchall()
        
        # Export tables
        for table in tables:
            table_name = table[0]
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
            output_file = os.path.join(output_dir, f'{table_name}.csv')
            df.to_csv(output_file, index=False)
            print(f"Exported table {table_name} to CSV: {output_file}")
        
        # Export views
        for view in views:
            view_name = view[0]
            df = pd.read_sql_query(f"SELECT * FROM {view_name}", conn)
            output_file = os.path.join(output_dir, f'{view_name}.csv')
            df.to_csv(output_file, index=False)
            print(f"Exported view {view_name} to CSV: {output_file}")
        
        print("\nAll tables and views have been exported to CSV files")
        print(f"Files are located in: {output_dir}")
        
    except Exception as e:
        print(f"Error exporting data: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    export_tables()

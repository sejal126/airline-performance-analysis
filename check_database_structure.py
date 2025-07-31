import sqlite3
import os

def check_structure():
    """Check the structure of the SQLite database"""
    # Check if database exists
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airline_performance.db')
    if not os.path.exists(db_path):
        print(f"Database file not found at: {db_path}")
        return
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        print("\nChecking database structure...")
        
        # Get list of tables
        print("\nTables in the database:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        tables = cursor.fetchall()
        for table in tables:
            print(table[0])
            
            # Get columns for each table
            cursor.execute(f"PRAGMA table_info({table[0]})")
            columns = cursor.fetchall()
            print("  Columns:")
            for column in columns:
                print(f"    {column[1]} ({column[2]})")
        
        # Get list of views
        print("\nViews in the database:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='view'")
        views = cursor.fetchall()
        for view in views:
            print(view[0])
            
            # Get view definition
            cursor.execute(f"SELECT sql FROM sqlite_master WHERE name='{view[0]}'")
            view_sql = cursor.fetchone()
            if view_sql:
                print("  SQL Definition:")
                print(f"    {view_sql[0]}")
        
    except Exception as e:
        print(f"Error checking database structure: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    check_structure()

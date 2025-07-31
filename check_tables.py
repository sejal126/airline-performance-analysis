import sqlite3

def check_tables():
    """Check what tables exist in the database"""
    conn = sqlite3.connect('airline_performance.db')
    cursor = conn.cursor()
    
    try:
        # Get list of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table[0])
            
        # Get list of views
        cursor.execute("SELECT name FROM sqlite_master WHERE type='view';")
        views = cursor.fetchall()
        print("\nViews in the database:")
        for view in views:
            print(view[0])
            
    except Exception as e:
        print(f"Error checking tables: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    check_tables()

# U.S. Airline Performance & Delay Analysis

This project analyzes U.S. domestic flight data to uncover patterns in delays and cancellations, evaluate airline and airport performance, and provide data-driven insights.

## Project Structure

```
airline-performance-analysis/
├── data/           # Raw data files
├── sql/            # SQL schema and queries
│   └── schema.sql  # Database schema definition
├── data_loader.py  # Python script for data loading
└── requirements.txt # Python dependencies
```

## Setup Instructions

1. Install MySQL Server and create a database named `airline_performance`
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the dataset from Google Drive and place the CSV files in the `data/` directory:
   - airlines.csv
   - airports.csv
   - flights.csv
4. Update the database connection parameters in `data_loader.py`
5. Run the data loader script:
   ```bash
   python data_loader.py
   ```

## Key Features

- Comprehensive database schema for flight data
- Data cleaning and transformation scripts
- Support for SQL queries and analysis
- Ready for Power BI/Tableau integration

## Next Steps

1. Run SQL queries for exploratory data analysis
2. Create dashboards using Power BI or Tableau
3. Generate insights and recommendations
4. Prepare final report and presentation

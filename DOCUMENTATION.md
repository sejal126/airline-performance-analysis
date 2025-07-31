# U.S. Airline Performance Dashboard - Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dashboard Guide](#dashboard-guide)
3. [Data Dictionary](#data-dictionary)
4. [Technical Documentation](#technical-documentation)
5. [Implementation Guide](#implementation-guide)
6. [Troubleshooting](#troubleshooting)

## Project Overview
This dashboard provides comprehensive analysis of U.S. domestic flight performance, including delay patterns, airline performance metrics, and airport operations analysis.

## Dashboard Guide

### Navigation
- **Overview Page**: Key performance indicators and high-level trends
- **Airline Analysis**: Detailed carrier performance metrics
- **Airport Analysis**: Geographic performance visualization
- **Time Analysis**: Temporal patterns and trends

### How to Use
1. **Filtering Data**
   - Use the date range selector in the top-right corner
   - Select specific airlines from the airline filter
   - Filter by origin/destination airport as needed

2. **Interacting with Visuals**
   - Hover over data points for detailed tooltips
   - Click on elements to cross-filter other visuals
   - Use the drill-down feature in hierarchical charts

## Data Dictionary

### Tables
#### Flights
| Column | Type | Description |
|--------|------|-------------|
| FLIGHT_NUMBER | Text | Unique flight identifier |
| AIRLINE | Text | Airline code |
| ORIGIN_AIRPORT | Text | Departure airport code |
| DESTINATION_AIRPORT | Text | Arrival airport code |
| SCHEDULED_DEPARTURE | Time | Scheduled departure time |
| DEPARTURE_DELAY | Number | Delay in minutes |
| ARRIVAL_DELAY | Number | Arrival delay in minutes |
| CANCELLED | Boolean | Flight cancellation status |

#### Airlines
| Column | Type | Description |
|--------|------|-------------|
| IATA_CODE | Text | Airline code |
| AIRLINE | Text | Airline full name |

#### Airports
| Column | Type | Description |
|--------|------|-------------|
| IATA_CODE | Text | Airport code |
| AIRPORT | Text | Airport name |
| CITY | Text | City name |
| STATE | Text | State code |
| COUNTRY | Text | Country name |

### Key Performance Indicators (KPIs)
1. **On-Time Performance**
   - Definition: Percentage of flights arriving within 15 minutes of schedule
   - Calculation: (On-time flights / Total flights) * 100

2. **Average Delay**
   - Definition: Mean delay time across all flights
   - Calculation: SUM(DELAY_MINUTES) / COUNT(FLIGHTS)

3. **Cancellation Rate**
   - Definition: Percentage of cancelled flights
   - Calculation: (Cancelled flights / Total flights) * 100

## Technical Documentation

### Data Sources
- **Flight Data**: `sql/data/flights.csv` - Contains flight records with delay and cancellation information
- **Airline Reference**: `sql/data/airlines.csv` - Maps airline codes to full names
- **Airport Reference**: `sql/data/airports.csv` - Contains airport details including codes and locations

### Data Model
```
+-------------+       +-------------+       +-------------+
|  Airlines   |       |   Flights   |       |  Airports   |
+-------------+       +-------------+       +-------------+
| IATA_CODE   |<----->| AIRLINE     |       | IATA_CODE   |
| AIRLINE     |       | ORIGIN_CODE |<----->| (as Origin) |
+-------------+       | DEST_CODE   |       +-------------+
                     +-------------+               ^
                                                 |
                                                 |
                                   +-------------+-------------+
                                   |  Time Dimension (Date Table) |
                                   +-----------------------------+
```

### Performance Optimization
- Data is loaded in DirectQuery mode for large datasets
- Relationships are properly defined in the data model
- Visuals are optimized with appropriate granularity
- Date hierarchy is used for time-based analysis

## Implementation Guide

### Prerequisites
- Power BI Desktop (Latest version)
- Access to the following files in the `sql/data/` directory:
  - `flights.csv`
  - `airlines.csv`
  - `airports.csv`

### Setup Instructions
1. **Initial Setup**
   - Ensure all required CSV files are in the `sql/data/` directory
   - The expected directory structure is:
     ```
     airline-performance-analysis/
     ├── powerbi/
     │   ├── dashboard.pbix
     │   └── dashboard_config.json
     └── sql/
         └── data/
             ├── flights.csv
             ├── airlines.csv
             └── airports.csv
     ```

2. **Data Refresh**
   - Open the Power BI Desktop file
   - Click "Home" > "Transform data" > "Data source settings"
   - For each source, click "Edit Permissions" and ensure the file path is correct
   - Click "Apply changes" and then "Close"
   - Click "Refresh" to update the data

3. **Customization**
   - To modify visuals, select the visual and adjust fields
   - Add new measures using DAX in the Modeling tab
   - Update filters from the Visualizations pane

## Troubleshooting

### Common Issues
1. **Data Not Loading**
   - Verify file paths in Power Query Editor
   - Check for file permissions
   - Ensure CSV files are not open in other programs

2. **Visuals Not Updating**
   - Click "Refresh" in the Home tab
   - Verify all filters are set correctly
   - Check relationships in the Model view
   - Ensure all required fields are included in the visual

3. **Performance Issues**
   - For large datasets, use DirectQuery mode
   - Disable auto date/time in Power BI options
   - Reduce the number of visuals on a single page
   - Consider using aggregations for large datasets

### Support
For additional support, please contact [Your Contact Information] or open an issue in the project repository.

---
*Last Updated: August 1, 2025*

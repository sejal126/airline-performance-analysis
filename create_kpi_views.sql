-- On-Time Performance KPI
CREATE VIEW IF NOT EXISTS OnTimePerformance AS
SELECT 
    DATE_TRUNC('month', DATE) as Month,
    AIRLINE,
    COUNT(*) as TotalFlights,
    SUM(CASE WHEN ARRIVAL_DELAY <= 15 THEN 1 ELSE 0 END) as OnTimeFlights,
    ROUND(CAST(SUM(CASE WHEN ARRIVAL_DELAY <= 15 THEN 1 ELSE 0 END) as REAL) * 100.0 / COUNT(*), 2) as OnTimeRate
FROM Flights
GROUP BY DATE_TRUNC('month', DATE), AIRLINE
ORDER BY Month, OnTimeRate DESC;

-- Average Delays KPI
CREATE VIEW IF NOT EXISTS AverageDelays AS
SELECT 
    DATE_TRUNC('month', DATE) as Month,
    AIRLINE,
    AVG(ARRIVAL_DELAY) as AvgArrivalDelay,
    AVG(DEPARTURE_DELAY) as AvgDepartureDelay,
    AVG(AIR_SYSTEM_DELAY) as AvgAirSystemDelay,
    AVG(SECURITY_DELAY) as AvgSecurityDelay,
    AVG(AIRLINE_DELAY) as AvgAirlineDelay,
    AVG(LATE_AIRCRAFT_DELAY) as AvgLateAircraftDelay,
    AVG(WEATHER_DELAY) as AvgWeatherDelay
FROM Flights
WHERE ARRIVAL_DELAY > 0 OR DEPARTURE_DELAY > 0
GROUP BY DATE_TRUNC('month', DATE), AIRLINE
ORDER BY Month, AVG(ARRIVAL_DELAY) DESC;

-- Cancellation Analysis KPI
CREATE VIEW IF NOT EXISTS CancellationAnalysis AS
SELECT 
    DATE_TRUNC('month', DATE) as Month,
    AIRLINE,
    COUNT(*) as TotalFlights,
    SUM(CANCELLED) as TotalCancellations,
    ROUND(CAST(SUM(CANCELLED) as REAL) * 100.0 / COUNT(*), 2) as CancellationRate,
    SUM(CASE WHEN CANCELLATION_REASON = 'A' THEN 1 ELSE 0 END) as CarrierCancellations,
    SUM(CASE WHEN CANCELLATION_REASON = 'B' THEN 1 ELSE 0 END) as WeatherCancellations,
    SUM(CASE WHEN CANCELLATION_REASON = 'C' THEN 1 ELSE 0 END) as NASCancellations,
    SUM(CASE WHEN CANCELLATION_REASON = 'D' THEN 1 ELSE 0 END) as SecurityCancellations
FROM Flights
GROUP BY DATE_TRUNC('month', DATE), AIRLINE
ORDER BY Month, CancellationRate DESC;

-- Airport Performance KPI
CREATE VIEW IF NOT EXISTS AirportPerformance AS
SELECT 
    DATE_TRUNC('month', DATE) as Month,
    ORIGIN_AIRPORT,
    COUNT(*) as TotalFlights,
    SUM(CASE WHEN ARRIVAL_DELAY > 0 THEN 1 ELSE 0 END) as DelayedFlights,
    ROUND(CAST(SUM(CASE WHEN ARRIVAL_DELAY > 0 THEN 1 ELSE 0 END) as REAL) * 100.0 / COUNT(*), 2) as DelayRate,
    AVG(ARRIVAL_DELAY) as AvgDelayTime
FROM Flights
GROUP BY DATE_TRUNC('month', DATE), ORIGIN_AIRPORT
ORDER BY Month, DelayRate DESC;

-- Time of Day Analysis KPI
CREATE VIEW IF NOT EXISTS TimeOfDayAnalysis AS
SELECT 
    DATE_TRUNC('month', DATE) as Month,
    CASE 
        WHEN TIME(SCHEDULED_DEPARTURE) BETWEEN '00:00:00' AND '05:59:59' THEN 'Night'
        WHEN TIME(SCHEDULED_DEPARTURE) BETWEEN '06:00:00' AND '11:59:59' THEN 'Morning'
        WHEN TIME(SCHEDULED_DEPARTURE) BETWEEN '12:00:00' AND '17:59:59' THEN 'Afternoon'
        ELSE 'Evening'
    END as TimeOfDay,
    COUNT(*) as TotalFlights,
    SUM(CASE WHEN ARRIVAL_DELAY > 0 THEN 1 ELSE 0 END) as DelayedFlights,
    ROUND(CAST(SUM(CASE WHEN ARRIVAL_DELAY > 0 THEN 1 ELSE 0 END) as REAL) * 100.0 / COUNT(*), 2) as DelayRate,
    AVG(ARRIVAL_DELAY) as AvgDelayTime
FROM Flights
GROUP BY DATE_TRUNC('month', DATE), TimeOfDay
ORDER BY Month, TimeOfDay;

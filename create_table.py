import sqlite3

conn = sqlite3.connect('trips.db')
c = conn.cursor()

# Drop existing table if it exists
c.execute("DROP TABLE IF EXISTS trips")

# Create table with correct columns
c.execute('''
CREATE TABLE trips (
    trip_id TEXT,
    trip_date TEXT,
    vehicle_id TEXT,
    driver_id TEXT,
    planned_distance INTEGER,
    advance_given REAL,
    origin TEXT,
    destination TEXT,
    vehicle_type TEXT,
    flags TEXT,
    total_freight REAL
)
''')

conn.commit()
conn.close()

print("Table 'trips' created successfully with correct columns.")

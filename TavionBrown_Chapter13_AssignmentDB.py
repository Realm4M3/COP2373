import sqlite3
import matplotlib.pyplot as plt

# Step 1: Creating the Database and Table
def create_database():
    conn = sqlite3.connect('population_TB.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Step 2: Inserting Initial Data for 2023
def insert_initial_data():
    cities = [
        ('Miami', 2023, 470000),
        ('Orlando', 2023, 310000),
        ('Tampa', 2023, 400000),
        ('Jacksonville', 2023, 960000),
        ('Tallahassee', 2023, 195000),
        ('Fort Lauderdale', 2023, 180000),
        ('Gainesville', 2023, 141000),
        ('Sarasota', 2023, 58000),
        ('St. Petersburg', 2023, 270000),
        ('Pensacola', 2023, 55000)
    ]
    conn = sqlite3.connect('population_TB.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', cities)
    conn.commit()
    conn.close()

# Step 3: Simulating Population Growth
def simulate_population_growth():
    conn = sqlite3.connect('population_TB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT city FROM population')
    cities = cursor.fetchall()
    for city in cities:
        city_name = city[0]
        for year in range(2024, 2044):
            cursor.execute('SELECT population FROM population WHERE city=? AND year=?', (city_name, year-1))
            last_population = cursor.fetchone()[0]
            new_population = int(last_population * 1.02)
            cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city_name, year, new_population))
    conn.commit()
    conn.close()

# Step 4: Visualizing Population Growth
def visualize_population_growth():
    conn = sqlite3.connect('population_TB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT city FROM population')
    cities = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    print("Available cities:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")
    
    city_choice = int(input("Choose a city by number: "))
    chosen_city = cities[city_choice - 1]
    
    conn = sqlite3.connect('population_TB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT year, population FROM population WHERE city=? ORDER BY year', (chosen_city,))
    data = cursor.fetchall()
    conn.close()
    
    years = [row[0] for row in data]
    populations = [row[1] for row in data]
    
    plt.plot(years, populations, marker='o')
    plt.title(f'Population Growth in {chosen_city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()

# Main function to run the program
def main():
    create_database()
    insert_initial_data()
    simulate_population_growth()
    visualize_population_growth()

if __name__ == "__main__":
    main()

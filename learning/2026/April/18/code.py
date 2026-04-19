"""
Code Explanation:
Generating the environment, used NumPy to quickly handle the random distributions and math arrays. 
Systematically build the target variable `energy_consumption` by adding different mathematical effects together, finishing it off with random noise.
"""
import numpy as np

def generate_smart_building_data(num_days: int = 1000):
    """Generates a synthetic, non-linear dataset for energy consumption."""
    np.random.seed(42) 

    # Base Features
    day_of_year = np.arange(1, num_days + 1) % 365
    day_of_year[day_of_year == 0] = 365
    is_weekend = (np.arange(num_days) % 7 >= 5).astype(int)
    
    # Temperature follows a seasonal sine wave + daily noise
    avg_temperature = 15 + 10 * np.sin(2 * np.pi * day_of_year / 365) + np.random.normal(0, 3, num_days)
    
    working_hours = np.where(is_weekend == 1, np.random.uniform(0, 4, num_days), np.random.uniform(8, 12, num_days))
    num_occupants = np.where(is_weekend == 1, np.random.randint(0, 50, num_days), np.random.randint(200, 500, num_days))
    
    # Devices strongly correlate with occupants
    num_devices_on = (num_occupants * np.random.uniform(1.5, 2.5, num_days)).astype(int)
    
    # 2. Constructing the Target Variable (Energy Consumption)
    base_load = 500.0
    
    # Non-linear temperature effect (parabola centered at 22C)
    temp_effect = 2.5 * (avg_temperature - 22)**2 
    
    # Interaction effect
    occupancy_effect = 0.5 * (num_occupants * working_hours)
    
    # Seasonal background load
    seasonal_effect = 100 * np.sin(2 * np.pi * day_of_year / 365)
    
    # Target generation
    energy_consumption = base_load + temp_effect + occupancy_effect + seasonal_effect
    
    # Lag Dependency (Yesterday's consumption affects today's baseline)
    # Applying the lag iteratively
    for i in range(1, num_days):
        energy_consumption[i] += 0.2 * energy_consumption[i-1]
        
    # The Irreducible Error (Noise)
    noise = np.random.normal(0, 150, num_days)
    energy_consumption += noise
    
    dataset = np.column_stack((
        avg_temperature,
        num_occupants,
        working_hours,
        is_weekend,
        num_devices_on,
        day_of_year,
        energy_consumption
    ))
    
    return dataset

# Let's generate it and look at a single row!
data = generate_smart_building_data(1000)
print("Temp,Occupants,Hours,Weekend,Devices,DayOfYear,EnergyConsumption")
try:
    for row in data:
        print(",".join(str(np.round(x, 2)) for x in row))
except Exception as e:
    print(f"An error occurred: {e}")
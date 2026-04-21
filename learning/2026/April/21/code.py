"""
Code Explanation:
calculate_r2 function implements the Coefficient of Determination. 
Notice how calculating TSS simply subtracts the mean from every single true value, acting as the baseline worst-case scenario.
"""

import numpy as np
import math

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
def engineer_features(raw_data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Takes the raw dataset and generates a new feature matrix X and target y.
    Raw Columns: [Temp, Occupants, Hours, Weekend, Devices, DayOfYear, Energy]
    Indices:      0     1          2      3        4        5          6
    """
    X_engineered = []
    y = []
    i = 0
    for row in raw_data:
        temp = row[0]
        occupants = row[1]
        hours = row[2]
        weekend = row[3]
        devices = row[4]
        day_of_year = row[5]
        target_energy = row[6]

        # Base features (pass them through)
        new_row = [temp, occupants, hours, weekend]
        
        # Polynomial Feature: Temp Squared
        new_row.append(temp ** 2)
        
        # Interaction Term: Occupants * Hours
        new_row.append(occupants * hours)
        
        # 4. Cyclical Encoding: Sin and Cos of DayOfYear
        # YOUR CODE HERE: Calculate and append sin_day and cos_day
        sin_day = math.sin(2 * math.pi * day_of_year / 365)
        cos_day = math.cos(2 * math.pi * day_of_year / 365)
        new_row.append(sin_day)
        new_row.append(cos_day)
        
        X_engineered.append(new_row)
        y.append(target_energy)
        
    return np.array(X_engineered), np.array(y)
def calculate_r2(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculates the R-squared metric.
    """
    y_true_mean = np.mean(y_true)
    tss = np.sum((y_true - y_true_mean) ** 2)
    rss = np.sum((y_true - y_pred) ** 2)
    r2 = 1 - (rss / tss) if tss != 0 else 0
    return r2

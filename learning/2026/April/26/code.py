"""
Code Explanation:
This script defines the mathematical sigmoid function required to map raw linear outputs into bounded probabilities. It includes an explicit memory safety check (np.clip) to prevent numpy float overflows during extreme exponential calculations.
"""
import numpy as np

def sigmoid(z: np.ndarray) -> np.ndarray:
    z_extreme = np.clip(z, -250, 250)
    return np.round(1 / (1 + np.exp(-z_extreme)), 2)

# Test 1: The Bounds
z_normal = np.array([-10, 0, 10])
print("Normal Bounds:", sigmoid(z_normal))

# Test 2: Break Things (The Overflow)
z_extreme = np.array([-1000, 1000])
print("Extreme Bounds:", sigmoid(z_extreme))
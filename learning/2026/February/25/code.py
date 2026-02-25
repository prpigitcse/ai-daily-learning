"""
Code Explanation:
- `def predict(self, other: "Vector", intercept: float) -> float`: We add a method that takes a weight vector (`other`) and a bias (`intercept`). 
- `return self.dot(other) + intercept`: This is the exact code translation of $\hat{y} = (\vec{w} \cdot \vec{x}) + b$. We execute the dot product logic we built in Day 3 and simply add the intercept to shift the result.
- *Architectural Note:* Currently, our `Vector` class is acting as both the data structure and the model itself. In software engineering for ML, the data (`Vector`) is usually passed into a separate `Model` object. We will build that exact architectural separation in our Day 7 Capstone!
"""
import math

class Vector:
    def __init__(self, attributes: list[float]):
        self.attributes = attributes
    
    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            if len(self.attributes) != len(other.attributes):
                raise ValueError("Vectors must have the same dimension for subtraction.")
            return Vector([s - o for s, o in zip(self.attributes, other.attributes)])
        else:
            raise TypeError(f"Unsupported operand type for -: 'Vector' and '{type(other).__name__}'")


    def distance(self, other: "Vector") -> float:
        # 1. Calculate the difference vector
        diff = self - other

        # 2. Square each element in the difference vector
        squared_diff = [x ** 2 for x in diff.attributes]

        # 3. Sum the squared differences
        sum_squared_diff = sum(squared_diff)

        # 4. Take the square root of the sum
        distance = math.sqrt(sum_squared_diff)

        return distance

    def dot(self, other: "Vector") -> float:
        if isinstance(other, Vector):
            if len(self.attributes) != len(other.attributes):
                raise ValueError("Vectors must have the same dimension for dot product.")
            
            return sum([a * b for a, b in zip(self.attributes, other.attributes)])
        else:
            raise TypeError(f"Unsupported operand type for dot product: 'Vector' and '{type(other).__name__}'")

    def predict(self, other: "Vector", intercept: float) -> float:
        return self.dot(other) + intercept

    def __repr__(self) -> str:
        attribute_str = ", ".join(f"{a:.2f}" for a in self.attributes)
        return f"Vector({attribute_str})"


# Example Usage: Predicting a house price using features, weights, and a bias

# Features: [3 bedrooms, 2 bathrooms, 15 years old]
house_features = Vector([3, 2, 15])

# Weights: [50000 per bed, 25000 per bath, -2000 per year of age]
model_weights = Vector([50000, 25000, -2000])

# Bias: The base value of the land in the neighborhood
land_base_value = 75000.0

# Calculate final prediction
final_prediction = house_features.predict(model_weights, land_base_value)

print(f"Dot Product (Features * Weights): ${house_features.dot(model_weights):.2f}")
print(f"Final Prediction (+ Base Value):  ${final_prediction:.2f}")
"""
Code Explanation:
- `def dot(self, other)`: We introduce the method to calculate the dot product between two vectors.
- `if len(self.attributes) != len(other.attributes)`: Just like in subtraction from [What is a Vector? Translating the Real World into Code](/2026/february/22/what-is-a-vector-translating-the-real-world-into-code), the dot product is only mathematically defined if both vectors exist in the exact same dimensional space.
- `zip(self.attributes, other.attributes)`: We pair up the corresponding elements from our feature vector and our weight vector.
- `a * b for a, b in ...`: We multiply each feature by its corresponding weight.
- `sum(...)`: We add all those individual products together to return a single scalar value, completing the $\sum_{i=1}^{n} a_i b_i$ formula.
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

    def __repr__(self) -> str:
        attribute_str = ", ".join(f"{a:.2f}" for a in self.attributes)
        return f"Vector({attribute_str})"


# Example Usage: Predicting a house price using features and weights

# Features: [3 bedrooms, 2 bathrooms, 15 years old]
house_features = Vector([3, 2, 15])

# Weights: [50000 per bed, 25000 per bath, -2000 per year of age]
model_weights = Vector([50000, 25000, -2000])

# Calculate prediction using the dot product
base_prediction = house_features.dot(model_weights)
print(f"Base Price Prediction: ${base_prediction:.2f}")
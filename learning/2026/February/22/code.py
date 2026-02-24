"""
Code Explanation:
- `class Vector`: We define a custom class to represent our mathematical vector, bypassing NumPy initially to understand the raw mechanics.
- `def __init__(self, attributes)`: Initializes the vector with an arbitrary sequence of numbers. Unlike a hardcoded 3D vector (x, y, z), this allows for $n$-dimensional feature representation.
- `if isinstance(other, Vector)`: Guards against invalid operations. We can only subtract a Vector from another Vector.
- `if len(self.attributes) != len(other.attributes)`: **Dimensionality Check**: Mathematically, vector addition and subtraction are only defined for vectors residing in the exact same dimensional space.
- `zip(self.attributes, other.attributes)`: Pairs corresponding elements $(a_i, b_i)$ from both vectors together.
- `[s - o for s, o in ...]`: **List Comprehension**: Iterates through the zipped pairs, performs the element-wise subtraction $a_i - b_i$, and builds the new resulting list in a single, optimized pass.
- `return Vector(...)`: Wraps the resulting list back into a new `Vector` object, allowing for method chaining later on.
"""

class Vector:
    def __init__(self, attributes: list[float]):
        self.attributes = attributes
    
    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            if len(self.attributes) != len(other.attributes):
                raise ValueError("Vectors must have the same dimension for subtraction.")
            return Vector([s - o for s, o in zip(self.attributes, other.attributes)])
        else:
            raise TypeError("Unsupported operand type for -: 'Vector' and '{}'".format(type(other).__name__))
        
    def __repr__(self) -> str:
        attributes_str = ", ".join("{:.2f}".format(a) for a in self.attributes)
        return "Vector({})".format(attributes_str)


# Example Usage: Simulating two houses with 4 features (bedrooms, bathrooms, age, sqft)
house_A = Vector([3, 2, 15, 2000]) 
house_B = Vector([4, 3, 10, 2500])

# Computes the difference in features: [-1.00, -1.00, 5.00, -500.00]
difference = house_A - house_B 
print(f"Feature Difference: {difference}")
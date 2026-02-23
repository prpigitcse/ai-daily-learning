"""
Code Explanation:
- `import math`: We import the standard math library to access the square root function, `math.sqrt()`.
- `def distance(self, other)`: A new method in our `Vector` class to calculate how far apart two vector instances are.
- `diff = self - other`: We leverage the `__sub__` magic method we built in [What is a Vector?](/2026/february/22/what-is-a-vector-translating-the-real-world-into-code) This elegantly handles the $(x_i - y_i)$ portion of the formula and includes the dimension validation checks automatically.
- `sum(x**2 for x in diff.attributes)`: We iterate through the newly created difference vector, squaring each element `x**2` to ensure all distances are positive, and then sum them together. This represents $\sum (x_i - y_i)^2$.
- `return math.sqrt(...)`: Finally, we take the square root of the total sum, completing the Euclidean distance formula.
"""
import math

class Vector:
    def __init__(self, attributes):
        self.attributes = attributes
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.attributes) != len(other.attributes):
                raise ValueError("Vectors must have the same dimension for subtraction.")
            return Vector([s - o for s, o in zip(self.attributes, other.attributes)])
        else:
            raise TypeError(f"Unsupported operand type for -: 'Vector' and '{type(other).__name__}'")


    def distance(self, other):
        # 1. Calculate the difference vector
        diff = self - other

        # 2. Square each element in the difference vector
        squared_diff = [x ** 2 for x in diff.attributes]

        # 3. Sum the squared differences
        sum_squared_diff = sum(squared_diff)

        # 4. Take the square root of the sum
        distance = math.sqrt(sum_squared_diff)

        return distance

    def __repr__(self):
        attribute_str = ", ".join(f"{a:.2f}" for a in self.attributes)
        return f"Vector({attribute_str})"


# Example Usage: Finding similar users based on age, monthly spend, and site visits
user_A = Vector([25, 150.0, 12])
user_B = Vector([26, 145.0, 15]) # Very similar to A
user_C = Vector([55, 10.0, 2])   # Very different from A

dist_A_B = user_A.distance(user_B)
dist_A_C = user_A.distance(user_C)

print(f"Distance between User A and User B: {dist_A_B:.2f}")
print(f"Distance between User A and User C: {dist_A_C:.2f}")
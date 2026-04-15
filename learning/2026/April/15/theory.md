# AI/ML Concept: The Global Compass

When we trained on a single house, the gradients only pointed toward the perfect answer for *that specific house*. 

**Batch Gradient Descent** acts as a global compass. By passing an entire matrix $X$ through the network and calculating the average error, the gradients point toward the mathematical compromise that minimizes the error for *every house in the dataset simultaneously*.

Why do we use the transpose $X^T$ in the math? Think about it geometrically. $X$ transforms our weights into predictions. $X^T$ does the exact opposite: it takes the final errors and maps them *backwards* onto the specific features (like Bedrooms or SqFt) that caused them!
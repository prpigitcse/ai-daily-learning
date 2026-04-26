# Math: The Sigmoid Function

Linear regression relies on the equation $z = X\vec{w} + b$. When applied to probability, this linear dot product fails because it outputs values extending towards negative and positive infinity, violating the foundational rule that probabilities must exist between $0$ and $1$.

The **Sigmoid Function** ($\sigma$) mathematically squashes any real number into a strict $0.0$ to $1.0$ boundary:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

**Mathematical Limits:**
* As $z \to \infty$, $e^{-z} \to 0$. The equation resolves to $\frac{1}{1 + 0} = 1.0$.
* As $z \to -\infty$, $e^{-z} \to \infty$. The equation resolves to $\frac{1}{1 + \infty} = 0.0$.
* When $z = 0$, $e^{0} = 1$. The equation resolves to $\frac{1}{1 + 1} = 0.5$ (The decision boundary).
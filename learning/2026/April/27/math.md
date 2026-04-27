# Math Intuition: Why MSE Fails & The Log Loss Solution

Mean Squared Error (MSE) creates a convex, smooth "bowl" shape when applied to straight linear equations, allowing Gradient Descent to easily find the global minimum. However, when the output is wrapped in a non-linear Sigmoid function, the MSE error landscape becomes non-convex (bumpy with multiple local minima), causing the optimization algorithm to get permanently stuck.

To restore convexity, the objective function is changed to **Binary Cross-Entropy (Log Loss)**:
$$Loss = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$$

**The Mathematical Mechanism:**
* **If the truth is $y = 1$:** The right term cancels out. The loss is evaluated strictly on $-\log(\hat{y}_i)$. If the predicted probability is $0.99$, the loss is near zero. If the prediction is $0.01$, the loss approaches infinity.
* **If the truth is $y = 0$:** The left term cancels out. The loss is evaluated strictly on $-\log(1 - \hat{y}_i)$, aggressively punishing confident false positives.
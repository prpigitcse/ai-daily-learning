# Math: The Mathematical System

Over the past 6 days, we have built individual mathematical components:
* **Data** as Vectors in space ($x \in \mathbb{R}^n$)
* **Weights** mapping importance ($w$)
* **Bias** providing a baseline ($b$)
* **Dot products** for predictions ($\hat{y} = w \cdot x + b$)
* **Mean Squared Error** for evaluation ($J(w,b) = \frac{1}{n}\sum(y_i - \hat{y}_i)^2$)

Today, we acknowledge that these equations do not exist in isolation. They form a single mathematical system. 


Data flows in, predictions flow out, error is measured, and parameters are adjusted. The system's entire goal is to find the specific values of $w$ and $b$ that minimize the output of the $J(w,b)$ error function.
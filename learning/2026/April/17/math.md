# Math: The Complete Pipeline

We don't need any new equations today. Instead, we are orchestrating the math we derived over the last 15 days into a strict, cyclical lifecycle:

1. **Initialization:** Set $\vec{w}$ to zeroes and $b$ to $0.0$.
2. **The Forward Pass:** $\vec{\hat{y}} = X\vec{w} + b$
3. **The Loss Evaluation:** $MSE = \frac{1}{N} \sum (\hat{y}_i - y_i)^2$
4. **The Backward Pass (Gradients):**
   * $\text{Grad\_w} = \frac{2}{N} X^T (\vec{\hat{y}} - \vec{y})$
   * $\text{Grad\_b} = \frac{2}{N} \sum (\vec{\hat{y}} - \vec{y})$
5. **The Update:** Step $\vec{w}$ and $b$ against the gradients using the learning rate ($\alpha$).
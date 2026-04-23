# Math: The Complete Regularized Update

We do not need to invent any new equations today; we just need to orchestrate them into the Batch Gradient Descent loop. 

During the `.fit()` phase, the loop must calculate the error, derive the base gradients, and then immediately add the chosen penalty (Ridge $L_2$, Lasso $L_1$, or ElasticNet) to the weight gradients before taking a step.

1. **Forward Pass:** $\vec{\hat{y}} = X\vec{w} + b$
2. **Base Gradients:**
   * $\text{Grad\_w\_base} = \frac{2}{N} X^T (\vec{\hat{y}} - \vec{y})$
   * $\text{Grad\_b} = \frac{2}{N} \sum (\vec{\hat{y}} - \vec{y})$
3. **The Penalty Injection (e.g., Ridge):**
   $$\text{Grad\_w\_final} = \text{Grad\_w\_base} + \frac{2\lambda}{N} \vec{w}$$
4. **The Update:** * $\vec{w}_{\text{new}} = \vec{w}_{\text{old}} - \alpha \cdot \text{Grad\_w\_final}$
   * $b_{\text{new}} = b_{\text{old}} - \alpha \cdot \text{Grad\_b}$
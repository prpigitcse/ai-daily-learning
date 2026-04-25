# Math: The Master Equation

The foundational linear regression architecture culminates in a single, regularized batch gradient update equation.

**The Weight Update (e.g., Ridge):**
$$w_{\text{new}} = w_{\text{old}} - \alpha \left( \frac{2}{N} X^T (\vec{\hat{y}} - \vec{y}) + \frac{2\lambda}{N} \vec{w} \right)$$

* $\alpha$: The step size (Learning Rate).
* $\frac{2}{N} X^T (\vec{\hat{y}} - \vec{y})$: The base gradient derived from the Mean Squared Error.
* $\frac{2\lambda}{N} \vec{w}$: The $L_2$ penalty gradient, scaling the force of the regularization constraints.
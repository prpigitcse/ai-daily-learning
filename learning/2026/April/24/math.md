# Math: Algorithmic Convergence

When evaluating custom Batch Gradient Descent algorithms against production libraries like Scikit-Learn, exact decimal parity in weight distribution is rare due to differing underlying optimization strategies. However, the models converge on the same global minimum.

$$W_{\text{custom}} \approx W_{\text{sklearn}}$$

* **Batch Gradient Descent (Custom):** Iteratively minimizes the error function by updating all weights simultaneously using partial derivatives scaled by the learning rate ($\alpha$).
* **Analytical Solvers (Sklearn Ridge/Linear):** Utilizes linear algebra techniques such as Cholesky Decomposition or Singular Value Decomposition (SVD) to calculate the exact global minimum algebraically in a single step, bypassing epochs.
* **Coordinate Descent (Sklearn Lasso):** Iteratively optimizes a single weight while holding all others constant. This mathematically resolves the non-differentiability of the $L_1$ penalty's absolute value at exactly $0$.

Despite divergent mathematical paths, sound implementations converge on highly comparable $R^2$ scores and directional weight distributions.
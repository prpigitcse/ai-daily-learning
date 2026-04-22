# Math: Penalizing Confidence ($L_2$ Ridge)

If a model is allowed to grow its weights to infinity, it will exploit highly correlated features by assigning massive positive and negative weights that cancel each other out. This makes the model extremely unstable in production.

To stop this, we change the Loss Function. We add a **Penalty Term** that punishes the model simply for having large weights. 

The $L_2$ (Ridge) penalty adds the squared sum of all weights to the Mean Squared Error, scaled by a tuning parameter called Lambda ($\lambda$):
$$Loss = MSE + \lambda \sum_{j=1}^{M} w_j^2$$

**The Calculus Update:**
Because we changed the Loss function, we must take the derivative of this new penalty term to update our gradients. The derivative of $\lambda w^2$ with respect to a specific weight $w$ is $2\lambda w$. 

So, our new Batch Gradient for the weights becomes:
$$\text{Grad\_w} = \text{Original\_Grad\_w} + \frac{2\lambda}{N} \vec{w}$$
*(Note: We divide the penalty by $N$ to keep it on the same scale as our MSE average).*

**Crucial Rule:** We **never** regularize the bias ($b$). The bias just shifts the baseline up or down; it doesn't cause overfitting. The gradient for the bias remains unchanged.
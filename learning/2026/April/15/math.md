# Math: Matrix Calculus

For the last three days, we have calculated the gradient for a single data point (one house). But a real dataset ($X$) contains hundreds of houses, and multiple features per house. 

When predicting a whole batch, our Forward Pass is:
$$\vec{\hat{y}} = X\vec{w} + b$$

The Loss for the whole batch is the Mean Squared Error (the average error across all houses, where $N$ is the number of houses):
$$MSE = \frac{1}{N} \sum (\hat{y}_i - y_i)^2$$

How do we calculate the partial derivatives for an entire matrix of data? We use **Matrix Calculus**. 

1. **The Batch Gradient for Weights ($\frac{\partial L}{\partial \vec{w}}$):**
   Instead of multiplying the error by a single $x$, we take the *dot product* of our dataset Matrix and the error vector. To make the inner dimensions align, we must multiply the Transpose of the dataset ($X^T$) by the error vector ($\vec{\hat{y}} - \vec{y}$). Finally, we divide by $N$ to get the average gradient across the batch:
   $$\text{Gradient\_w} = \frac{2}{N} X^T (\vec{\hat{y}} - \vec{y})$$

2. **The Batch Gradient for Bias ($\frac{\partial L}{\partial b}$):**
   The bias doesn't interact with the features ($X$), it just shifts the final prediction. So the batch gradient for the bias is simply the average of all the raw errors in the batch:
   $$\text{Gradient\_b} = \frac{2}{N} \sum (\vec{\hat{y}} - \vec{y})$$
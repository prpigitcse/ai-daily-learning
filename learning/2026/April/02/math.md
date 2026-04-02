# Math: Calculating Squared Error

When we make a prediction, we need to mathematically quantify how wrong we are. We do this by calculating the difference between the actual truth ($y$) and our prediction ($\hat{y}$). This is called the residual or error: $(y - \hat{y})$.

However, if we just add up all our errors across multiple predictions, a prediction that is too high ($+50$) and a prediction that is too low ($-50$) would cancel each other out to $0$. This would falsely tell us our model is perfect!

To fix this, we square the error: $(y - \hat{y})^2$. 



Squaring does two critical things:
1. It forces all errors to be positive (since a negative multiplied by a negative is a positive).
2. It heavily penalizes large errors. Being off by 10 results in an error of 100, but being off by 20 results in an error of 400. 

To find the average error across an entire dataset of $n$ predictions, we sum up all the squared errors and divide by $n$. This formula is the Mean Squared Error (MSE):
$$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
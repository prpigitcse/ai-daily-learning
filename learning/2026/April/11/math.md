# Math: The Batch System

In Week 1, our system processed one single data point at a time:
$$\hat{y} = (\vec{w} \cdot \vec{x}) + b$$

By building our `Matrix` class, we have upgraded our mathematical engine to process $n$ data points simultaneously. Our entire dataset $X$ is multiplied by our weights vector $\vec{w}$ in a single batch operation, and our scalar bias $b$ is added to every resulting prediction.

Because $X$ is an $m \times n$ matrix (where $m$ is the number of samples and $n$ is the number of features), and $\vec{w}$ is a vector of length $n$, the product $X\vec{w}$ results in a vector of length $m$. 

$$\vec{y} = X\vec{w} + b$$

This means instead of generating one prediction, our forward pass generates an entire vector of predictions ($\vec{y}$). We then pass that entire vector into our Mean Squared Error function to calculate the total loss for the batch.
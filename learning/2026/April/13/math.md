# Math: The Chain Rule

In machine learning, our math is a chain of functions nested inside each other. 
1. We calculate a prediction: $\hat{y} = w \cdot x$
2. We plug that prediction into our loss function: $L = (\hat{y} - y)^2$

If we substitute the first equation into the second, our full equation is: 
$$L = ((w \cdot x) - y)^2$$

How do we find the derivative of this nested function with respect to our weight ($\frac{\partial L}{\partial w}$)? We use **The Chain Rule**. 


The Chain Rule states that the derivative of nested functions is the product of their individual derivatives. 
$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w}$$

Let's break that down:
* **The Outer Derivative ($\frac{\partial L}{\partial \hat{y}}$):** How does the prediction affect the loss? Using the power rule on $L = (\hat{y} - y)^2$, the derivative is $2(\hat{y} - y)$.
* **The Inner Derivative ($\frac{\partial \hat{y}}{\partial w}$):** How does the weight affect the prediction? The derivative of $\hat{y} = w \cdot x$ with respect to $w$ is just $x$.

Multiply them together, and you have the exact formula for your gradient:
$$\text{Gradient} = 2(\hat{y} - y) \cdot x$$
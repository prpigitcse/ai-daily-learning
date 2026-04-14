# Math: Partial Derivatives

Yesterday, we took the derivative of our loss function with respect to a single weight. But a real prediction equation has a bias ($b$) as well:
$$\hat{y} = (w \cdot x) + b$$

When we plug this into our squared error loss function, it looks like this:
$$L = ((w \cdot x) + b - y)^2$$


Now we have two parameters we can change to reduce the error: $w$ and $b$. To figure out how to update them, we need to take the derivative of the loss with respect to $w$, and *also* the derivative of the loss with respect to $b$. 

When you have an equation with multiple variables and you take the derivative for just one of them, it is called a **Partial Derivative** (denoted with the symbol $\partial$ instead of a standard $d$). 

To take a partial derivative, you treat the variable you are focusing on as normal, and you pretend every other variable is just a constant number. 

1. **The Partial Derivative with respect to $w$ ($\frac{\partial L}{\partial w}$):**
   Using the Chain Rule, the outer derivative is $2(\hat{y} - y)$. The inner derivative of $(w \cdot x) + b$ with respect to $w$ is just $x$ (because the constant $b$ disappears).
   $$\frac{\partial L}{\partial w} = 2(\hat{y} - y) \cdot x$$

2. **The Partial Derivative with respect to $b$ ($\frac{\partial L}{\partial b}$):**
   The outer derivative is exactly the same: $2(\hat{y} - y)$. The inner derivative of $(w \cdot x) + b$ with respect to $b$ is just $1$ (because the derivative of $b$ is $1$, and the $w \cdot x$ term is treated as a constant and disappears).
   $$\frac{\partial L}{\partial b} = 2(\hat{y} - y) \cdot 1$$
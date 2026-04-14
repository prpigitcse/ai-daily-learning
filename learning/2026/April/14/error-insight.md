# Developer's Insight: Disconnected Pipelines & Self-Scaling Math

During this implementation, I ran into an architectural bug and discovered a fascinating mathematical property of gradient descent.

**1. The Disconnected Pipeline Bug**
Initially, the math wasn't working because I forgot to add the bias into the `forward_pass` function. Even though my gradient formulas were perfect, the parameters updating at the bottom of the loop were disconnected from the prediction generation at the top. If a parameter isn't used in the forward pass, it cannot impact the loss, rendering backpropagation useless. 

**2. Non-Linear Step Scaling**
I ran experiments adjusting the `learning_rate` ($\alpha$). I noticed that increasing the learning rate by 5 times (from 0.01 to 0.05) decreased the required epochs by almost 7 times (from 140 to 22). The speedup isn't perfectly 1:1; larger learning rates compound their efficiency right up until the point they cause the model to diverge.

**3. The Self-Scaling Gradient**
I tested changing the target dataset. I increased $y$ from 150 to 200, and then increased both $x$ and $y$ simultaneously. To my surprise, the model converged in the exact same number of epochs. 
Why? Because the gradient equation `2 * x * (y_hat - y)` scales itself. If the target $y$ is much larger, the initial error is massive. This causes the gradient to output a massive step size right out of the gate. The math automatically leaps further to cover the larger distance in the same amount of time.
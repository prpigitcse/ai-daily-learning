# Developer's Insight: Reading the Rubber Band

When I first wrote my regularized gradient function, I ran a quick test using a massive fake weight ($200.0$) and a $\lambda$ of $100$. 

The base, unpenalized MSE gradient was `-5.0`. In gradient descent, we *subtract* the gradient, meaning the raw MSE was actively telling the model to increase the weight and make it even more massive!

When I printed the final regularized gradient, it had flipped to `39999.97`. The penalty completely overpowered the MSE. By flipping the gradient positive, it forces the update rule to heavily subtract from the weight, snapping it back down toward zero. 

**The Bug:** I also realized exactly why my output was basically $40000$ (which is $2 \cdot 100 \cdot 200$). I forgot to divide my penalty calculation by $N$! If you don't divide by the number of data points, the penalty scales to infinity as your dataset grows, instantly crushing your weights to zero regardless of the MSE. Dividing by $N$ ensures the penalty's force remains proportional to the error term.
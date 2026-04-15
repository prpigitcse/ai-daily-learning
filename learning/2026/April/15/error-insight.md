# Developer's Insight: Triggering an Explosion

I wanted to see what would happen if I didn't manually pre-scale my dataset. I changed the inputs from `[1.0, 2.0, 3.0]` (representing thousands) back to their raw numbers: `[1000.0, 2000.0, 3000.0]`. 

The entire engine collapsed almost instantly:
`Epoch 38: Weight = [6.49e+150, 3.71e+148], Bias = 2.78e+147, Loss = 2.25e+300`

**The Insight:** Feature scaling isn't just an optimization trick; it is mathematically mandatory for gradient descent. Because the gradient formula contains the term $x$, feeding $x = 1000$ into the equation creates a massive initial step size. 

The model overshoots the minimum so violently that the new error is larger than the starting error. This larger error multiplies by $x=1000$ again, creating an even larger step, creating a positive feedback loop. In just 38 epochs, the loss exploded to $e+300$. Without normalizing the features to the same scale, the math literally rips itself apart.
# AI/ML Concept: Isolating the Blame

Why do we calculate two separate gradients? Because $w$ and $b$ do entirely different things geometrically. 

* The weight ($w$) changes the *angle* or *slope* of our prediction line.
* The bias ($b$) shifts the entire prediction line *up or down* the y-axis.

If a prediction is wrong, the network needs to know exactly how much of the error was caused by a bad angle, and exactly how much was caused by a bad vertical shift. Partial derivatives allow the neural network to isolate the blame. 

The Loss function looks at the total error and splits it up:
* "Weight, if you change by this specific amount ($\frac{\partial L}{\partial w}$), the error will go down."
* "Bias, if you shift by this entirely different amount ($\frac{\partial L}{\partial b}$), the error will also go down."

We then apply the Gradient Descent update rule to *both* of them simultaneously.
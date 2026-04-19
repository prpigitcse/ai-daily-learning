# Developer's Insight: Reading the Gradient Output

After generating the non-linear dataset, I fed it into my `LinearRegressor` from Week 3 and ran a full Batch Gradient Descent to see how it would attempt to solve it. 

The model converged and output a prediction, but inspecting the internal weights (`[-49.29, 215.77, 97.85, 0.0, 231.04, 142.48]`) revealed two massive conceptual flaws caused by the raw matrix representation.

**1. The Multicollinearity Trap**
The weights for `Occupants` (215.77) and `Devices` (231.04) are both massive. In my data generator, I explicitly made `Devices` highly correlated with `Occupants`. Because these two features move together perfectly, the gradient descent math couldn't isolate the blame. It assigned massive, competing weights to both of them, proving that correlated features make linear models highly unstable.

**2. The Straight Line Fallacy**
The model assigned a weight of 142.48 to the `Day of the year` feature. In linear regression, this means the model mathematically assumes that as the day number increases (from Day 1 to Day 365), energy consumption just keeps going up. 

This is completely wrong. The year is a cyclical season. Day 365 and Day 1 share the exact same winter weather and should have nearly identical energy profiles. Because my input matrix simply provided raw integers (1 to 365), the linear engine tried to draw a straight line through a continuous loop. To fix this, I need to physically alter the representation of the data in the matrix before it reaches the gradient descent loop.
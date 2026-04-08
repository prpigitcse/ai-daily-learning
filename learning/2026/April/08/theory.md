# AI/ML Concept: Deep Learning & Hidden Layers

Why do we need to multiply two matrices together? This is the exact mathematical operation that unlocks **Deep Learning**. 

Up until now, our model only had one layer of weights. But neural networks have "hidden layers". Imagine we don't just want to predict a house's *Price*. Maybe our first layer of weights calculates three intermediate concepts: "Luxury Score", "Space Score", and "Location Score". 

* $X$ is our dataset matrix (e.g., $1000$ houses $\times$ $4$ features).
* $W_1$ is a matrix of weights mapping $4$ features to $3$ "Scores" (shape $4 \times 3$).

When we calculate $X \cdot W_1$, we get a new $1000 \times 3$ matrix. We have successfully transformed our entire dataset of $4$ raw features into a new dataset of $3$ high-level concepts! We can then pass that *new* matrix into a second layer of weights ($W_2$) to get our final price prediction. Matrix-matrix multiplication is how data flows forward through the multiple hidden layers of a deep neural network.
# AI/ML Concept: Backpropagation (Single Node)

This concept of multiplying derivatives backward through a chain of equations is called **Backpropagation**. 

When data flows forward through our network to make a prediction, it is called the *Forward Pass*. But when we calculate the error, we have to trace that error backward to see exactly who is responsible for it. We propagate the error backwards.

* The Loss function says: "Hey $\hat{y}$, you were off by this much!" (The Outer Derivative)
* The Prediction function $\hat{y}$ turns around to the weight and says: "Hey $w$, because the input $x$ was this size, your portion of the blame is this!" (The Inner Derivative multiplied by the Outer)

By chaining these derivatives together, the neural network can assign exact mathematical blame to every single weight, no matter how many hidden layers deep it is.
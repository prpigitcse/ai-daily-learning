# AI/ML Concept: The Training Loop

We now have all the individual pieces of an Artificial Intelligence engine:
1. **The Data:** Features translated into numbers.
2. **The Model:** Weights and Bias combined to make predictions.
3. **The Evaluation:** The Loss Function from [Measuring Error: How Wrong is Our Model?](/2026/april/02/measuring-error-how-wrong-is-our-model) to measure how wrong we are.

Today, we connect these pieces into the **Training Loop**. Machine learning is not magic; it is simply a loop that repeats these three steps:
1. **Predict:** Make a prediction using the current weights.
2. **Evaluate:** Calculate the loss (MSE).
3. **Optimize:** Adjust the weights slightly to try and make the loss smaller.

By randomly nudging our weights up and down, keeping the changes that lower the error, and discarding the ones that increase it, we can actually watch the machine "learn" the relationship between the data and the truth through computation.
# AI/ML Concept: The Batch Regressor

Why do we go through all the trouble of building matrices? **Parallelization.**

If you train a model on 10,000 images one by one, your CPU has to execute the forward pass 10,000 separate times. But if you pack those 10,000 images into a Design Matrix $X$, the operation $X\vec{w}$ is just one mathematical instruction. Modern hardware (like NVIDIA GPUs) is designed to compute the thousands of tiny multiplications required for $X\vec{w}$ simultaneously. 

Today, we upgrade the `SimpleLinearRegressor` from Week 1. Instead of taking a standard list of numbers, it will now accept our new `Matrix` object as its input data, allowing it to learn from multiple features (like Bedrooms *and* Square Footage) at the exact same time.
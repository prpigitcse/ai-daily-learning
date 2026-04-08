# AI/ML Concept: The Batch Forward Pass

In (The Capstone: Object-Oriented ML Architecture)[/2026/april/04/the-capstone-object-oriented-ml-architecture], to make predictions for 3 houses, we had to run our predict method 3 separate times. In Python, this requires a `for` loop, which is notoriously slow for large datasets.

By using Matrix-Vector multiplication, we can push the entire dataset through the model in a single mathematical operation. 
* Let $X$ be our Design Matrix (e.g., $1000$ houses, $4$ features each).
* Let $\vec{w}$ be our Weights Vector ($4$ weights).

When we compute $X\vec{w}$, the math automatically calculates the dot product (prediction) for all $1,000$ houses simultaneously, returning a single vector of $1,000$ predictions. This is called a **Batch Forward Pass**. 

When hardware like NVIDIA GPUs run this operation, they calculate all $1,000$ dot products at the exact same time in parallel. This specific mathematical operation is the foundational secret to why modern AI can train on massive datasets so quickly.
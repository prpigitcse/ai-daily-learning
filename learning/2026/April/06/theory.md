# AI/ML Concept: Manipulating the Dataset

Why do we need these operations? In machine learning, we rarely use raw data exactly as it comes to us. We need to preprocess it so our neural networks can digest it effectively. 

* **Scalar Multiplication (Scaling):** Imagine our dataset has a column for "Square Footage" where values are in the thousands (e.g., $2500$) and another for "Bedrooms" (e.g., $3$). Large numbers can overwhelm an AI model and make training unstable. We use scalar multiplication to scale entire datasets down (e.g., multiplying the matrix by $0.001$) so the AI can process the data smoothly.
* **Matrix Addition (Shifting/Bias):** When processing entire batches of data at once, we still need to add our Bias ($b$) to our predictions, just like we did in Week 1. Matrix addition allows us to add that base bias across thousands of predictions simultaneously.
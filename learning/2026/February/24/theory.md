# AI/ML Concept: Applying Importance (Weights)

In machine learning, the dot product is how a model applies "importance" to different features. We call this level of importance a "weight". 

When predicting a house price, not all features are equally important. Let's look at how a model might process this using a dot product:

| Feature | Value (Vector x) | Weight (Vector w) | Product (x * w) |
| :--- | :--- | :--- | :--- |
| Bedrooms | 3 | 50000 | 150000 |
| Age (years) | 15 | -2000 | -30000 |

The dot product combines them: $(3 \times 50000) + (15 \times -2000) = 120000$. The model has used the dot product to calculate a mathematical prediction by scaling our data by its learned weights.
# AI/ML Concept: The Design Matrix

In Week 1, we built an engine that could look at a single house (a vector) and predict a price. But in the real world, we don't train AI on one house at a time; we train it on thousands or millions of houses simultaneously. 

To achieve this, your entire dataset is represented as a single matrix. We call this the **Design Matrix** and denote it with a capital $X$. 

The standard convention in AI is:
* **Rows ($m$)** represent individual samples (e.g., individual houses, individual users).
* **Columns ($n$)** represent the features (e.g., bedrooms, age, square footage).

If we have a dataset of 3 houses, and each house has 4 features, our dataset $X$ is a $3 \times 4$ matrix. 

| | Bedrooms (Col 1) | Bathrooms (Col 2) | Age (Col 3) | SqFt (Col 4) |
| :--- | :--- | :--- | :--- | :--- |
| **House 1 (Row 1)** | 3 | 2 | 15 | 2000 |
| **House 2 (Row 2)** | 4 | 3 | 10 | 2500 |
| **House 3 (Row 3)** | 2 | 1 | 50 | 1200 |

By structuring data this way, we can eventually use GPU acceleration to push this entire grid of numbers through our weights in a single mathematical operation, rather than using slow `for` loops.
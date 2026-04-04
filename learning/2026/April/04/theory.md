# AI/ML Concept: Object-Oriented ML Architecture

In standard software engineering, you separate your data from your business logic. In Machine Learning, we separate our **Data** from our **Model**.

Industry-standard libraries like `scikit-learn` use a very specific Object-Oriented architecture. A model is defined as a Class (e.g., `LinearRegressor`) that contains its own internal state (weights and bias). Every standard ML model shares two universal methods:

1. `.fit(X, y)`: This method triggers the training loop we built in [Brute-Force Learning: The Training Loop](/2026/april/03/brute-force-learning-the-training-loop). It takes in the features (`X`) and the truth (`y`), and optimizes the internal weights and bias.
2. `.predict(X)`: Once trained, this method takes in new, unseen data (`X`) and returns the model's predictions.

By wrapping our math into this architectural standard, we bridge the gap between educational scripts and production-ready machine learning code.
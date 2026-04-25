# System Architecture: The Glass Box Engine

Constructing a production-ready machine learning engine entirely from scratch establishes a transparent mathematical pipeline, bypassing black-box abstractions. 

The system executes in four distinct architectural phases:

1. **The Representation Layer (Linear Algebra):**
   * Data is ingested and cast into a mathematical $X$ matrix.
   * To prevent data leakage, the Z-score scaler computes its state strictly on the training matrix before transforming the data.
   * Non-linear complexities (cyclical time, parabolas, feature interactions) are engineered directly into the matrix columns prior to algorithm ingestion.
2. **The Forward Pass (The Hypothesis):**
   * The model calculates its prediction using the dot product: $\vec{\hat{y}} = X\vec{w} + b$.
3. **The Loss & Penalty Calculation (The Objective):**
   * The system calculates the Mean Squared Error (MSE).
   * Regularization mathematically penalizes large weights using $L_1$ (Lasso), $L_2$ (Ridge), or ElasticNet, explicitly dividing the penalty by the sample size $N$ to maintain scale stability across varying dataset volumes.
4. **The Backward Pass (Calculus & Optimization):**
   * The engine calculates the partial derivatives (gradients) of the loss function with respect to every single weight.
   * Batch Gradient Descent subtracts these gradients (scaled by the learning rate $\alpha$) from the current weights, iteratively descending the multidimensional error surface to locate the global minimum.
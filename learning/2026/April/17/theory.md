# AI/ML Concept: State & Encapsulation

Why do we wrap our math inside a `class LinearRegressor` instead of just running a loose script? **Statefulness and Data Leakage.**

When you train a model, it doesn't just need to remember its final weights and bias. If your training dataset had an average house size of 2000 SqFt, and you later ask the model to predict the price of a *new* unseen 2500 SqFt house, you cannot calculate a new mean and standard deviation for that single new house! 

You must scale the new house using the *exact same* Mean and Standard Deviation that the model learned during training. Otherwise, the Z-score will be mapped to the wrong mathematical space, and the prediction will be garbage. 

A production-grade ML class must encapsulate its state. It saves its `feature_means` and `feature_stds` during the `.fit()` phase, so it can flawlessly apply them without recalculation during the `.predict()` phase.
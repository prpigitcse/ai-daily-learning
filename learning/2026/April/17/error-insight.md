# Developer's Insight: API Design and Data Leakage

While orchestrating the final `LinearRegressor` class, the biggest architectural challenge wasn't the calculus—it was managing the state of the data normalization. 

I split the scaling logic into three distinct methods: `_fit_scaler`, `_transform`, and `_fit_transform`. 

**The Insight:** Why not just scale the matrix right before prediction using the new data? Because of Data Leakage. 
If the model is trained on houses averaging 2000 SqFt (Mean = 2000), it aligns its weights to that specific mathematical center. If I pass in a single test house that is 3000 SqFt and calculate a *new* mean just for that house, its mean becomes 3000, and its Z-score becomes 0.0. The neural network will treat it like an "average" house, utterly destroying the prediction. 

By explicitly saving `self.feature_means` and `self.feature_stds` during the `fit()` stage, the `predict()` method is forced to scale incoming test data according to the worldview the model was originally trained on. This strict separation of state perfectly mirrors the design of professional libraries like Scikit-Learn.
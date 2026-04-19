# AI/ML Concept: The Trap of Multicollinearity

When generating this dataset, we intentionally injected a fatal flaw that ruins naive linear regression: **Multicollinearity**. 



This occurs when two features in your matrix are highly correlated with each other. For example, the `num_occupants` in a building heavily dictates the `num_devices_on`. If you know one, you basically know the other. 

Why is this dangerous? Because the Gradient Descent algorithm isolates blame using Partial Derivatives. If two variables move together perfectly, the math cannot determine which variable is *actually* responsible for the rising energy bill. The gradients become highly unstable, and the weights wildly oscillate trying to split the blame. 

By building this into our synthetic data today, we are setting up the exact problem that $L_2$ (Ridge) Regularization is designed to solve.
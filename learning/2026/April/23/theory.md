# AI/ML Concept: Hyperparameters vs. Parameters

As we upgrade our class to handle Regularization, there is a distinct separation in how variables are handled. This is the difference between Hyperparameters and Parameters.

* **Hyperparameters ($\lambda$, $\alpha$, Epochs, Type):** These are the architectural dials. The machine cannot learn them. The engineer must set them in the `__init__` method before the model ever sees a single row of data. 
* **Parameters ($\vec{w}$, $b$):** This is the model's internal state. They are strictly initialized to zero and learned dynamically inside the `.fit()` method. 

By passing `lambda_param` into the constructor, we give the engineer the power to mathematically tighten or loosen the regularization based on how messy the incoming dataset is.
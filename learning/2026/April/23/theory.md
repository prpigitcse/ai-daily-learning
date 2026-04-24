# AI/ML Concept: Hyperparameters vs. Parameters

Machine learning architectures enforce a strict mathematical separation in how state variables are handled during training:

* **Hyperparameters ($\lambda$, $\alpha$, Epochs, Type):** These are the architectural dials. They dictate the behavior of the training algorithm itself. They are not learned by the machine and must be set in the object initialization phase before any data is processed.
* **Parameters ($\vec{w}$, $b$):** This is the model's internal mathematical state. They are strictly initialized to zero and learned dynamically inside the training optimization loop.

Passing `lambda_param` into the constructor allows the engineer to dictate the mathematical tension of the regularization based on the specific variance and noise of the incoming dataset.
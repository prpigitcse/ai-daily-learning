# AI/ML Concept: Linear in Weights, Non-Linear in Features

"Linear regression is not weak. It’s actually very powerful if you give it the right representation."

When you add a $x^2$ column or a $\sin(x)$ column to your matrix, the model is still executing a strictly linear equation: 
$$\hat{y} = w_1 x_1 + w_2 x_1^2 + w_3 \sin(x_2) + b$$



The algorithm is just scaling weights ($w_1, w_2, w_3$) and adding them up. It is entirely linear with respect to the *weights*. But because the *input features* are curved, the final prediction line that the model outputs is bent perfectly to match the chaos of reality. 

Feature engineering is the art of giving your linear model a non-linear vocabulary.
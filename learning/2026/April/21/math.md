# Math: The Coefficient of Determination ($R^2$)

To scientifically prove how much better our engineered matrix is, we compare it against the "dumbest possible model." The dumbest possible model ignores all features ($X$) and just predicts the average energy consumption ($\bar{y}$) for every single day. 

We calculate two things:
1.  **Total Sum of Squares (TSS):** The total error of the "dumb" mean model. It measures how much the true energy values vary from their own average.
    $$TSS = \sum (y_i - \bar{y})^2$$
2.  **Residual Sum of Squares (RSS):** The total error of *our* model. It measures how much the true energy values vary from our predictions. 
    $$RSS = \sum (y_i - \hat{y}_i)^2$$

Finally, we calculate $R^2$:
$$R^2 = 1 - \frac{RSS}{TSS}$$

* If our model's error (RSS) is exactly equal to the dumb model's error (TSS), $\frac{RSS}{TSS}$ equals 1, and $1 - 1 = 0$. Our model explains **0%** of the data's variance. 
* If our model makes zero mistakes, RSS is 0, and $1 - 0 = 1$. Our model explains **100%** of the variance. 
* Because RSS cannot be negative, $R^2$ can **never** be greater than 1.
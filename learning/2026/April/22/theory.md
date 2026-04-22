# AI/ML Concept: The Rubber Band Effect

Why does squaring the weights fix multicollinearity? It comes down to the geometry of exponents. 

Imagine two features are perfectly correlated, and the model needs them to contribute a total value of 1.0 to the prediction. 
* **Scenario A (Unregularized):** The model sets $w_1 = 10$ and $w_2 = -9$. The net effect is 1.0. The MSE is happy. But the $L_2$ penalty calculates: $10^2 + (-9)^2 = 181$. Massive penalty!
* **Scenario B (Regularized):** The model sets $w_1 = 0.5$ and $w_2 = 0.5$. The net effect is still 1.0. The MSE is still happy. But the $L_2$ penalty calculates: $0.5^2 + 0.5^2 = 0.5$. Very low penalty!

$L_2$ Regularization acts like a rubber band attached to every weight, pulling them toward zero. The larger the weight grows, the harder the rubber band pulls back. This mathematically forces the algorithm to distribute the workload evenly across correlated features instead of letting one dominate.
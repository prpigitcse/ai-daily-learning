# Developer's Insight: Asymptotic Convergence

While running the Backpropagation loop, I noticed an interesting pattern with the Loss over time. I had to manually increase the `epochs` variable to track when the model actually finished learning.

Here is what I observed during execution:
* **Epoch 20:** Loss = **404.0076**
* **Epoch 50:** Loss = **2.7143** (Still dropping rapidly)
* **Epoch 100:** Loss = **0.0006** (Slowing down significantly)
* **Epoch 112:** Loss = **0.00008** (Converged. Barely changing after this point).

**The Insight:** Why does the learning slow down so drastically at the end? It is mathematically baked into our gradient formula: `2 * x * (y_hat - y)`. 
        
As the model gets smarter, the prediction `y_hat` gets closer and closer to the true target `y`. This means the error `(y_hat - y)` approaches $0$. Since the error is multiplying the entire gradient equation, the *gradient itself* shrinks toward $0$. 

Because the gradient is shrinking, our step sizes get microscopically small. The model takes massive leaps when it's wrong, but delicately tip-toes as it approaches the exact right answer. This is known as asymptotic convergence!
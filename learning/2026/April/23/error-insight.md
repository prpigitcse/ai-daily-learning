# Developer's Insight: The Default Parameter Trap

During the finalization of the regularization suite, two architectural concepts became clear regarding mathematical representations and API design.

**1. The Polynomial Surface Equation**
Initially, keeping both the raw `Temp` feature and the engineered `Temp_Squared` feature in the matrix seemed redundant. However, a true quadratic equation is $ax^2 + bx + c$. If the model is only provided with $x^2$, it is forced to center the parabola exactly at $0$. Providing both $x$ and $x^2$ allows the model to mathematically shift the U-shape along the axis to locate the true optimal temperature. 
The exact same logic applies to interaction terms. Maintaining `Occupants` ($x$), `Hours` ($y$), and `Occupant_Hours` ($xy$) maps to the surface equation $axy + bx + cy + d$. The model requires all components to isolate baseline effects from the synergistic effect.

**2. The Default Parameter Trap**
When testing the new Ridge, Lasso, and ElasticNet classes with high lambda values ($\lambda=100$), the weights remained static. The regularization was mathematically sound, but an API routing bug bypassed the logic entirely. During instantiation, omitting the explicit `type` parameter caused the class to fall back to its `"linear"` default, silently disabling the penalty gradients. Flawless mathematical logic is ineffective if the software routing defaults to the incorrect execution path.

**3. The Polynomial Surface Equation**
Initially, I wondered why I kept both the raw `Temp` feature AND the engineered `Temp_Squared` feature in the matrix. Why not just pass the square? Then the algebra clicked. A true quadratic equation is $ax^2 + bx + c$. If I only provide $x^2$, the model is forced to center the parabola exactly at $0$. By providing both $x$ and $x^2$, the model can mathematically shift the U-shape left and right to find the true optimal temperature. 
The exact same logic applies to my interaction term. I keep `Occupants` ($x$), `Hours` ($y$), and the combined `Occupant_Hours` ($xy$) because the true mathematical surface is $axy + bx + cy + d$. The model needs all the pieces to map the baseline effects *plus* the synergistic effect.


**The Bug:** When I checked the output, the weights for `lambda=100` were identical down to the decimal point to the weights for `lambda=0.01`. The $R^2$ scores never budged. My regularization was completely silent. I immediately assumed my calculus was wrong or that I forgot to wire the penalty into the gradient update loop. But after tearing the logic apart, I realized the math was flawless. The bug was in my API routing. 

When I instantiated my model class in the test script, I forgot to explicitly pass the `type` parameter (e.g., `type="ridge"`). Because my class was designed to default to `"linear"`, it silently bypassed all of my new regularization logic entirely. It was a classic software engineering trap: a perfectly written engine is useless if the routing switch is flipped to the wrong default.


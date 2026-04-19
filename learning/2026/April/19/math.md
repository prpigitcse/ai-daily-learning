# Math: The Target Function & Irreducible Error

When we train a model, we are trying to approximate a true, hidden function that governs the universe. Mathematically, the real-world value ($y$) is a combination of a deterministic function ($f(X)$) and random, unpredictable noise ($\epsilon$).

$$y = f(X) + \epsilon$$

To simulate our Smart Building, we need to design $f(X)$ to be intentionally messy:

1. **Non-Linearity:** Energy consumption isn't a straight line with temperature. If the ideal building temperature is 22°C, energy spikes when it gets hotter (AC) *and* when it gets colder (Heating). This forms a parabola.
   $$E_{\text{temp}} = \beta_1(T - 22)^2$$
2. **Seasonality:** The day of the year naturally cycles. We represent this continuous loop using a sine wave, where $d$ is the day of the year. 
   $$E_{\text{season}} = \beta_2 \sin(\frac{2\pi \cdot d}{365})$$
3. **Interaction Terms:** A building only uses massive energy if there are many occupants *and* it is open for many hours. We multiply them to create a combined effect.
   $$E_{\text{active}} = \beta_3(\text{occupants} \times \text{hours})$$

Finally, we add $\epsilon$ (Gaussian noise). This is the "Irreducible Error." No matter how perfect your AI is, it can never predict the noise. It is mathematically impossible.
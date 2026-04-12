# AI/ML Concept: Gradient Descent

This concept is the core intelligence of every neural network in existence, from the simplest regressor to Large Language Models. It is called **Gradient Descent**.


Imagine dropping a marble into a smooth, curved bowl (your Loss Landscape). Gravity automatically pulls the marble down the steepest slope until it rests perfectly at the bottom center (where Loss = $0$). 

Gradient Descent is how we program mathematical gravity.
1. **Calculate the Gradient (Slope):** Where are we in the bowl?
2. **Take a Step:** Update our weight by moving *against* the slope. 
3. **The Learning Rate ($\alpha$):** We don't want to jump too far and fly out the other side of the bowl! We multiply our step by a tiny fraction (like $0.1$) to slowly roll down to the bottom.

The weight update formula is the single most important equation in AI training:
$$w_{new} = w_{old} - (\text{learning\_rate} \times \text{gradient})$$
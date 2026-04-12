# Math: The Derivative

To stop guessing random numbers, we need to know exactly how changing a weight will affect our error. In calculus, we measure this using a **derivative**. 

A derivative is simply the exact slope of a curve at one specific point. 


Let's imagine the simplest possible error function. Your Loss ($L$) is just your Weight ($w$) squared: 
$$L = w^2$$

If $w = 4$, your loss is $16$. If we want to reduce the loss, should we increase $w$ or decrease $w$? 
By taking the derivative of $w^2$ (using the basic power rule of calculus, where you multiply the coefficient by the exponent and subtract one from the exponent), we get the slope equation:
$$\frac{dL}{dw} = 2w$$

If we plug our weight ($w=4$) into our derivative equation ($2 \cdot 4$), the slope is $8$. Because the slope is positive, it tells us the curve is currently going *up*. To get to the bottom of the curve ($0$), we must go in the opposite direction. We need to decrease $w$.
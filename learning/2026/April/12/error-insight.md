# 💡 Developer's Insight: The Geometry of the Minus Sign

While implementing the gradient descent loop, I wanted to build a visual intuition for *why* the mathematical formula works without needing conditional logic. 

I reached this intuition by approximating a curve using nearby points and shrinking the gap to one point. The tangent line gives the exact direction at that point. 

Moving left→right on a tangent line for a parabola ($x^2$):
* At $x = -1$, the slope is negative (downhill).
* At $x = 1$, the slope is positive (uphill).

If the tangent line goes down left→right, the change is negative. To find the bottom of the curve (the minimum loss), we must move in the opposite direction. 

This beautifully explains the minus sign in the core Gradient Descent formula:
$$w = w - (\text{learning\_rate} \times \text{gradient})$$

If the gradient is negative, subtracting a negative becomes an addition, pushing the weight to the right (towards $0$). If the gradient is positive, subtracting a positive pushes the weight to the left (towards $0$). The minus sign acts as a natural, self-correcting directional switch, allowing the loop to find the minimum without any `if/else` checks.
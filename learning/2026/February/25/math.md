# Math: The Equation of a Line

In algebra, the fundamental equation for a straight line is $y = mx + b$.
* $x$ is the input variable.
* $m$ is the slope, which dictates how steep the line is.
* $b$ is the y-intercept, which is the value of $y$ when $x$ is exactly $0$.


When we move from 2D algebra to multi-dimensional data, the math remains exactly the same, but we expand the notation. Instead of one slope $m$ and one input $x$, we have a vector of weights $\vec{w}$ and a vector of features $\vec{x}$. We combine them using the dot product and add our intercept $b$:
$$y = (\vec{w} \cdot \vec{x}) + b$$
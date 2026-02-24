# Math: Euclidean Distance

To understand how far apart two points are in space, we use Euclidean distance. This is the exact straight-line distance between two points, acting as an $n$-dimensional extension of the Pythagorean theorem ($a^2 + b^2 = c^2$).

For a 2D space, the distance $d$ between points $(x_1, y_1)$ and $(x_2, y_2)$ is:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

In machine learning, we rarely work in just 2 dimensions. The beauty of the math is that it scales perfectly to high-dimensional spaces. To find the distance between any two vectors $\vec{x}$ and $\vec{y}$, we subtract their corresponding elements, square the differences (to remove negative values), sum them up, and take the square root:
$$d = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$$
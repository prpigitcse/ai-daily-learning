# Math: Matrix-Vector Multiplication

How do we multiply a 2D matrix by a 1D vector? We essentially perform the dot product from Week 1 over and over again. We take the dot product of the *first row* of the matrix with the vector, then the *second row* with the vector, and so on.


Because we are pairing up elements to multiply them, there is one unbreakable mathematical rule for this operation: **The number of columns in the matrix must exactly equal the number of elements in the vector.** If matrix $X$ has a shape of $(3, 2)$ (3 rows, 2 columns), the vector $\vec{v}$ *must* have a length of $2$. The result of this multiplication is a brand new vector with a length of $3$ (one result for each row). 

Mathematically, we write this as:
$$\vec{y} = X\vec{v}$$
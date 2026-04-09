# Math: The Matrix Transpose

Sometimes, the matrices we want to multiply don't have matching inner dimensions. To fix this, we use an operation called **Transposition**. 

Transposing a matrix simply means flipping it over its diagonal. The rows become columns, and the columns become rows. 


We denote a transposed matrix with a capital "T" superscript ($A^T$).
If matrix $A$ has a shape of $(3, 2)$:
$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$$

Then $A^T$ will have a shape of $(2, 3)$:
$$A^T = \begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \end{bmatrix}$$
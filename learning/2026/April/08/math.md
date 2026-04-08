# Math: Multiplying Matrices

If multiplying a matrix by a vector is just a series of dot products, multiplying a matrix by another matrix is simply taking that process into two dimensions. 

To find the value for the first row and first column of your new matrix, you take the dot product of the **1st Row of Matrix A** and the **1st Column of Matrix B**. 


Because we are pairing rows with columns, the golden rule of matrix multiplication is: **The inner dimensions must match.**
* Matrix $A$ has shape $(m, n)$.
* Matrix $B$ has shape $(n, p)$.
* You can only multiply them if $n = n$. The resulting Matrix $C$ will have the shape of the outer dimensions: $(m, p)$.

Mathematically, the element in row $i$ and column $j$ of the new matrix is calculated as:
$$C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}$$
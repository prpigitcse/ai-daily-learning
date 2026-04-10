# Math: Linear Dependence

In linear algebra, two vectors are considered **linearly dependent** if one is simply a scaled version of the other.

For example, if $\vec{v}_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ and $\vec{v}_2 = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$, they point in the exact same direction in space; $\vec{v}_2$ is just twice as long. Mathematically, $\vec{v}_2 = 2 \cdot \vec{v}_1$.

Because they point in the exact same direction, the second vector provides absolutely zero _new_ geometric information. If a matrix contains columns that are linearly dependent, the matrix contains redundant mathematical information.

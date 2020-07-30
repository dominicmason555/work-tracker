Matrices
========

$$
\begin{bmatrix}
I_1 \\
I_2 \\
I_3
\end{bmatrix}
=
\begin{bmatrix} 
Y_1 & Y_4 & Y_7 \\
Y_2 & Y_5 & Y_8 \\ 
Y_3 & Y_6 & Y_9 
\end{bmatrix}

\begin{bmatrix}
V_1 \\
V_2 \\
V_3
\end{bmatrix}
$$

Generic current, voltage and admission model of a circuit for nodal analysis.

# Lecture 1

Symmetrical matrices mean lossless cycle, no energy loss in circuit for example.

Matrices can represent simultaneous equations.

Single column matrices are called column matrices or vectors.

Identity matrix multiplied by any matrix is that matrix, equivalent of 1.

Identity matrix of size 3: $\begin{bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix}$

Transpose of matrix is flip it across the diagonal, so a 3x1 becomes a 1x3.

Transpose matrix product: reverse the order and transpose each $(ABC)^T = C^T \ B^T \ A^T$

Norm of vector (or column) is itself multiplied by its transform $||V||^2_2 = V^T V$ 

Norm is like "squaring" the vector, or finding its magnitude or RMS.

Permutation matrix is like identity but with 1s in wrong places, multiply to swap inputs and outputs without changing them, re-orders elements of the matrix, also $||input||^2_2 = ||output||^2_2$

Permutation matrix looks like: $\begin{bmatrix}1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{bmatrix}$

To scale a certain row, can change value in identity/permuation matrix: $\begin{bmatrix}1 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 1\end{bmatrix}$

Matrix multiplication $AB = C$: each element $C_{i,\ j}$ is the sum of the $i$th row of $A$ multiplied by the $j$th row of $B$. Number of columns of $A$ must be equal to the number of rows of $B$. Because of this, $AB \ne BA$.

Two linear time invariant systems, each represented by matrices, that are cascaded together can be represented by one system with a matrix that is the product of the two matrices.

Scalar product is like amplifying with a gain, multiply each element of the matrix by the scalar.

Matrix addition and subtraction are just element-wise add and subtract, matrices must be the same size.

Can't divide matrices, can only multiply by their inverse and even then the inverse might not exist.

# Lecture 2

Matrix multiplication is easy, matrix solving is hard - may be 0 or many solutions.

Diagonal matrices only have non-0 numbers on the diagonal top left to bottom right, look like identity matrices but can have numbers other than one. Easy to solve unless theres a 0 on the diagonal.

Bidiagonal matrices have a bonus diagonal either directly above or directly below the main diagonal like: $\begin{bmatrix}1 & 2 & 0 \\ 0 & 2 & 3 \\ 0 & 0 & 3\end{bmatrix}$

Triangular matrices have all (inclusive) above or all below diagonal like: $\begin{bmatrix}1 & 2 & 3\\ 0 & 2 & 3 \\ 0 & 0 & 3\end{bmatrix}$

Diagonal, bidiagonal and triangular are easy to solve, because one row will always have only one non-0 element, so that can be trivially solved to remove an unknown, the next row will have two unknows etc. You can manipulate some matrices to become one of these using a permutation matrix to swap its rows, so that its easy to solve if its now one of the "nice" matrices. Can multiply both sides of the equation by anything you want to make it easier to solve and still get the correct result, even multiplying bits by 0 to get rid of them to make it nice.

You can pick a matrix that will be 0 at certain terms using trigonometry, using $\begin{bmatrix}\cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$ and then choosing theta using inverse tan. Called a Given's roatation.

The $\sin \theta$ and $\cos \theta$ terms can be placed in columns and rows $i$ and $k$ to affect rows $i$ and $k$ of the rotated matrix.

To make a triangular matrix, delete elements with roatations in this order: $\begin{bmatrix}0 & 0 & 0 \\ 2 & 0 & 0 \\ 1 & 3 & 0\end{bmatrix}$

Can't do too many calculations because time contraints and each calculation adds some rounding error.

Multiplying a column by a row (i.e. finding the norm) is $O(N)$, multiplying 2D by column is $O(N^2)$, multiplying 2D by 2D is $O(N^3)$

Inverse of matrix $A$ is $A^{-1}$ such that $A A^{-1} = I$. An orthogoal matrix is whose transpose is its inverse, $Q Q^T = ||Q||^2_2 = I$. Given's rotation matrices are orthogonal, as are any sequence of multiplications of them.

More unknowns that equations, i.e. a matrix wider than it is tall means its underspecified, there may be multiple solutions. More equations than unknown i.e. a matrix that is taller than it is wide is overspecified, can be no solutions. These are called rectangular, whereas a square matrix where the width and the height are the same are nice and solvable.

QR Decomposition is where any matrix can be decomposed into the product of an orthagonal matrix Q and an upper triangular matrix R. This can be done using a sequence of Given's rotations. Can be used to solve $Ax = b$ as follows:

| Step | Expression        | Explanation                                  |
|:----:|:-----------------:|:--------------------------------------------:|
| 1    | $Ax = b$          | Standard matrix solve                        |
| 2    | $A = QR$          | $A$ can be decomposed                        |
| 3    | $Q^T Ax = Q^T b$  | Can multiply both sides by $Q^T$             |
| 4    | $Q^T QRx = Q^T b$ | Substitute step 2, note $Q^T Q = I$          |
| 5    | $Rx = Q^T b$      | $I$ is like 1, so A replaced with triangular |

Now the equation $Rx = Q^T b$ is easy to solve as $A$ has been replaced with a triangular matrix, and $Q^T b$ is a simple multiplication.

Another way to perform the QR decomposition is using Householder Reflections. A householder matrix is an orthagonal matrix you can multiply a matrix by to zero out all the sub-diagonal terms in a column. You can multiply a matrix that is say 10 columns wide by 10 householder matrices to zero out each column below the diagonal. Once this is done, ss products of orthagonal matrices are also orthagonal,  the product of the Householder matrices is orthagonal (Q) and the resulting matrix is triangular (R). Householder reflections are very efficient.

Triangular matrices don't have to be square. QR decomposition still works on non-square matrices but you can only get the "most optimal" solution like a constraint solver, no correct answer.

For a QR decomposition of a triangular matrix, if the diagonals are 0 that means it will fail with divide by 0, having numbers close to 0 means the problem is "unstable". This way, a QR decomposition can be used to determine if there are enough equations for a unique solution, as each on the diagonal means one less independent equation to solve. So even if it is an N by N matrix it might not have N real equations to solve, the "effective" size of the matrix is its **Rank**.

All matrices can be expressed in cannonical forms $A = QR$ (orthogonal and upper triangular) and $A = LU$ (lower triangular and upper triangular). QR generally better but LU is easy given matrices that fit it well, uncommon though.

# Lecture 3

A vector input to a matrix will usually give a different "shaped" output, but certain inputs can give you an amplification (or attenuation) of the input instead, sort of like resonance. For a general input its the matrix multiplication, but for the one special input its just a scalar multiplication by an amplification factor. Finding if a matrix has this special frequency can determine if it is prone to feedback, like if a system is prone to positive feedback and instability.

The special case is where $Ax = kx$ instead of $Ax = Mx$, the solutions to the special case are called eigensolutions, x is the eigenvector and k is the eigenvalue. With eigenvalues, multiplying and solving become trivial. A matrix equation may have zero, a finite number, or infinite eigenvectors and eigenvalues.

Eigensolutions are often resonances in systems. As with fourier, any signal (solution) can be represented by the sum (superposition) of its harmonics (eigensolutions). That is for most matrices that come up in engineering anyway. The superposition is the sum of all of the solutions multiplied by their respective coefficients.

The matrix of all the eigenvectors is (usually) orthogonal (real, symmetrical matrices). All of the eigenvalues of a matrix is called its spectrum. The inverse of a matrix can be calculated if you know all its eigensolutions. 

The determinant of a matrix is the product of its eigenvalues. If any of the eigenvalues are 0, the determinant is 0, and the system cannot be solved.

# Lecture 4

Non-square (rectangular) matrices have no unique inverse.

**The Singular Value Decomposition** (SVD) is where any matrix can be written in the form $A = Q \sigma P^T$ where $Q$ and $P$ are orthogonal matrices and $\sigma$ is a diagonal matrix. It is valid for literally **any** matrix.

It is like lossy compressions where you remove extraneous detail. Can clean up noisy data, prioritise the more and less important aspects of the data, help avoiding finite precision issues, find a best fit solution, and tell you how much control you have over a system from its inputs. Very robust against rounding errors, but it is computationally expensive.

An orthogonal matrix multiplied by its transpose is $I$, the transpose of an orthagonal matrix is its inverse. 

If $a^T b = 0$ then $a$ and $b$ are perpendicular.

The axes of an N-dimensional space (i.e. X, Y and Z) are called the **basis vectors**. You can represent any point (column vector) with different numbers depending on what the basis vectors are, you can choose them to be in any direction and they don't have to be orthogonal, we just like X, Y and Z because they're easy.

The SVD chooses basis vectors for given data to use the minimum necessary number of basis vectors, the basis vectors are perpendicular, and the biggest distance along a basis vector is stored "first", then the second biggest etc so the basis vectors are "prioritised".

The $\sigma$ diagonal matrix is the distance of the data from the origin in each axis, called the singular values. It is an "RMS" style mean value of the distance, the square root of the sum of the square distances on each axis. The top left singular value is the largest, then the second largest e.t.c. and the smallest is the bottom right.

You can remove noise by just focusing on the most important, largest basis vector. SVD can find a part of a system that you cannot conrol because one of the $\sigma$ coefficients will be 0. A coefficient being zero or near-zero shows that you don't have enough independent equations, so the matrix isn't uniquely solvable.

The perpendicular axes mean that noise/inaccuracy in one axis will not affect another axis, they are independant.

Inverse of diagonal matrix $A = \begin{bmatrix}A_1 & 0 & 0 \\ 0 & A_2 & 0 \\ 0 & 0 & A_3\end{bmatrix}$ is $A^{-1} = \begin{bmatrix}1/A_1 & 0 & 0 \\ 0 & 1/A_2 & 0 \\ 0 & 0 & 1/A_3\end{bmatrix}$ which is easy.

SVD can be used to solve an equation $Ax = b$ where the SVD of $A$ is known to be $A = Q \sigma P^T$ as follows:

| Step | Expression                                     | Explanation                                  |
|:----:|:----------------------------------------------:|:--------------------------------------------:|
| 1    | $Ax = b$                                       | Standard matrix solve                        |
| 2    | $A = Q \sigma P^T$                             | $A$ can be decomposed                        |
| 3    | $Q^T Ax = Q^T b$                               | Can multiply both sides by $Q^T$             |
| 4    | $Q^T Q \sigma P^T x = Q^T b$                   | Substitute step 2, note $Q^T Q = I$          |
| 5    | $\sigma P^T x = Q^T b$                         | $I$ is like 1, so A replaced with triangular |
| 6    | $\sigma^{-1} \sigma P^T x = \sigma^{-1} Q^T b$ | Do the same with $\sigma \sigma^{-1} = I$    |
| 7    | $P^T x = \sigma^{-1} Q^T b$                    | Moved sigma to other side                    |
| 8    | $P P^T x = P^T \sigma^{-1} Q^T b$              | Again with $PP^T = I$                        |
| 9    | $x = P \sigma^{-1} Q^T b$                      | Finally just multiply RHS                    |

# Lecture 5

Engineering matrices have a lot of zeroes, e.g. in a circuit there are only non-zero values where nodes are connected, i.e. nearest neighbours. A matrix with few zeroes is dense, a matrix with many zeroes is sparse. Sparse matrices stored normally don't speed up computations.

Storing sparse matrices is a waste because storing all the zeroes takes up useless space, can use Compressed Sparse Row (CSR) storage or other compressions. These compressed forms have their own algorithms which do give the speedup as well as saving memory. Not all the normal techniques work well with sparse matrices.

A way of solving matrices is to use an iterative approach like newtons method where you start with a random matrix and then improve the guess. Can find the error of solving $Ax = b$ with residual error $r = b - A \widetilde{x}$ where $\widetilde{x}$ is the guess at the true $x$. Can minimise $r$ on a gradient descent to find $x$. Need to change $\widetilde{x}$ to decrease $r$ from the previous guess, on the graph of $r$ against $\widetilde{x}$ it would go downhill. Keep changing it in different directions to keep it efficient. The algorithm works with just multiplies so it's very efficient.

If the matrix is symmetric and "positive definite" meaning theres no energy source inside the system, then the convergence to $\widetilde{x} \rightarrow x$ is guaranteed to work and reach $x$ and solve the matrix, this is called the **steepest descent algorithm**. There is also one for asymemetric matrices called the **minimal residual algorithm**, but it is less efficient. 

These are called **Conjugate Gradient** methods, to keep them efficient they never step in the same direction twice. For an $N \times N$ matrix it would converge in $N$ steps if you had infinite decimal precision, but you don't. They are most efficient on mostly diagonal - **diagonally dominant** matrices, i.e. the non-diagonal terms might not be zero but they are really small. 

If you multiply a matrix by a close estimate of its inverse you'll get a mostly diagonal matrix.

Can be used to find the dominant eigenvector using the power methods.

If you iterate more than around 100 iterations without solving it probably won't ever solve and you should pre-condition it better.

In systems like circuits and wave propogation etc when elements are only connected to their nearest neighbour it is possible to split the system into chunks of neighbours and leave the dividing lines where the chunks are neighbours to be calculated last after the chunks have finished. no.

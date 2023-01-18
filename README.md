# Homography-Python-Nonlinear-Optimization
Example of homography estimation: linear solution + nonlinear optimization refinement. 


$$
				 \begin{align}  \begin{bmatrix}      u \\      v    \end{bmatrix}  &=  T^{-1}  \begin{bmatrix}      x \\      y    \end{bmatrix}.   \label{eq_xy2uv}  \end{align}
$$



$$

x \begin{align}{\bf p}_{uv} &=\begin{bmatrix}    \frac{4}{5} & -\frac{3}{5} \\    \frac{3}{5} & \frac{4}{5}  \end{bmatrix}^{-1}{\bf p}_{xy} \notag \\ &= \begin{bmatrix}    \frac{4}{5} & \frac{3}{5} \\    -\frac{3}{5} & \frac{4}{5}  \end{bmatrix}\begin{bmatrix}    4  \\    3   \end{bmatrix}  \notag \\ &=   \begin{bmatrix}    5  \\    0   \end{bmatrix}.  \end{align}
$$

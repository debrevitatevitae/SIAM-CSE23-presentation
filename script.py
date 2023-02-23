import matplotlib.pyplot as plt
import numpy as np

def linearly_separable(n):
    X = np.random.uniform(0, 5, size=(n ,2))
    ground_truth = lambda x1, x2: 4 - x1 - x2
    delta = 0.1
    y = np.array(
        [-1 if ground_truth(*x) < -delta else 1 for x in X]
        )
    return X, y


if __name__ == '__main__':
    np.random.seed(0)
    X, y = linearly_separable(n=100)
    colors = ['r' if yy==-1 else 'b' for yy in y]
    plt.scatter(X[:, 0], X[:, 1], c=colors, marker='o')

    ground_truth = lambda x1: 4 - x1
    x1_grid = np.linspace(0, 5, 100)
    x2_ = ground_truth(x1_grid)
    plt.plot(x1_grid, x2_, 'k-')
    
    w = np.array([1, 1])  # normal to hyperplane
    xw1 = np.array([2., ground_truth(2.)])
    # xw2 = xw1 + .3 * w
    plt.arrow(xw1[0], xw1[1], .3*w[0], .3*w[1], width=0.01, lw=2., color='k')
    plt.show()
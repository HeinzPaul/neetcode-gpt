import numpy as np
from numpy.typing import NDArray
import math


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        x = []
        store = 0
        for i in z:
            x.append(math.exp(i-max(z)))
        store = sum(x)
        for i in range(len(x)):
            x[i] = x[i]/store
        return np.round(x,4)


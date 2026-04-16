import numpy as np
import math
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        x = []
        for i in z:
            x.append(round(1/(1+(math.exp(-i))),5)) 
        return x
        

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        x = []
        for i in z:
            x.append(float(max(0,i)))
        return x
        

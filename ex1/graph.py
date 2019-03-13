import numpy as np
import matplotlib.pyplot as plt


# results from serial version of matrix multiplication with size of matrices: 10, 100, 1000, 10000, 20000, 30000, 40000, 50000, ...
serial_version = [0.004, 0.055, 10.185, 720.354, 1284.211]

# results from pthread version of matrix multiplication with 4 threads and size of matrices: 10, 100, 1000, 10000, 20000, 30000, 40000, 50000, ...
pthread_version = [0.115, 0.088, 2.821, 169.455, 495.213]

matrix_sizes = ('10', '100', '1000', '10000', '20000')
x_pos = np.arange(len(serial_version))

plt.plot(serial_version, label='Serial Version')
plt.plot(pthread_version, label='Pthread Version with 4 Threads')

plt.xlabel('Matrix sizes (N)')
plt.xticks(x_pos, matrix_sizes)
plt.ylabel('Execution time (s)')
plt.title('Matrix Multiplication in Parallel Computing')
plt.grid(True)
plt.legend()

plt.show()

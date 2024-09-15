import numpy as np
import tkinter as tk
from tkinter import messagebox

def isSquareMatrix(matrix):
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            return False
    return True    

def firstNotZeroElement(matrix,p):
    for i in range(p,len(matrix)):
        if matrix[i][p]!= 0 :
            return i
    return -1    

def gauss(matrix,b):
    if  not isSquareMatrix(matrix) or len(matrix) != len(b):
        raise ValueError("Matrix must be square and the size of b must match the number of rows in the matrix.")
    if np.linalg.det(matrix)==0:
        raise ValueError("Determanate is 0;There is 0 or a lot of solution ")

    n = len(matrix)  
    for p in range(n):
        if matrix[p][p] == 0:
            k= firstNotZeroElement(matrix,p)
            if k != -1:
               matrix[p],matrix[k] = matrix[k],matrix[p]
               b[p],b[k] = b[i],b[k]
            else:
                break

        for i in range(p+1,n):
            factor = matrix[i][p] / matrix[p][p]
            b[i] -= factor * b[p] 
            for j in range(p,n):
                matrix[i][j] -=factor * matrix[p][j]

    result=[0] * n
    for i in reversed(range(0,n)):
        sumx = sum(matrix[i][j] * result[j] for j in range(i + 1, n))
        x = (b[i] - sumx)/matrix[i][i]
        result[i] = x
    return result

def solve():
    try:
        # Convert inputs to numpy arrays
        matrix = np.array(eval(entry_matrix.get()),dtype= float)
        b = np.array(eval(entry_vector.get()),dtype= float)
                
        result = gauss(matrix, b)

        result_label.config(text="\n".join([f"x{i} = {val}" for i, val in enumerate(result)]))
    
    except Exception as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Gaussian Elimination Solver")

# Labels
label_matrix = tk.Label(root, text="Enter coefficient matrix (e.g. [[1,1,3], [0,1,3], [-1,3,0]]):")
label_matrix.pack()

entry_matrix = tk.Entry(root, width=50)
entry_matrix.pack()

label_vector = tk.Label(root, text="Enter constant vector (e.g. [1, 3, 5]):")
label_vector.pack()

entry_vector = tk.Entry(root, width=50)
entry_vector.pack()

# Solve button
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter loop
root.mainloop()

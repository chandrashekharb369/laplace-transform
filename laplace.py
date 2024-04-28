import tkinter as tk
from sympy import symbols, laplace_transform, simplify, lambdify
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


t, s,a = symbols('t s a')


window = tk.Tk()


label1 = tk.Label(window, text="Enter your function:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

canvas = None
label2 = None

def compute_laplace():
    global canvas, label2

    
    if canvas is not None:
        canvas.get_tk_widget().destroy()
    if label2 is not None:
        label2.destroy()

   
    f = parse_expr(entry1.get())

   
    F = laplace_transform(f, t, s)

   
    F_simplified = simplify(F[0])

    
    F_str = str(F_simplified).replace('**', '^')

   
    label2 = tk.Label(window, text="The Laplace transform is: " + F_str)
    label2.pack()

    
    F_lambdified = lambdify(s, F_simplified, "numpy")
    s_values = np.linspace(0, 10, 400)
    F_values = F_lambdified(s_values)

    
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

   
    if isinstance(F_values, np.ndarray) and issubclass(F_values.dtype.type, np.floating):
        ax.plot(s_values, F_values)
        ax.set_title('Laplace Transform')
        ax.set_xlabel('s')
        ax.set_ylabel('F(s)')
        ax.grid(True)
    else:
        print("F_values is not a numpy array of floats.")

   
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

button1 = tk.Button(window, text="Compute and Plot Laplace Transform", command=compute_laplace)
button1.pack()


window.mainloop()

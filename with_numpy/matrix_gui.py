"""
3x3 MATRIX OPERATIONS - WITH NUMPY
GUI: Tkinter
Run: python matrix_gui.py
Install dependency first: pip install numpy

This version uses NumPy functions for matrix calculations.
"""

import tkinter as tk
from tkinter import ttk, messagebox

import numpy as np


SIZE = 3


def read_matrix(entries):
    """Read the nine Entry values and convert them into a NumPy 3x3 array."""
    values = []
    for row in entries:
        values_row = []
        for entry in row:
            value = entry.get().strip()
            if not value:
                raise ValueError("Please fill in all nine matrix cells.")
            values_row.append(float(value))
        values.append(values_row)
    return np.array(values, dtype=float)


class MatrixApp:
    """Create and control the Tkinter matrix calculator window."""

    def __init__(self, root):
        self.root = root
        self.root.title("3x3 Matrix Operations - With NumPy")
        self.root.geometry("850x650")
        self.root.minsize(760, 600)

        ttk.Label(root, text="3x3 Matrix Operations", font=("Arial", 20, "bold")).pack(pady=(12, 2))
        ttk.Label(root, text="NumPy version").pack(pady=(0, 12))

        matrices_frame = ttk.Frame(root, padding=10)
        matrices_frame.pack()
        self.entries_a = self.create_matrix_input(matrices_frame, "Matrix A", 0)
        self.entries_b = self.create_matrix_input(matrices_frame, "Matrix B", 1)

        operations = ttk.LabelFrame(root, text="Choose an operation", padding=10)
        operations.pack(fill="x", padx=20, pady=10)

        buttons = [
            ("A + B", self.add), ("A - B", self.subtract),
            ("A × B", self.multiply), ("Transpose A", self.transpose),
            ("Determinant A", self.show_determinant), ("Inverse A", self.inverse),
        ]
        for index, (label, command) in enumerate(buttons):
            ttk.Button(operations, text=label, command=command).grid(
                row=index // 3, column=index % 3, padx=7, pady=6, sticky="ew"
            )
        for column in range(3):
            operations.columnconfigure(column, weight=1)

        result_frame = ttk.LabelFrame(root, text="Result", padding=10)
        result_frame.pack(fill="both", expand=True, padx=20, pady=(0, 15))
        self.result = tk.Text(result_frame, height=8, font=("Consolas", 12), wrap="none")
        self.result.pack(fill="both", expand=True)
        self.result.insert("1.0", "Enter values in Matrix A and Matrix B, then choose an operation.")
        self.result.config(state="disabled")
        ttk.Button(root, text="Clear all", command=self.clear_all).pack(pady=(0, 12))

    def create_matrix_input(self, parent, title, column):
        """Create a labeled 3x3 grid of input boxes."""
        frame = ttk.LabelFrame(parent, text=title, padding=10)
        frame.grid(row=0, column=column, padx=12, sticky="n")
        entries = []
        for i in range(SIZE):
            row_entries = []
            for j in range(SIZE):
                entry = ttk.Entry(frame, width=9, justify="center")
                entry.grid(row=i, column=j, padx=4, pady=4, ipady=5)
                entry.insert(0, "1" if i == j else "0")
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def get_a(self):
        return read_matrix(self.entries_a)

    def get_b(self):
        return read_matrix(self.entries_b)

    def display_result(self, value, heading="Result"):
        """Display a NumPy matrix or a single numeric result."""
        self.result.config(state="normal")
        self.result.delete("1.0", tk.END)
        self.result.insert(tk.END, heading + "\n\n")
        if isinstance(value, np.ndarray):
            for row in value:
                self.result.insert(tk.END, "   ".join(f"{number:10.4f}" for number in row) + "\n")
        else:
            self.result.insert(tk.END, f"{float(value):.6g}\n")
        self.result.config(state="disabled")

    def run_operation(self, operation, heading):
        """Read input, calculate, and display errors without closing the app."""
        try:
            a = self.get_a()
            result = operation(a)
            self.display_result(result, heading)
        except ValueError as error:
            messagebox.showerror("Input Error", str(error))
        except np.linalg.LinAlgError:
            messagebox.showerror("Calculation Error", "This matrix is singular and has no inverse.")
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def run_two_matrix_operation(self, operation, heading):
        """Read both matrices and apply an operation that needs A and B."""
        try:
            a = self.get_a()
            b = self.get_b()
            self.display_result(operation(a, b), heading)
        except ValueError as error:
            messagebox.showerror("Input Error", str(error))
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def add(self):
        self.run_two_matrix_operation(np.add, "A + B")

    def subtract(self):
        self.run_two_matrix_operation(np.subtract, "A - B")

    def multiply(self):
        # np.matmul performs standard matrix multiplication 
        # (not element-wise multiplication).
        self.run_two_matrix_operation(
            np.matmul, "A × B")

    def transpose(self):
        self.run_operation(
            np.transpose, "Transpose of A"
            )

    def show_determinant(self):
        self.run_operation(
            np.linalg.det, "Determinant of A"
            )

    def inverse(self):
        self.run_operation(
            np.linalg.inv, "Inverse of A")

    def clear_all(self):
        """Empty both input matrices and reset the result area."""
        for matrix_entries in (self.entries_a, self.entries_b):
            for row in matrix_entries:
                for entry in row:
                    entry.delete(0, tk.END)
        self.result.config(state="normal")
        self.result.delete("1.0", tk.END)
        self.result.insert("1.0", "All fields cleared.")
        self.result.config(state="disabled")


if __name__ == "__main__":
    window = tk.Tk()
    MatrixApp(window)
    window.mainloop()

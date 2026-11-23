
"""
3x3 MATRIX OPERATIONS - WITHOUT NUMPY
GUI: Tkinter

Operations:
1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Determinant
6. Inverse
"""

import tkinter as tk
from tkinter import ttk, messagebox

# Matrix size
SIZE = 3


# ==========================================
# 1. READ MATRIX VALUES
# Get values from the Tkinter input boxes and convert them into a Python matrix.
# ==========================================

def read_matrix(entries):

    matrix = []

    for row in entries:

        matrix_row = []

        for entry in row:

            value = entry.get().strip()

            if value == "":
                raise ValueError("Please fill all matrix cells.")

            try:
                number = float(value)
            except ValueError:
                raise ValueError("Please enter numbers only.")

            matrix_row.append(number)

        matrix.append(matrix_row)

    return matrix


# ==========================================
# 2. MATRIX ADDITION
# ==========================================

def add_matrices(a, b):

    result = []

    for i in range(SIZE):

        row = []

        for j in range(SIZE):

            row.append(a[i][j] + b[i][j])

        result.append(row)

    return result


# ==========================================
# 3. MATRIX SUBTRACTION
# ==========================================

def subtract_matrices(a, b):

    result = []

    for i in range(SIZE):

        row = []

        for j in range(SIZE):

            row.append(a[i][j] - b[i][j])

        result.append(row)

    return result


# ==========================================
# 4. MATRIX MULTIPLICATION
# ==========================================

def multiply_matrices(a, b):

    result = []

    for i in range(SIZE):

        row = []

        for j in range(SIZE):

            total = 0

            for k in range(SIZE):

                total = total + a[i][k] * b[k][j]

            row.append(total)

        result.append(row)

    return result


# ==========================================
# 5. MATRIX TRANSPOSE
# ==========================================

def transpose_matrix(a):

    result = []

    for i in range(SIZE):

        row = []

        for j in range(SIZE):

            row.append(a[j][i])

        result.append(row)

    return result


# ==========================================
# 6. DETERMINANT
# ==========================================

def determinant(a):

    det = (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )

    return det


# ==========================================
# 7. MATRIX INVERSE
# ==========================================

def inverse_matrix(a):

    det = determinant(a)

    if abs(det) < 0.0000000001:
        raise ValueError("Inverse does not exist. Determinant is zero.")

    cofactors = []

    for i in range(SIZE):

        row = []

        for j in range(SIZE):

            minor = []

            for r in range(SIZE):

                if r != i:

                    minor_row = []

                    for c in range(SIZE):

                        if c != j:
                            minor_row.append(a[r][c])

                    minor.append(minor_row)

            minor_det = (
                minor[0][0] * minor[1][1]
                - minor[0][1] * minor[1][0]
            )

            cofactor = ((-1) ** (i + j)) * minor_det

            row.append(cofactor)

        cofactors.append(row)

    adjugate = transpose_matrix(cofactors)

    inverse = []

    for i in range(SIZE):

        row = []

        for j in range(SIZE):

            row.append(adjugate[i][j] / det)

        inverse.append(row)

    return inverse


# ==========================================
# 8. GUI APPLICATION
# ==========================================

class MatrixApp:

    def __init__(self, root):

        self.root = root

        self.root.title("3x3 Matrix Operations - Without NumPy")
        self.root.geometry("850x650")

        # Main heading
        ttk.Label(
            root,
            text="3x3 Matrix Operations",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        ttk.Label(
            root,
            text="Pure Python Version (Without NumPy)"
        ).pack()

        # Matrix input section
        matrices_frame = ttk.Frame(root, padding=10)
        matrices_frame.pack()

        self.entries_a = self.create_matrix_input(
            matrices_frame, "Matrix A", 0
        )

        self.entries_b = self.create_matrix_input(
            matrices_frame, "Matrix B", 1
        )

        # Operation buttons
        operations = ttk.LabelFrame(
            root,
            text="Choose an Operation",
            padding=10
        )

        operations.pack(fill="x", padx=20, pady=10)

        buttons = [
            ("A + B", self.add),
            ("A - B", self.subtract),
            ("A x B", self.multiply),
            ("Transpose A", self.transpose),
            ("Determinant A", self.show_determinant),
            ("Inverse A", self.inverse)
        ]

        for index, (label, command) in enumerate(buttons):

            ttk.Button(
                operations,
                text=label,
                command=command
            ).grid(
                row=index // 3,
                column=index % 3,
                padx=7,
                pady=6,
                sticky="ew"
            )

        # Result section
        result_frame = ttk.LabelFrame(
            root,
            text="Result",
            padding=10
        )

        result_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.result = tk.Text(
            result_frame,
            height=8,
            font=("Consolas", 12)
        )

        self.result.pack(fill="both", expand=True)

        self.result.insert(
            "1.0",
            "Enter matrix values and select an operation."
        )

        self.result.config(state="disabled")

        # Clear button
        ttk.Button(
            root,
            text="Clear All",
            command=self.clear_all
        ).pack(pady=10)


    # ======================================
    # CREATE MATRIX INPUT BOXES
    # ======================================

    def create_matrix_input(self, parent, title, column):

        frame = ttk.LabelFrame(
            parent,
            text=title,
            padding=10
        )

        frame.grid(row=0, column=column, padx=12)

        entries = []

        for i in range(SIZE):

            row_entries = []

            for j in range(SIZE):

                entry = ttk.Entry(
                    frame,
                    width=9,
                    justify="center"
                )

                entry.grid(row=i, column=j, padx=4, pady=4)

                # Default identity matrix
                if i == j:
                    entry.insert(0, "1")
                else:
                    entry.insert(0, "0")

                row_entries.append(entry)

            entries.append(row_entries)

        return entries


    # ======================================
    # GET MATRIX VALUES
    # ======================================

    def get_a(self):
        return read_matrix(self.entries_a)

    def get_b(self):
        return read_matrix(self.entries_b)


    # ======================================
    # DISPLAY RESULT
    # ======================================

    def display_result(self, value, heading):

        self.result.config(state="normal")

        self.result.delete("1.0", tk.END)

        self.result.insert(tk.END, heading + "\n\n")

        if isinstance(value, list):

            for row in value:

                for number in row:

                    self.result.insert(
                        tk.END,
                        f"{number:10.4f} "
                    )

                self.result.insert(tk.END, "\n")

        else:

            self.result.insert(
                tk.END,
                str(round(value, 6))
            )

        self.result.config(state="disabled")


    # ======================================
    # HANDLE TWO MATRIX OPERATIONS
    # ======================================

    def run_two_matrix_operation(self, operation, heading):

        try:

            a = self.get_a()
            b = self.get_b()

            result = operation(a, b)

            self.display_result(result, heading)

        except ValueError as error:

            messagebox.showerror("Error", str(error))


    # ======================================
    # HANDLE ONE MATRIX OPERATIONS
    # ======================================

    def run_one_matrix_operation(self, operation, heading):

        try:

            a = self.get_a()

            result = operation(a)

            self.display_result(result, heading)

        except ValueError as error:

            messagebox.showerror("Error", str(error))


    # ======================================
    # OPERATION BUTTON FUNCTIONS
    # ======================================

    def add(self):
        self.run_two_matrix_operation(
            add_matrices, "A + B"
        )

    def subtract(self):
        self.run_two_matrix_operation(
            subtract_matrices, "A - B"
        )

    def multiply(self):
        self.run_two_matrix_operation(
            multiply_matrices, "A x B"
        )

    def transpose(self):
        self.run_one_matrix_operation(
            transpose_matrix, "Transpose of A"
        )

    def show_determinant(self):
        self.run_one_matrix_operation(
            determinant, "Determinant of A"
        )

    def inverse(self):
        self.run_one_matrix_operation(
            inverse_matrix, "Inverse of A"
        )


    # ======================================
    # CLEAR ALL INPUTS
    # ======================================

    def clear_all(self):

        for matrix in (self.entries_a, self.entries_b):

            for row in matrix:

                for entry in row:

                    entry.delete(0, tk.END)

        self.result.config(state="normal")

        self.result.delete("1.0", tk.END)

        self.result.insert("1.0", "All fields cleared.")

        self.result.config(state="disabled")


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    window = tk.Tk()

    app = MatrixApp(window)

    window.mainloop()

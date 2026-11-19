
"""
3x3 MATRIX OPERATIONS - WITHOUT NUMPY
GUI: Tkinter
Run: python matrix_gui.py

This program performs matrix operations using
pure Python lists, loops, and mathematical formulas.

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


# Matrix size (3 rows and 3 columns)
SIZE = 3


# --------------------------------------------------
# MATRIX FUNCTIONS (WITHOUT NUMPY)
# --------------------------------------------------

def read_matrix(entries):
    """Read values from GUI input boxes and create a 3x3 matrix."""

    matrix = []

    for row in entries:
        matrix_row = []

        for entry in row:
            value = entry.get().strip()

            if not value:
                raise ValueError("Please fill in all nine matrix cells.")

            try:
                matrix_row.append(float(value))
            except ValueError:
                raise ValueError("Please enter valid numeric values.")

        matrix.append(matrix_row)

    return matrix


def add_matrices(a, b):
    """Add two matrices element by element."""

    return [
        [a[i][j] + b[i][j] for j in range(SIZE)]
        for i in range(SIZE)
    ]


def subtract_matrices(a, b):
    """Subtract matrix B from matrix A."""

    return [
        [a[i][j] - b[i][j] for j in range(SIZE)]
        for i in range(SIZE)
    ]


def multiply_matrices(a, b):
    """Multiply two matrices using row-by-column multiplication."""

    result = [[0.0 for _ in range(SIZE)] for _ in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            for k in range(SIZE):
                result[i][j] += a[i][k] * b[k][j]

    return result


def transpose_matrix(a):
    """Convert rows into columns and columns into rows."""

    return [
        [a[j][i] for j in range(SIZE)]
        for i in range(SIZE)
    ]


def determinant(a):
    """Calculate the determinant of a 3x3 matrix."""

    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def inverse_matrix(a):
    """Calculate matrix inverse using cofactors and determinant."""

    det = determinant(a)

    # An inverse does not exist when determinant is zero.
    if abs(det) < 1e-10:
        raise ValueError(
            "This matrix has no inverse because its determinant is zero."
        )

    cofactors = []

    # Calculate the cofactor matrix.
    for i in range(SIZE):
        cofactor_row = []

        for j in range(SIZE):

            # Create a 2x2 minor by removing row i and column j.
            minor = [
                [a[r][c] for c in range(SIZE) if c != j]
                for r in range(SIZE) if r != i
            ]

            # Calculate the determinant of the 2x2 minor.
            minor_det = (
                minor[0][0] * minor[1][1]
                - minor[0][1] * minor[1][0]
            )

            # Apply the positive/negative cofactor sign.
            cofactor_row.append(((-1) ** (i + j)) * minor_det)

        cofactors.append(cofactor_row)

    # Transpose the cofactor matrix to get the adjugate.
    adjugate = transpose_matrix(cofactors)

    # Divide every adjugate element by the determinant.
    inverse = [
        [adjugate[i][j] / det for j in range(SIZE)]
        for i in range(SIZE)
    ]

    return inverse


# --------------------------------------------------
# GUI APPLICATION CLASS
# --------------------------------------------------

class MatrixApp:

    def __init__(self, root):

        self.root = root

        self.root.title("3x3 Matrix Operations - Without NumPy")
        self.root.geometry("850x650")
        self.root.minsize(760, 600)

        # Main heading.
        title = ttk.Label(
            root,
            text="3x3 Matrix Operations",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=(12, 2))

        ttk.Label(
            root,
            text="Pure Python Version (Without NumPy)"
        ).pack(pady=(0, 12))

        # Frame containing both matrices.
        matrices_frame = ttk.Frame(root, padding=10)
        matrices_frame.pack()

        # Create Matrix A and Matrix B input grids.
        self.entries_a = self.create_matrix_input(
            matrices_frame, "Matrix A", 0
        )

        self.entries_b = self.create_matrix_input(
            matrices_frame, "Matrix B", 1
        )

        # Operations section.
        operations = ttk.LabelFrame(
            root,
            text="Choose an Operation",
            padding=10
        )
        operations.pack(fill="x", padx=20, pady=10)

        # Create operation buttons.
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

        # Make operation button columns expand equally.
        for column in range(3):
            operations.columnconfigure(column, weight=1)

        # Result section.
        result_frame = ttk.LabelFrame(
            root,
            text="Result",
            padding=10
        )
        result_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 15)
        )

        self.result = tk.Text(
            result_frame,
            height=8,
            font=("Consolas", 12),
            wrap="none"
        )

        self.result.pack(fill="both", expand=True)

        self.result.insert(
            "1.0",
            "Enter matrix values and choose an operation."
        )

        self.result.config(state="disabled")

        # Clear button.
        ttk.Button(
            root,
            text="Clear All",
            command=self.clear_all
        ).pack(pady=(0, 12))

    # --------------------------------------------------
    # CREATE MATRIX INPUT GRID
    # --------------------------------------------------

    def create_matrix_input(self, parent, title, column):
        """Create a 3x3 grid of input fields."""

        frame = ttk.LabelFrame(
            parent,
            text=title,
            padding=10
        )

        frame.grid(
            row=0,
            column=column,
            padx=12,
            sticky="n"
        )

        entries = []

        for i in range(SIZE):

            row_entries = []

            for j in range(SIZE):

                entry = ttk.Entry(
                    frame,
                    width=9,
                    justify="center"
                )

                entry.grid(
                    row=i,
                    column=j,
                    padx=4,
                    pady=4,
                    ipady=5
                )

                # Insert identity matrix as default example.
                entry.insert(0, "1" if i == j else "0")

                row_entries.append(entry)

            entries.append(row_entries)

        return entries

    # --------------------------------------------------
    # GET MATRIX VALUES
    # --------------------------------------------------

    def get_a(self):
        """Get Matrix A values."""

        return read_matrix(self.entries_a)

    def get_b(self):
        """Get Matrix B values."""

        return read_matrix(self.entries_b)

    # --------------------------------------------------
    # DISPLAY RESULT
    # --------------------------------------------------

    def display_result(self, value, heading="Result"):
        """Display calculated matrix or single numeric result."""

        self.result.config(state="normal")

        self.result.delete("1.0", tk.END)

        self.result.insert(tk.END, heading + "\n\n")

        if isinstance(value, list):

            for row in value:

                self.result.insert(
                    tk.END,
                    "   ".join(
                        f"{number:10.4f}" for number in row
                    ) + "\n"
                )

        else:

            self.result.insert(
                tk.END,
                f"{value:.6g}\n"
            )

        self.result.config(state="disabled")

    # --------------------------------------------------
    # COMMON OPERATION HANDLER
    # --------------------------------------------------

    def run_operation(self, operation, needs_b=False):
        """
        Execute the selected operation.

        needs_b=True means the operation requires both matrices.
        needs_b=False means only Matrix A is required.
        """

        try:

            # Read Matrix A.
            a = self.get_a()

            if needs_b:

                # Read Matrix B for two-matrix operations.
                b = self.get_b()

                result, heading = operation(a, b)

            else:

                # Perform single-matrix operation.
                result, heading = operation(a)

            # Display the result.
            self.display_result(result, heading)

        except ValueError as error:

            messagebox.showerror(
                "Input / Calculation Error",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # --------------------------------------------------
    # OPERATION BUTTON METHODS
    # --------------------------------------------------

    def add(self):
        """Perform matrix addition."""

        self.run_operation(
            lambda a, b: (add_matrices(a, b), "A + B"),
            needs_b=True
        )

    def subtract(self):
        """Perform matrix subtraction."""

        self.run_operation(
            lambda a, b: (subtract_matrices(a, b), "A - B"),
            needs_b=True
        )

    def multiply(self):
        """Perform standard matrix multiplication."""

        self.run_operation(
            lambda a, b: (multiply_matrices(a, b), "A x B"),
            needs_b=True
        )

    def transpose(self):
        """Calculate transpose of Matrix A."""

        self.run_operation(
            lambda a: (transpose_matrix(a), "Transpose of A")
        )

    def show_determinant(self):
        """Calculate determinant of Matrix A."""

        self.run_operation(
            lambda a: (determinant(a), "Determinant of A")
        )

    def inverse(self):
        """Calculate inverse of Matrix A."""

        self.run_operation(
            lambda a: (inverse_matrix(a), "Inverse of A")
        )

    # --------------------------------------------------
    # CLEAR ALL INPUTS
    # --------------------------------------------------

    def clear_all(self):
        """Clear both matrices and the result area."""

        for matrix_entries in (self.entries_a, self.entries_b):

            for row in matrix_entries:

                for entry in row:

                    entry.delete(0, tk.END)

        self.result.config(state="normal")

        self.result.delete("1.0", tk.END)

        self.result.insert(
            "1.0",
            "All fields cleared."
        )

        self.result.config(state="disabled")


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

if __name__ == "__main__":

    # Create the main Tkinter window.
    window = tk.Tk()

    # Initialize the MatrixApp class.
    app = MatrixApp(window)

    # Start the GUI event loop.
    window.mainloop()

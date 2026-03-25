# =============================================================================
# GUI CALCULATOR
# Concepts: tkinter (built-in GUI library), classes, OOP, event-driven
#           programming, widget layout (grid), lambda functions,
#           error handling with try/except
# =============================================================================
#
# tkinter is built into Python — no installation needed.
# Run this script and a window will appear.
# =============================================================================

import tkinter as tk


# Colour scheme — named constants instead of magic strings throughout the code
COLOUR_DISPLAY_BG = "#1e1e2e"
COLOUR_DISPLAY_FG = "#cdd6f4"
COLOUR_BTN_NUMBER = "#313244"
COLOUR_BTN_NUMBER_FG = "#cdd6f4"
COLOUR_BTN_OPERATOR = "#45475a"
COLOUR_BTN_OPERATOR_FG = "#89b4fa"
COLOUR_BTN_EQUALS = "#89b4fa"
COLOUR_BTN_EQUALS_FG = "#1e1e2e"
COLOUR_BTN_CLEAR = "#f38ba8"
COLOUR_BTN_CLEAR_FG = "#1e1e2e"
COLOUR_WINDOW_BG = "#1e1e2e"


class Calculator:
    """
    A simple GUI calculator built with tkinter.

    This class groups together all the data (state) and behaviour (methods)
    for the calculator — this is Object-Oriented Programming (OOP) in action.
    """

    def __init__(self, window):
        """
        __init__ is the constructor — it runs when we create a Calculator.
        `window` is the main tkinter window passed in from main().
        """
        self.window = window
        self.window.title("Calculator")
        self.window.resizable(False, False)
        self.window.configure(bg=COLOUR_WINDOW_BG)

        # These variables hold the calculator's state
        self.current_expression = ""   # What's on the display right now
        self.full_expression = ""      # The full calculation string (e.g. "12 + 5")

        self._build_display()
        self._build_buttons()
        self._bind_keyboard()

    # -----------------------------------------------------------------------
    # Building the UI
    # -----------------------------------------------------------------------

    def _build_display(self):
        """Create the text display at the top of the calculator."""
        display_frame = tk.Frame(self.window, bg=COLOUR_WINDOW_BG)
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))

        # The top label shows the full expression (e.g. "12 + 5 =")
        self.full_label = tk.Label(
            display_frame,
            text="",
            anchor=tk.E,         # Right-align the text
            bg=COLOUR_DISPLAY_BG,
            fg="#6c7086",
            font=("Arial", 14),
            padx=10,
        )
        self.full_label.pack(fill=tk.BOTH, expand=True)

        # The bottom label shows the current number being typed
        self.current_label = tk.Label(
            display_frame,
            text="0",
            anchor=tk.E,
            bg=COLOUR_DISPLAY_BG,
            fg=COLOUR_DISPLAY_FG,
            font=("Arial", 32, "bold"),
            padx=10,
            pady=5,
        )
        self.current_label.pack(fill=tk.BOTH, expand=True)

    def _build_buttons(self):
        """Create the grid of calculator buttons."""
        buttons_frame = tk.Frame(self.window, bg=COLOUR_WINDOW_BG)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Configure columns to be equal width
        for col in range(4):
            buttons_frame.columnconfigure(col, weight=1)

        # Button layout: (label, row, column, colspan, bg, fg, command)
        button_config = [
            ("AC",  0, 0, 1, COLOUR_BTN_CLEAR,    COLOUR_BTN_CLEAR_FG,    self.clear),
            ("+/-", 0, 1, 1, COLOUR_BTN_OPERATOR,  COLOUR_BTN_OPERATOR_FG, self.toggle_sign),
            ("%",   0, 2, 1, COLOUR_BTN_OPERATOR,  COLOUR_BTN_OPERATOR_FG, self.percent),
            ("÷",   0, 3, 1, COLOUR_BTN_OPERATOR,  COLOUR_BTN_OPERATOR_FG, lambda: self.append_operator("/")),

            ("7",   1, 0, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("7")),
            ("8",   1, 1, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("8")),
            ("9",   1, 2, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("9")),
            ("×",   1, 3, 1, COLOUR_BTN_OPERATOR,  COLOUR_BTN_OPERATOR_FG, lambda: self.append_operator("*")),

            ("4",   2, 0, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("4")),
            ("5",   2, 1, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("5")),
            ("6",   2, 2, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("6")),
            ("−",   2, 3, 1, COLOUR_BTN_OPERATOR,  COLOUR_BTN_OPERATOR_FG, lambda: self.append_operator("-")),

            ("1",   3, 0, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("1")),
            ("2",   3, 1, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("2")),
            ("3",   3, 2, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("3")),
            ("+",   3, 3, 1, COLOUR_BTN_OPERATOR,  COLOUR_BTN_OPERATOR_FG, lambda: self.append_operator("+")),

            ("0",   4, 0, 2, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   lambda: self.append_digit("0")),
            (".",   4, 2, 1, COLOUR_BTN_NUMBER,    COLOUR_BTN_NUMBER_FG,   self.append_decimal),
            ("=",   4, 3, 1, COLOUR_BTN_EQUALS,    COLOUR_BTN_EQUALS_FG,   self.evaluate),
        ]

        for (label, row, col, colspan, bg, fg, command) in button_config:
            button = tk.Button(
                buttons_frame,
                text=label,
                bg=bg,
                fg=fg,
                font=("Arial", 18, "bold"),
                relief=tk.FLAT,
                cursor="hand2",
                command=command,
            )
            button.grid(row=row, column=col, columnspan=colspan,
                        padx=3, pady=3, sticky=tk.NSEW, ipady=10)
            buttons_frame.rowconfigure(row, weight=1)

    def _bind_keyboard(self):
        """Allow the user to type numbers and operators on their keyboard too."""
        for digit in "0123456789":
            self.window.bind(digit, lambda event, d=digit: self.append_digit(d))
        self.window.bind("+", lambda e: self.append_operator("+"))
        self.window.bind("-", lambda e: self.append_operator("-"))
        self.window.bind("*", lambda e: self.append_operator("*"))
        self.window.bind("/", lambda e: self.append_operator("/"))
        self.window.bind(".", lambda e: self.append_decimal())
        self.window.bind("<Return>", lambda e: self.evaluate())
        self.window.bind("<BackSpace>", lambda e: self.backspace())
        self.window.bind("<Escape>", lambda e: self.clear())

    # -----------------------------------------------------------------------
    # Calculator logic
    # -----------------------------------------------------------------------

    def append_digit(self, digit):
        """Add a digit to the current expression."""
        if self.current_expression == "0" and digit != ".":
            self.current_expression = digit
        else:
            self.current_expression += digit
        self._update_display()

    def append_operator(self, operator):
        """Add an operator (+, -, *, /) and move to the next number."""
        if not self.current_expression and not self.full_expression:
            return

        self.full_expression += self.current_expression + f" {operator} "
        self.current_expression = ""
        self._update_display()

    def append_decimal(self):
        """Add a decimal point, but only if there isn't one already."""
        if "." not in self.current_expression:
            self.current_expression += "0." if not self.current_expression else "."
        self._update_display()

    def toggle_sign(self):
        """Flip the sign of the current number (positive ↔ negative)."""
        if self.current_expression and self.current_expression != "0":
            if self.current_expression.startswith("-"):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = "-" + self.current_expression
        self._update_display()

    def percent(self):
        """Divide the current number by 100."""
        if self.current_expression:
            try:
                value = float(self.current_expression) / 100
                self.current_expression = self._format_result(value)
                self._update_display()
            except ValueError:
                pass

    def backspace(self):
        """Delete the last character typed."""
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
        self._update_display()

    def clear(self):
        """Reset the calculator completely."""
        self.current_expression = ""
        self.full_expression = ""
        self._update_display()

    def evaluate(self):
        """
        Calculate the result of the full expression.
        eval() executes a string as Python code — convenient here, but in
        real applications you'd never use eval() with untrusted user input.
        """
        if not self.current_expression and not self.full_expression:
            return

        expression = self.full_expression + self.current_expression

        try:
            result = eval(expression)  # noqa: S307
            formatted = self._format_result(result)

            self.full_label.configure(text=f"{expression} =")
            self.current_expression = formatted
            self.full_expression = ""
            self._update_display()

        except ZeroDivisionError:
            self._show_error("Can't divide by zero")
        except Exception:
            self._show_error("Error")

    def _format_result(self, value):
        """Return an integer string if the result is a whole number, else float."""
        if value == int(value):
            return str(int(value))
        return str(round(value, 10)).rstrip("0")

    def _show_error(self, message):
        """Display an error message on screen and reset state."""
        self.current_label.configure(text=message)
        self.current_expression = ""
        self.full_expression = ""

    def _update_display(self):
        """Refresh both display labels to match the current state."""
        display_text = self.current_expression if self.current_expression else "0"
        self.current_label.configure(text=display_text)
        self.full_label.configure(text=self.full_expression)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    window = tk.Tk()
    window.geometry("320x480")

    Calculator(window)

    # mainloop() starts the event loop — it waits for button clicks,
    # key presses, etc. and calls the appropriate methods in response.
    window.mainloop()


if __name__ == "__main__":
    main()

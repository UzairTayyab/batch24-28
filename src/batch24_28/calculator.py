class AdvancedCalculator:
    def __init__(self):
        self.running_total = None
        self.display_value = "0.0"

    def draw_calculator(self):
        print("\n _____________________")
        print("|  _________________  |")
        print(f"| | {self.display_value.rjust(15)} | |")
        print("| |_________________| |")
        print("|  ___   ___   ___    |")
        print("| | 7 | | 8 | | 9 |   |")
        print("| |___| |___| |___|   |")
        print("|  ___   ___   ___    |")
        print("| | 4 | | 5 | | 6 |   |")
        print("| |___| |___| |___|   |")
        print("|  ___   ___   ___    |")
        print("| | 1 | | 2 | | 3 |   |")
        print("| |___| |___| |___|   |")
        print("|  ___   ___   ___    |")
        print("| | C | | 0 | | = |   |")  # Added 'C' to clear/reset the calculator
        print("| |___| |___| |___|   |")
        print("|_____________________|\n")

    def interact(self):
        print("--- Advanced Continuous Calculator ---")
        print("Type 'q' to quit, or 'c' to clear and reset.")
        
        while True:
            self.draw_calculator()
            
            # If we don't have a total yet, ask for the first number
            if self.running_total is None:
                try:
                    val = input("Enter a number (or 'q' to quit): ").strip()
                    if val.lower() == 'q': break
                    if val.lower() == 'c': continue
                    self.running_total = float(val)
                    self.display_value = str(self.running_total)
                    self.draw_calculator() # Redraw with the first number shown
                except ValueError:
                    print("⚠️ Invalid number!")
                    continue

            op = input(f"Operation on ({self.running_total}) [+, -, *, /, ^] or 'c' to clear, 'q' to quit: ").strip()
            if op.lower() == 'q':
                print("Goodbye!")
                break
            if op.lower() == 'c':
                self.running_total = None
                self.display_value = "0.0"
                print("🧹 Calculator cleared!")
                continue
                
            if op not in ['+', '-', '*', '/', '^']:
                print("⚠️ Invalid operation!")
                continue

            try:
                next_val = input("Enter next number: ").strip()
                if next_val.lower() == 'q': break
                if next_val.lower() == 'c':
                    self.running_total = None
                    self.display_value = "0.0"
                    continue
                
                b = float(next_val)
                a = self.running_total

                if op == '+': result = a + b
                elif op == '-': result = a - b
                elif op == '*': result = a * b
                elif op == '/':
                    if b == 0:
                        print("⚠️ Cannot divide by zero!")
                        continue
                    result = a / b
                elif op == '^': result = a ** b

                # Save the result back into the running total so the next loop builds on it
                self.running_total = result
                self.display_value = str(result)

            except ValueError:
                print("⚠️ Invalid input! Please enter numbers only.")
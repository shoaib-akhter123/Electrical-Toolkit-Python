# Electrical Toolkit – Python CLI Project
A Python-based Electrical Toolkit to calculate core electrical engineering values and explore series & parallel resistor circuits. Ideal for students and beginners to visualize Ohm’s Law, power, and resistor networks.
## Features
- Ohm’s Law Calculator – find Voltage (V), Current (I), or Resistance (R)
- Power Calculator – supports all formulas: P = V×I, P = I²×R, P = V²/R
- Series Resistors – calculate total resistance and apply Voltage Division Rule (VDR)
- Parallel Resistors – calculate total resistance and apply Current Division Rule (CDR)
- User-Friendly CLI – interactive menu for easy input
- Input Validation – handles invalid or zero-resistance inputs
## How to Use
Clone or download the repository
Run the main Python file:
Copy code
Bash
python electrical_toolkit.py
Follow the menu to:
Choose what to calculate (V, I, R, Power)
Enter required values
For resistors, select Series or Parallel and input values
View results including total resistance, VDR/CDR calculations, and power
## Example Outputs
Voltage Calculation
Copy code

Enter current (I): 2 A
Enter resistance (R): 5 Ω
Voltage (V) = 10 V
Series Resistors & VDR
Copy code

Resistors: [5 Ω, 10 Ω, 15 Ω]
Total Resistance: 30 Ω
Voltage across R1: 5 V
Voltage across R2: 10 V
Voltage across R3: 15 V
Parallel Resistors & CDR
Copy code

Resistors: [5 Ω, 10 Ω, 20 Ω]
Total Resistance: 2.857 Ω
Current through R1: 2.0 A
Current through R2: 1.0 A
Current through R3: 0.5 A
Next Steps / Improvements
Add mixed series-parallel circuits
Include graphical visualization of voltage and current
Enhance error handling and input validation
Technologies Used
Python 3
CLI (Command Line Interface)
Loops, conditionals, and input handling
Screenshots
Include your 7 screenshots here or in a /screenshots folder for a visual guide.
GitHub Repository
[Add your repository link here]

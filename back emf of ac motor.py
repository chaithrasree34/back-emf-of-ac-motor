# back-emf-of-ac-motor
# Python program to calculate induced EMF of an AC motor

V = float(input("Enter supply voltage (V): "))
I = float(input("Enter motor current (A): "))
R = float(input("Enter effective winding resistance (Ohm): "))

# Calculate voltage drop in winding
voltage_drop = I * R

# Calculate induced EMF
E = V - voltage_drop

print("\nAC Motor Back EMF Calculation")
print("Supply Voltage =", V, "V")
print("Motor Current =", I, "A")
print("Winding Resistance =", R, "Ohm")
print("Voltage Drop =", round(voltage_drop, 2), "V")
print("Induced EMF =", round(E, 2), "V")

Example

Input:

Enter supply voltage (V): 230
Enter motor current (A): 5
Enter effective winding resistance (Ohm): 2


Output:

AC Motor Back EMF Calculation
Supply Voltage = 230.0 V
Motor Current = 5.0 A
Winding Resistance = 2.0 Ohm
Voltage Drop = 10.0 V
Induced EMF = 220.0 V


Note: For an actual induction motor, the induced rotor EMF depends on slip and the motor's equivalent circuit, so a more detailed program would use parameters such as frequency, slip, rotor resistance, and reactance.

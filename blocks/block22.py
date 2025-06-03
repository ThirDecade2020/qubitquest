# block22.py
            # Title: Biased Superposition (RY)

            from braket.circuits import Circuit
import math

def build():
    # Create a biased superposition via RY(π/4) on qubit0
    circuit = Circuit()
    theta = math.pi / 4
    circuit.ry(0, theta)
    return circuit

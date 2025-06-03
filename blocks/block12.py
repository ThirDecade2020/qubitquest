# block12.py
            # Title: Inverse Quantum Fourier Transform (IQFT)

            from braket.circuits import Circuit
import math

def build():
    # 2‐qubit inverse QFT
    circuit = Circuit()
    circuit.swap(0, 1)
    circuit.h(1)
    circuit.cphaseshift(0, 1, -math.pi/2)
    circuit.h(0)
    return circuit

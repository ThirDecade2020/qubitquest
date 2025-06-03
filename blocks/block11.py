# block11.py
            # Title: Quantum Fourier Transform (QFT)

            from braket.circuits import Circuit
import math

def build():
    # 2‐qubit QFT
    circuit = Circuit()
    circuit.h(0)
    circuit.cphaseshift(1, 0, math.pi/2)  # controlled Rₖ for k=2
    circuit.h(1)
    # Swap qubits (optional for 2‐qubit QFT)
    circuit.swap(0, 1)
    return circuit

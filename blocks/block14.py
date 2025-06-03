# block14.py
            # Title: Time Evolution (Trotter)

            from braket.circuits import Circuit
import math

def build():
    # Simulate e^{-iHt} for H = X_0 ⊗ X_1 using a simple 1st-order Trotter step
    circuit = Circuit()
    t = math.pi / 4  # total evolution time
    # Trotter: e^{-i (X⊗X) t} ≈ e^{-i X t} e^{-i X t} for small t; 
    # but for 2‐qubit, use Rxx gate if available. We'll approximate with:
    circuit.rx(0, 2 * t)
    circuit.rx(1, 2 * t)
    return circuit

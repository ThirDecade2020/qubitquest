# block13.py
            # Title: Quantum Phase Estimation

            from braket.circuits import Circuit
import math

def build():
    # 3‐qubit example: 2‐qubit “phase” register, 1‐qubit “unitary” register
    circuit = Circuit()
    # Prepare |+> on phase qubits 0,1
    circuit.h(0); circuit.h(1)
    # Prepare eigenstate on qubit 2 (for U=e^{-iZθ})
    # Assume θ=π/4; controlled‐U^2 from qubit0→2, controlled‐U from qubit1→2
    # U = Rz(π/4) on qubit 2
    circuit.crz(0, 2, math.pi/4 * 2)  # U^2
    circuit.crz(1, 2, math.pi/4)     # U^1
    # Inverse QFT on qubits 0 and 1
    circuit.swap(0, 1)
    circuit.h(1)
    circuit.cphaseshift(0, 1, -math.pi/2)
    circuit.h(0)
    return circuit

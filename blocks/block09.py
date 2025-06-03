# block09.py
            # Title: Phase Kickback (Controlled Phase)

            from braket.circuits import Circuit

def build():
    # Phase kickback: apply a controlled‐Rz gate where control=qubit0, target=qubit1
    circuit = Circuit()
    # Prepare |+> on qubit1 so phase on target kicks back to control
    circuit.h(1)
    # Controlled Rz(π/2) on (0→1)
    circuit.crz(0, 1, 3.141592653589793 / 2)
    return circuit

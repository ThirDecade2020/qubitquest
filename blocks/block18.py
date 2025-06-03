# block18.py
            # Title: Pauli-X Gate

            from braket.circuits import Circuit

def build():
    # Apply Pauli-X (NOT) on qubit0, turning |0> → |1>
    circuit = Circuit()
    circuit.x(0)
    return circuit

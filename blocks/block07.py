# block07.py
            # Title: Grover’s Oracle (One Solution)

            from braket.circuits import Circuit

def build():
    # A 2‐qubit database with one marked state (e.g., |11>), implement Oracle
    circuit = Circuit()
    # Mark |11> by a Z gate on |11> basis (apply CZ on both qubits):
    circuit.cz(0, 1)  
    return circuit

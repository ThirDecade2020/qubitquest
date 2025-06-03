# block16.py
            # Title: Custom Native Gate (RXX)

            from braket.circuits import Circuit

def build():
    # On IonQ hardware, Rxx(θ) is a native two-qubit rotation about XX
    circuit = Circuit()
    # Example: Rxx(π/2) on qubits (0,1)
    circuit.rxx(0, 1, 3.141592653589793 / 2)
    return circuit

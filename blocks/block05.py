# block05.py
            # Title: GHZ State

            from braket.circuits import Circuit

def build():
    # Create a 3‐qubit GHZ state: (|000> + |111>)/√2
    circuit = Circuit()
    circuit.h(0)
    circuit.cnot(0, 1)
    circuit.cnot(1, 2)
    return circuit

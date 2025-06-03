# block06.py
            # Title: W State

            from braket.circuits import Circuit

def build():
    # Create a 3‐qubit W state: (|001> + |010> + |100>)/√3
    circuit = Circuit()
    # Stepwise creation using controlled rotations:
    circuit.ry(2, 2 * 1.0/3.0 * 3.141592653589793)  # approximate rotation
    circuit.cnot(2, 1)
    circuit.cry(1, 0, 2 * 1.0/2.0 * 3.141592653589793)
    return circuit

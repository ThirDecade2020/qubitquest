# block24.py
            # Title: W State & Measure

            from braket.circuits import Circuit

def build():
    # Re‐use W state from block06 and measure all qubits
    circuit = Circuit()
    circuit.ry(2, 2 * 1.0/3.0 * 3.141592653589793)
    circuit.cnot(2, 1)
    circuit.cry(1, 0, 2 * 1.0/2.0 * 3.141592653589793)
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    circuit.measure(2, 2)
    return circuit

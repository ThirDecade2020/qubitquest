# block23.py
            # Title: Two Qubits |00>

            from braket.circuits import Circuit

def build():
    # Explicitly initialize two qubits in |00> (default). Measure both.
    circuit = Circuit()
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    return circuit

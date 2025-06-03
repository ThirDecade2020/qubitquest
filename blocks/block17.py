# block17.py
            # Title: Initialize |0> & Measure

            from braket.circuits import Circuit

def build():
    # Explicitly initialize qubit0 to |0> (implicitly done by default),
    # then measure in computational basis
    circuit = Circuit()
    # (No gate needed; default is |0>.)
    circuit.measure(0, 0)
    return circuit

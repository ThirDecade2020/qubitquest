# block20.py
            # Title: Z-Basis Measurement

            from braket.circuits import Circuit

def build():
    # To measure in Z‐basis is the default measurement.
    # If you want an RZ rotation beforehand:
    circuit = Circuit()
    circuit.rz(0, 3.141592653589793 / 4)  # rotate by π/4
    circuit.measure(0, 0)
    return circuit

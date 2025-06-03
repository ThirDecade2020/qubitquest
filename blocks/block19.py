# block19.py
            # Title: H → X → H (Interference)

            from braket.circuits import Circuit

def build():
    # Demonstrate interference: H → X → H on qubit0
    circuit = Circuit()
    circuit.h(0)
    circuit.x(0)
    circuit.h(0)
    return circuit

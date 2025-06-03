from braket.circuits import Circuit

def build():
    circuit = Circuit()
    circuit.h(0)
    return circuit
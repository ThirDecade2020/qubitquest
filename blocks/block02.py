from braket.circuits import Circuit

def build():
    circuit = Circuit().h(0).cnot(0, 1)
    return circuit
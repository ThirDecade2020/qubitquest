# block08.py
            # Title: Grover’s Diffusion Operator

            from braket.circuits import Circuit

def build():
    # Grover diffusion for 2 qubits: reflect about uniform superposition
    circuit = Circuit()
    # H on all qubits
    circuit.h(0); circuit.h(1)
    # X on all qubits
    circuit.x(0); circuit.x(1)
    # Multi‐controlled Z (apply Z to |00>):
    circuit.h(1)
    circuit.cnot(0, 1)
    circuit.h(1)
    # X on all qubits
    circuit.x(0); circuit.x(1)
    # H on all qubits
    circuit.h(0); circuit.h(1)
    return circuit

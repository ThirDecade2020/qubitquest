# block10.py
            # Title: Deutsch–Jozsa Algorithm

            from braket.circuits import Circuit

def build():
    # For a 2‐qubit Deutsch–Jozsa oracle (balanced or constant)
    circuit = Circuit()
    # Prepare |01> in input register if we want to use f(x)=x0⊕x1, for example
    circuit.h(0); circuit.h(1)
    circuit.x(2)  # ancilla in |1>
    circuit.h(2)
    # Example oracle for f(x) = x0 ⊕ x1: CNOT(0→2), CNOT(1→2)
    circuit.cnot(0, 2)
    circuit.cnot(1, 2)
    # Apply Hadamard to inputs, measure them to see if “balanced” or “constant”
    circuit.h(0); circuit.h(1)
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    return circuit

# block25.py
            # Title: Bell State with Mid-Circuit Measurement

            from braket.circuits import Circuit

def build():
    circuit = Circuit()
    # Create a Bell pair on qubit 0 & 1
    circuit.h(0)
    circuit.cnot(0, 1)
    # Measure qubit 1 mid-circuit and reset it to |0>
    circuit.measure(1, 1)
    circuit.reset(1)    # Reset qubit 1 to |0>
    # Use qubit 1 after reset (e.g., apply H again)
    circuit.h(1)
    return circuit

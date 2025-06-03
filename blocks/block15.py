# block15.py
            # Title: 3‐Qubit Bit‐Flip Code

            from braket.circuits import Circuit

def build():
    # Encode logical |ψ> into 3 physical qubits, detect a single bit-flip
    # Step 1: Start with |ψ> on qubit 0 (assume |ψ> = |1>, flip qubit 0 for demo)
    circuit = Circuit()
    circuit.x(0)  # example: |ψ> = |1> on qubit 0
    # Step 2: Copy qubit0 into qubit1 & qubit2
    circuit.cnot(0, 1)
    circuit.cnot(0, 2)
    # Step 3: Introduce an error (X on qubit 1)
    circuit.x(1)
    # Step 4: Syndrome measurement: measure parity between (0,1) and (0,2)
    circuit.cx(0, 1)
    circuit.cx(0, 2)
    circuit.measure(1, 1)
    circuit.measure(2, 2)
    return circuit

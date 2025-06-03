# block03.py
            # Title: Swap Test

            from braket.circuits import Circuit

def build():
    # Swap test circuit for comparing two single-qubit states
    circuit = Circuit()
    # Prepare ancilla (qubit 0) in |+>:
    circuit.h(0)
    # Assume the two states to compare are built on qubit1 and qubit2.
    # For illustration, we compare |0> and |1> (you can modify as needed):
    # state1 = |0> (default)
    # state2 = |1> (apply X on qubit 2 to flip it to |1>)
    circuit.x(2)
    # Controlled-SWAP: if ancilla==1, swap qubit1 and qubit2
    circuit.cswap(0, 1, 2)
    # Hadamard on ancilla again, then measure ancilla
    circuit.h(0)
    return circuit

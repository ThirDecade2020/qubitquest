# block04.py
            # Title: Quantum Teleportation

            from braket.circuits import Circuit

def build():
    # Teleportation of an arbitrary qubit (qubit0) to qubit2, using qubit1 as entanglement pair
    circuit = Circuit()
    # Step 1: Prepare entangled pair between qubit1 & qubit2
    circuit.h(1)
    circuit.cnot(1, 2)
    # Step 2: Bell measurement on qubit0 + qubit1
    circuit.cnot(0, 1)
    circuit.h(0)
    # Step 3: Measure qubit0 and qubit1 (we do not include classical feed-forward here)
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    # Step 4 (in real hardware, you'd do conditional X/Z on qubit2 depending on meas)
    return circuit

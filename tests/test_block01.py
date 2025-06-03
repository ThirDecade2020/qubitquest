from blocks.block01 import build
from braket.circuits import Circuit

def test_block_builds_valid_circuit():
    circuit = build()
    assert isinstance(circuit, Circuit)
    assert circuit.qubit_count == 1
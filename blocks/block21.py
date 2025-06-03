# block21.py
            # Title: State Vector Visualization

            from braket.circuits import Circuit
from braket.aws import AwsDevice

def build():
    # For a pure Python “visualization” block we just build a simple state
    circuit = Circuit()
    circuit.h(0)
    return circuit

def visualize():
    # This example is for the Braket local simulator only.
    # Use the local simulator to get the statevector, then print it.
    from braket.devices import LocalSimulator
    device = LocalSimulator("braket_sv")
    task = device.run(build(), shots=0, disable_qubit_rewiring=True)
    result = task.result()
    return result.state_vector

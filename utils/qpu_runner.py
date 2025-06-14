# utils/qpu_runner.py

from braket.aws import AwsDevice

# ARN for the IonQ Harmony device on AWS Braket
IONQ_DEVICE_ARN = "arn:aws:braket:::device/qpu/ionq/Harmony"

def submit_to_ionq(circuit, shots: int = 100):
    """
    Submit the given Braket Circuit to IonQ Harmony and wait for results.
    Returns a dict mapping measurement bitstrings to counts.
    """
    device = AwsDevice(IONQ_DEVICE_ARN)

    # Check device status (string)
    status = device.status()
    if status != "ONLINE":
        raise RuntimeError(f"IonQ device not ready (status={status})")

    # Submit the job (blocks until complete)
    task = device.run(circuit, shots=shots)
    result = task.result()

    return result.measurement_counts


The 3‐qbit bit‐flip code encodes |ψ> across three qubits:  
1) Encode: CNOT(0→1), CNOT(0→2).  
2) (Example) Introduce X “bit‐flip” on qubit 1.  
3) Syndrome: Compare qubit 0 vs qubit 1 (CNOT, measure) and qubit 0 vs qubit 2 (CNOT, measure).  
If one of the syndrome measurements is 1, that indicates which qubit flipped.

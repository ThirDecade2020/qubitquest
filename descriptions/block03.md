The Swap Test uses a single ancilla qubit to compare two states |ψ⟩ (on qubit 1) 
and |φ⟩ (on qubit 2).  
1) Put ancilla in |+⟩ via H.  
2) Controlled-SWAP between qubit 1 and qubit 2, conditioned on ancilla.  
3) Apply H on ancilla again and measure.  
The probability of measuring ancilla=0 indicates overlap between |ψ⟩ and |φ⟩.  
In this example, we compare |0⟩ vs |1⟩ (so outcome ancilla=1 with high probability).

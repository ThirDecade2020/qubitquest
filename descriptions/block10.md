Deutsch–Jozsa decides if a function f is constant or balanced.  
Here, example oracle: f(x) = x₀ ⊕ x₁.  
Steps:  
1) H on input qubits (0,1); X+H on ancilla (qubit 2).  
2) Oracle: CNOT(0→2), CNOT(1→2).  
3) H on inputs → measure. All-0 means “constant,” otherwise “balanced.”

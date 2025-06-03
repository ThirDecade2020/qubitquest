# populate_blocks.py
# ----------------------------------------------------------------------
# This script auto-generates the remaining blocks (03–25), their markdown
# descriptions, and their LaTeX formulas. Simply run `python populate_blocks.py`
# once in the `qubitquest/` folder to populate everything.
# ----------------------------------------------------------------------

import os
import textwrap

# 1) Define a list of all 25 block‐ID / titles / code / description / formula
#    Each entry is (block_id, title, python_code, markdown_desc, latex_formula).
#    We have already created block01 (Hadamard) and block02 (Bell State).
#    Starting from block03, we fill in each of the “25-step progression” examples.

ALL_BLOCKS = [
    # block01 and block02 were already created by the scaffold.
    # We list them here for completeness; they will be skipped when writing new files:
    (
        "block01",
        "Hadamard Superposition",
        # code:
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Apply a Hadamard gate to qubit 0
                circuit = Circuit()
                circuit.h(0)
                return circuit
        """).strip(),
        # markdown description:
        textwrap.dedent(r"""
            The Hadamard gate creates a superposition of basis states |0⟩ and |1⟩.
            Starting from |0⟩, applying H gives:

                H|0⟩ = (|0⟩ + |1⟩)/√2
        """).strip(),
        # LaTeX formula:
        r"""
        H = \frac{1}{\sqrt{2}} 
        \begin{bmatrix}
        1 & 1 \\
        1 & -1
        \end{bmatrix}, 
        \quad
        H\lvert 0\rangle = \frac{1}{\sqrt{2}}(\lvert0\rangle + \lvert1\rangle)
        """.strip(),
    ),
    (
        "block02",
        "Bell State",
        # code: build |Φ⁺⟩ = (|00⟩+|11⟩)/√2
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Create a two-qubit Bell state |Φ+> = (|00> + |11>)/√2
                circuit = Circuit()
                circuit.h(0)         # superpose qubit 0
                circuit.cnot(0, 1)   # entangle 0 with 1
                return circuit
        """).strip(),
        # markdown description:
        textwrap.dedent(r"""
            The Bell State (specifically |Φ⁺⟩) is a maximally entangled two-qubit state:  
            \[
              \lvert \Phi^{+} \rangle 
              = \frac{1}{\sqrt{2}}(\lvert00\rangle + \lvert11\rangle).
            \]
            We first apply H on qubit 0, then CNOT from qubit 0 to qubit 1.
        """).strip(),
        # LaTeX formula:
        r"""
        \lvert \Phi^{+} \rangle = \frac{1}{\sqrt{2}} (\lvert00\rangle + \lvert11\rangle),
        \quad
        \Phi^{+} = \frac{1}{\sqrt{2}}
        \begin{bmatrix}
        1 & 0 & 0 & 1 \\
        0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0 \\
        1 & 0 & 0 & 1 
        \end{bmatrix}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 03: Swap Test
    ################################################################################
    (
        "block03",
        "Swap Test",
        textwrap.dedent("""
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
        """).strip(),
        textwrap.dedent(r"""
            The Swap Test uses a single ancilla qubit to compare two states |ψ⟩ (on qubit 1) 
            and |φ⟩ (on qubit 2).  
            1) Put ancilla in |+⟩ via H.  
            2) Controlled-SWAP between qubit 1 and qubit 2, conditioned on ancilla.  
            3) Apply H on ancilla again and measure.  
            The probability of measuring ancilla=0 indicates overlap between |ψ⟩ and |φ⟩.  
            In this example, we compare |0⟩ vs |1⟩ (so outcome ancilla=1 with high probability).
        """).strip(),
        r"""
        \text{Swap‐Test}:
        \quad
        \begin{aligned}
        &\lvert0\rangle_{\text{anc}} \xrightarrow{H} \frac{\lvert0\rangle+\lvert1\rangle}{\sqrt2}, \\
        &\text{CsWAP}(\text{anc},\,q_1,\,q_2), \\
        &H_{\text{anc}}\,\rightarrow\,\text{measure(anc)}. 
        \end{aligned}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 04: Quantum Teleportation
    ################################################################################
    (
        "block04",
        "Quantum Teleportation",
        textwrap.dedent("""
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
        """).strip(),
        textwrap.dedent(r"""
            Quantum teleportation transmits an unknown qubit |ψ⟩ (on qubit 0) to qubit 2 using 
            an entangled pair (qubit 1 & qubit 2).  
            1) Create Bell pair on (1,2): H(1) → CNOT(1,2).  
            2) Bell‐state measurement on (0,1) via CNOT(0,1) and H(0).  
            3) Measure qubits 0 and 1.  
            4) (In hardware) Apply corrections on qubit 2 based on classical outcomes.  
            The state |ψ⟩ originally on qubit 0 reappears on qubit 2.
        """).strip(),
        r"""
        \begin{aligned}
        &\lvert \psi\rangle_0 \otimes \lvert \Phi^{+} \rangle_{12} \\
        &\xrightarrow{\text{Bell‐measure(0,1)}} (\text{Bell‐outcomes},\,X^m Z^n \lvert \psi\rangle_2)
        \end{aligned}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 05: GHZ State (3 Qubits)
    ################################################################################
    (
        "block05",
        "GHZ State",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Create a 3‐qubit GHZ state: (|000> + |111>)/√2
                circuit = Circuit()
                circuit.h(0)
                circuit.cnot(0, 1)
                circuit.cnot(1, 2)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            A 3‐qubit GHZ state is 
            \[
              \lvert \text{GHZ}\rangle 
              = \frac{1}{\sqrt{2}} (\lvert000\rangle + \lvert111\rangle).
            \]
            We apply H on qubit 0, then CNOT(0→1), then CNOT(1→2).
        """).strip(),
        r"""
        \lvert \text{GHZ}\rangle = \frac{1}{\sqrt{2}} (\lvert000\rangle + \lvert111\rangle)
        """.strip(),
    ),
    ################################################################################
    # BLOCK 06: W State (3 Qubits)
    ################################################################################
    (
        "block06",
        "W State",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Create a 3‐qubit W state: (|001> + |010> + |100>)/√3
                circuit = Circuit()
                # Stepwise creation using controlled rotations:
                circuit.ry(2, 2 * 1.0/3.0 * 3.141592653589793)  # approximate rotation
                circuit.cnot(2, 1)
                circuit.cry(1, 0, 2 * 1.0/2.0 * 3.141592653589793)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            A 3‐qubit W state is 
            \[
              \lvert W\rangle 
              = \frac{1}{\sqrt{3}} (\lvert001\rangle + \lvert010\rangle + \lvert100\rangle).
            \]
            One way to build it is via sequential Ry rotations and CNOTs; here we show an 
            approximate Ry‐based construction.  
        """).strip(),
        r"""
        \lvert W\rangle = \frac{1}{\sqrt{3}} (\lvert001\rangle + \lvert010\rangle + \lvert100\rangle)
        """.strip(),
    ),
    ################################################################################
    # BLOCK 07: Grover’s Oracle (1-solution)
    ################################################################################
    (
        "block07",
        "Grover’s Oracle (One Solution)",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # A 2‐qubit database with one marked state (e.g., |11>), implement Oracle
                circuit = Circuit()
                # Mark |11> by a Z gate on |11> basis (apply CZ on both qubits):
                circuit.cz(0, 1)  
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            Grover’s oracle flips the sign of the marked state—e.g., |11⟩. Here, a controlled‐Z gate 
            on qubits (0,1) implements that phase flip on |11⟩.  
        """).strip(),
        r"""
        U_{f}\lvert x\rangle \;=\; (-1)^{f(x)}\lvert x\rangle,\quad
        U_{f} = \begin{cases}
          -1 & x = 11,\\
          +1 & \text{else}.
        \end{cases}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 08: Grover’s Diffusion Operator
    ################################################################################
    (
        "block08",
        "Grover’s Diffusion Operator",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Grover diffusion for 2 qubits: reflect about uniform superposition
                circuit = Circuit()
                # H on all qubits
                circuit.h(0); circuit.h(1)
                # X on all qubits
                circuit.x(0); circuit.x(1)
                # Multi‐controlled Z (apply Z to |00>):
                circuit.h(1)
                circuit.cnot(0, 1)
                circuit.h(1)
                # X on all qubits
                circuit.x(0); circuit.x(1)
                # H on all qubits
                circuit.h(0); circuit.h(1)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            The diffusion operator (in 2‐qubit Grover) is “inversion about the mean.”  
            Steps: H⊗H → X⊗X → controlled‐Z on |00⟩ → X⊗X → H⊗H.  
        """).strip(),
        r"""
        D = H^{\otimes 2} \;X^{\otimes 2}\; CZ\; X^{\otimes 2}\; H^{\otimes 2}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 09: Phase Kickback (Controlled-Phase)
    ################################################################################
    (
        "block09",
        "Phase Kickback (Controlled Phase)",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Phase kickback: apply a controlled‐Rz gate where control=qubit0, target=qubit1
                circuit = Circuit()
                # Prepare |+> on qubit1 so phase on target kicks back to control
                circuit.h(1)
                # Controlled Rz(π/2) on (0→1)
                circuit.crz(0, 1, 3.141592653589793 / 2)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            Phase kickback uses a controlled‐phase gate.  
            If qubit 1 is in |+⟩ (i.e. H applied), a controlled‐Rz on (0→1) will “kick back” 
            phase onto qubit 0.  
        """).strip(),
        r"""
        \text{Controlled-}R_{z}(\theta) =
        \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        0 & 0 & 0 & e^{i\theta}
        \end{pmatrix}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 10: Deutsch-Jozsa Algorithm
    ################################################################################
    (
        "block10",
        "Deutsch–Jozsa Algorithm",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # For a 2‐qubit Deutsch–Jozsa oracle (balanced or constant)
                circuit = Circuit()
                # Prepare |01> in input register if we want to use f(x)=x0⊕x1, for example
                circuit.h(0); circuit.h(1)
                circuit.x(2)  # ancilla in |1>
                circuit.h(2)
                # Example oracle for f(x) = x0 ⊕ x1: CNOT(0→2), CNOT(1→2)
                circuit.cnot(0, 2)
                circuit.cnot(1, 2)
                # Apply Hadamard to inputs, measure them to see if “balanced” or “constant”
                circuit.h(0); circuit.h(1)
                circuit.measure(0, 0)
                circuit.measure(1, 1)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            Deutsch–Jozsa decides if a function f is constant or balanced.  
            Here, example oracle: f(x) = x₀ ⊕ x₁.  
            Steps:  
            1) H on input qubits (0,1); X+H on ancilla (qubit 2).  
            2) Oracle: CNOT(0→2), CNOT(1→2).  
            3) H on inputs → measure. All-0 means “constant,” otherwise “balanced.”
        """).strip(),
        r"""
        U_{f}\lvert x\rangle \lvert y\rangle = \lvert x\rangle \lvert y \oplus f(x)\rangle,
        \quad
        f(x) = x_{0} \oplus x_{1}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 11: Quantum Fourier Transform (QFT)
    ################################################################################
    (
        "block11",
        "Quantum Fourier Transform (QFT)",
        textwrap.dedent("""
            from braket.circuits import Circuit
            import math

            def build():
                # 2‐qubit QFT
                circuit = Circuit()
                circuit.h(0)
                circuit.cphaseshift(1, 0, math.pi/2)  # controlled Rₖ for k=2
                circuit.h(1)
                # Swap qubits (optional for 2‐qubit QFT)
                circuit.swap(0, 1)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            The Quantum Fourier Transform on two qubits:  
            1) Apply H on q₀.  
            2) Apply controlled‐phase R₂ (π/2) from q₁→q₀.  
            3) H on q₁.  
            4) Swap q₀⇄q₁.  
        """).strip(),
        r"""
        U_{\text{QFT}_{2}} =
        \begin{pmatrix}
        1 & 1 & 1 & 1 \\
        1 & i & -1 & -i \\
        1 & -1 & 1 & -1 \\
        1 & -i & -1 & i
        \end{pmatrix}
        \frac{1}{2}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 12: Inverse QFT (IQFT)
    ################################################################################
    (
        "block12",
        "Inverse Quantum Fourier Transform (IQFT)",
        textwrap.dedent("""
            from braket.circuits import Circuit
            import math

            def build():
                # 2‐qubit inverse QFT
                circuit = Circuit()
                circuit.swap(0, 1)
                circuit.h(1)
                circuit.cphaseshift(0, 1, -math.pi/2)
                circuit.h(0)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            The inverse QFT on two qubits:  
            1) Swap q₀⇄q₁.  
            2) H on q₁.  
            3) Controlled‐R₋₂ (–π/2) from q₀→q₁.  
            4) H on q₀.  
        """).strip(),
        r"""
        U_{\text{IQFT}_{2}} = U_{\text{QFT}_{2}}^{\dagger}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 13: Quantum Phase Estimation (QPE)
    ################################################################################
    (
        "block13",
        "Quantum Phase Estimation",
        textwrap.dedent("""
            from braket.circuits import Circuit
            import math

            def build():
                # 3‐qubit example: 2‐qubit “phase” register, 1‐qubit “unitary” register
                circuit = Circuit()
                # Prepare |+> on phase qubits 0,1
                circuit.h(0); circuit.h(1)
                # Prepare eigenstate on qubit 2 (for U=e^{-iZθ})
                # Assume θ=π/4; controlled‐U^2 from qubit0→2, controlled‐U from qubit1→2
                # U = Rz(π/4) on qubit 2
                circuit.crz(0, 2, math.pi/4 * 2)  # U^2
                circuit.crz(1, 2, math.pi/4)     # U^1
                # Inverse QFT on qubits 0 and 1
                circuit.swap(0, 1)
                circuit.h(1)
                circuit.cphaseshift(0, 1, -math.pi/2)
                circuit.h(0)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            Quantum Phase Estimation estimates an eigenvalue φ of U via:  
            1) Prepare |+⟩ on “phase” qubits, 
            2) Controlled‐U^{2^{j}} gates onto eigenstate register (qubit 2),  
            3) Apply inverse QFT on phase register (qubits 0,1).  
            Here U = Rₓ(π/4) on qubit 2, φ = θ/2π = 1/8.
        """).strip(),
        r"""
        \text{QPE:} \quad 
        \frac{1}{2^{n}} \sum_{y=0}^{2^{n}-1} e^{2\pi i \phi y} \lvert y\rangle \lvert u\rangle
        """.strip(),
    ),
    ################################################################################
    # BLOCK 14: Simulate Time Evolution e^{-iHt} (Trotter)
    ################################################################################
    (
        "block14",
        "Time Evolution (Trotter)",
        textwrap.dedent("""
            from braket.circuits import Circuit
            import math

            def build():
                # Simulate e^{-iHt} for H = X_0 ⊗ X_1 using a simple 1st-order Trotter step
                circuit = Circuit()
                t = math.pi / 4  # total evolution time
                # Trotter: e^{-i (X⊗X) t} ≈ e^{-i X t} e^{-i X t} for small t; 
                # but for 2‐qubit, use Rxx gate if available. We'll approximate with:
                circuit.rx(0, 2 * t)
                circuit.rx(1, 2 * t)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            We want to simulate e^{-iHt} for H = X₀ ⊗ X₁.  
            A first-order Trotter step:  
            \[
              e^{-i X_0 X_1 t} \approx e^{-i X_0 t} e^{-i X_1 t},  
              \quad
              \text{for small }t.
            \]
            Here we set t = π/4 and approximate with Rx rotations on each qubit.
        """).strip(),
        r"""
        e^{-i X_0 X_1 t} \approx e^{-i X_{0} t} e^{-i X_{1} t}
        \quad
        \bigl(t = \frac{\pi}{4}\bigr)
        """.strip(),
    ),
    ################################################################################
    # BLOCK 15: 3‐Qubit Bit‐Flip Error Detection Code
    ################################################################################
    (
        "block15",
        "3‐Qubit Bit‐Flip Code",
        textwrap.dedent("""
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
        """).strip(),
        textwrap.dedent(r"""
            The 3‐qbit bit‐flip code encodes |ψ> across three qubits:  
            1) Encode: CNOT(0→1), CNOT(0→2).  
            2) (Example) Introduce X “bit‐flip” on qubit 1.  
            3) Syndrome: Compare qubit 0 vs qubit 1 (CNOT, measure) and qubit 0 vs qubit 2 (CNOT, measure).  
            If one of the syndrome measurements is 1, that indicates which qubit flipped.
        """).strip(),
        r"""
        \begin{aligned}
        &\lvert \psi \rangle_0 
        \xrightarrow[\text{encode}]{\text{CNOT}(0,1),\,\text{CNOT}(0,2)} 
        \lvert \psi\psi\psi\rangle_{012}
        \\
        &\text{(Flip Error on qubit1)}: X_{1}
        \\
        &\text{Syndrome: } 
        \begin{cases}
          s_{01} = \langle Z_{0} Z_{1}\rangle,\quad
          s_{02} = \langle Z_{0} Z_{2}\rangle
        \end{cases}
        \end{aligned}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 16: Custom Native Gates (RXX, etc.)
    ################################################################################
    (
        "block16",
        "Custom Native Gate (RXX)",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # On IonQ hardware, Rxx(θ) is a native two-qubit rotation about XX
                circuit = Circuit()
                # Example: Rxx(π/2) on qubits (0,1)
                circuit.rxx(0, 1, 3.141592653589793 / 2)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            The R_{XX}(θ) gate is a rotation around the 𝑋⊗𝑋 axis:  
            \[
              R_{XX}(\theta) = \exp\Bigl(-i \frac{\theta}{2} X\otimes X\Bigr).
            \]
            On IonQ hardware, this is a native two‐qubit gate. In this example, θ = π/2.
        """).strip(),
        r"""
        R_{XX}(\theta) = \exp\bigl(-i\,\tfrac{\theta}{2}\,X\otimes X\bigr)
        """.strip(),
    ),
    ################################################################################
    # BLOCK 17: Initialize |0⟩ (Explicit) & Measure
    ################################################################################
    (
        "block17",
        "Initialize |0> & Measure",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Explicitly initialize qubit0 to |0> (implicitly done by default),
                # then measure in computational basis
                circuit = Circuit()
                # (No gate needed; default is |0>.)
                circuit.measure(0, 0)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            Every qubit starts in |0⟩ by default on IonQ hardware. Here, we simply measure 
            qubit 0 in the Z‐basis, confirming it’s |0⟩ with probability 1.
        """).strip(),
        r"""
        \lvert 0\rangle \xrightarrow{\text{measure}} 0
        """.strip(),
    ),
    ################################################################################
    # BLOCK 18: Apply Pauli‐X Gate
    ################################################################################
    (
        "block18",
        "Pauli-X Gate",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Apply Pauli-X (NOT) on qubit0, turning |0> → |1>
                circuit = Circuit()
                circuit.x(0)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            The Pauli-X gate (bit‐flip) maps |0⟩ ↔ |1⟩. In this block, 
            \lvert 0\rangle \xrightarrow{X} \lvert 1\rangle.
        """).strip(),
        r"""
        X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, 
        \quad X\lvert 0\rangle = \lvert 1\rangle
        """.strip(),
    ),
    ################################################################################
    # BLOCK 19: Hadamard → X → Hadamard (Interference Example)
    ################################################################################
    (
        "block19",
        "H → X → H (Interference)",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Demonstrate interference: H → X → H on qubit0
                circuit = Circuit()
                circuit.h(0)
                circuit.x(0)
                circuit.h(0)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            Sequence H → X → H exhibits interference:  
            H maps |0⟩ → (|0⟩+|1⟩)/√2, then X flips amplitudes, then H recombines them.  
        """).strip(),
        r"""
        H X H = \frac{1}{\sqrt{2}}
        \begin{pmatrix}
        1 & 1 \\ 1 & -1
        \end{pmatrix} X 
        \frac{1}{\sqrt{2}}
        \begin{pmatrix}
        1 & 1 \\ 1 & -1
        \end{pmatrix}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 20: Z-Basis Measurement (RZ + measure)
    ################################################################################
    (
        "block20",
        "Z-Basis Measurement",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # To measure in Z‐basis is the default measurement.
                # If you want an RZ rotation beforehand:
                circuit = Circuit()
                circuit.rz(0, 3.141592653589793 / 4)  # rotate by π/4
                circuit.measure(0, 0)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            By default, measuring a qubit is in the Z‐basis. Here we optionally apply 
            an RZ(π/4) rotation to shift phase before measuring.
        """).strip(),
        r"""
        \lvert \psi \rangle \xrightarrow{R_{z}(\theta)} 
        R_{z}(\theta)\lvert \psi \rangle \xrightarrow{\text{measure}} \{0,1\}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 21: State Vector Visualization (Bloch Sphere) [Simulator Only]
    ################################################################################
    (
        "block21",
        "State Vector Visualization",
        textwrap.dedent("""
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
        """).strip(),
        textwrap.dedent(r"""
            This block shows how to get the full statevector (e.g., on a local simulator).
            Here, after H on qubit 0, the statevector = (1/√2, 1/√2).  
            In a real tutorial, you’d render this on a Bloch sphere.  
        """).strip(),
        r"""
        \lvert \psi \rangle 
        = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 22: Biased Superposition (RY Rotation)
    ################################################################################
    (
        "block22",
        "Biased Superposition (RY)",
        textwrap.dedent("""
            from braket.circuits import Circuit
            import math

            def build():
                # Create a biased superposition via RY(π/4) on qubit0
                circuit = Circuit()
                theta = math.pi / 4
                circuit.ry(0, theta)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            A biased superposition uses RY(θ).  
            Here, θ = π/4 gives amplitudes (cos(π/8), sin(π/8)).  
        """).strip(),
        r"""
        R_{y}(\theta) = 
        \begin{pmatrix}
        \cos(\theta/2) & -\sin(\theta/2) \\
        \sin(\theta/2) & \cos(\theta/2)
        \end{pmatrix},
        \quad \theta = \frac{\pi}{4}
        """.strip(),
    ),
    ################################################################################
    # BLOCK 23: Two Qubits |00> Initialization
    ################################################################################
    (
        "block23",
        "Two Qubits |00>",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Explicitly initialize two qubits in |00> (default). Measure both.
                circuit = Circuit()
                circuit.measure(0, 0)
                circuit.measure(1, 1)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            By default all qubits are in |0⟩. Here we simply measure two qubits to confirm |00⟩.
        """).strip(),
        r"""
        \lvert 00\rangle \xrightarrow{\text{measure}} 00
        """.strip(),
    ),
    ################################################################################
    # BLOCK 24: Create 3-Qubit W State & Measure
    ################################################################################
    (
        "block24",
        "W State & Measure",
        textwrap.dedent("""
            from braket.circuits import Circuit

            def build():
                # Re‐use W state from block06 and measure all qubits
                circuit = Circuit()
                circuit.ry(2, 2 * 1.0/3.0 * 3.141592653589793)
                circuit.cnot(2, 1)
                circuit.cry(1, 0, 2 * 1.0/2.0 * 3.141592653589793)
                circuit.measure(0, 0)
                circuit.measure(1, 1)
                circuit.measure(2, 2)
                return circuit
        """).strip(),
        textwrap.dedent(r"""
            We create the 3‐qubit W state (as in block06) and then measure all three qubits.  
            The outcome is probabilistic: each of {001,010,100} with probability 1/3.
        """).strip(),
        r"""
        \lvert W\rangle = \frac{1}{\sqrt{3}} (\lvert001\rangle + \lvert010\rangle + \lvert100\rangle)
        """.strip(),
    ),
    ################################################################################
    # BLOCK 25: Bell State with Mid‐Circuit Measurement & Reset
    ################################################################################
    (
        "block25",
        "Bell State with Mid-Circuit Measurement",
        textwrap.dedent("""
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
        """).strip(),
        textwrap.dedent(r"""
            This block creates a Bell state on (0,1), then performs a mid-circuit measurement 
            of qubit 1, resets it to |0⟩, and finally applies H on the reset qubit.  
            Demonstrates mid-circuit measurement + reset on IonQ hardware.
        """).strip(),
        r"""
        \text{Bell→Measure}(q_{0},q_{1}) \xrightarrow{\text{measure } q_{1}} 
        \lvert? \rangle\,; \;\text{reset}(q_{1})\,; \; H(q_{1})
        """.strip(),
    ),
]


def ensure_dirs_exist():
    """Ensure that blocks/, descriptions/, and formulas/ folders exist."""
    for folder in ("blocks", "descriptions", "formulas"):
        if not os.path.isdir(folder):
            os.makedirs(folder)


def write_file(path: str, content: str):
    """Write content to a file, overwriting if it exists."""
    with open(path, "w") as f:
        f.write(content.strip() + "\n")


def main():
    ensure_dirs_exist()

    for block_id, title, code_str, md_str, tex_str in ALL_BLOCKS:
        # Skip block01 and block02 if they already exist (they were part of scaffold)
        # If you want to overwrite them anyway, remove this check.
        # Here we only create missing files for block03–block25.
        if block_id in ("block01", "block02"):
            continue

        # 1) Write blocks/blockXX.py
        block_py = textwrap.dedent(f"""
            # {block_id}.py
            # Title: {title}

            {code_str}
        """).strip()
        write_file(os.path.join("blocks", f"{block_id}.py"), block_py)

        # 2) Write descriptions/blockXX.md
        write_file(os.path.join("descriptions", f"{block_id}.md"), md_str)

        # 3) Write formulas/blockXX.tex
        write_file(os.path.join("formulas", f"{block_id}.tex"), tex_str)

    print("✅ All missing blocks (03–25) have been generated under blocks/, descriptions/, and formulas/.")
    print("   Next: Update main.py’s BLOCKS list to include block03–block25.")

if __name__ == "__main__":
    main()


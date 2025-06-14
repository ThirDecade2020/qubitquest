# landing.py

import os
from pywebio import start_server
from pywebio.output import put_image, put_html, put_buttons, clear
from main import main  # Import the tutorial entry function

# Compute the absolute path to this file’s directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def landing():
    # Display the pixelated Standard Model logo (electron highlighted)
    logo_path = os.path.join(BASE_DIR, "assets", "qubitquest_logo_pixelated.png")
    with open(logo_path, "rb") as f:
        img_data = f.read()
    put_image(img_data)

    # One-sentence tagline
    put_html(
        "<p style='font-family: monospace; font-size: 16px;'>"
        "Enter the quantum realm where real particles, real math, and real code power your quest "
        "for fundamental understanding."
        "</p>"
    )

    # Focused on fundamentality
    put_html(r'''
    <h3 style="font-family: monospace;">Why “Fundamental” Matters</h3>
    <p style="font-family: monospace; font-size:14px;">
      QubitQuest uses <b>trapped‐ion qubits</b> because they let you directly harness the 
      <i>actual particles and interactions</i> at the heart of quantum theory:
    </p>
    <ul style="font-family: monospace; font-size:14px;">
      <li><b>Single Atomic Ions:</b> Each qubit is one ¹⁷¹Yb⁺ ion—no emergent circuits, just fundamental particles.</li>
      <li><b>Laser‐Driven Transitions:</b> We manipulate real electronic energy levels (|0⟩ ↔ |1⟩) via focused laser beams—textbook quantum mechanics in action.</li>
      <li><b>Direct Quantum Interactions:</b> Entanglement and gates arise from Coulomb coupling and photon exchange, not engineered Josephson junctions.</li>
    </ul>
    <p style="font-family: monospace; font-size:14px;">
      We surface these first-principles in every lesson, so you learn quantum computing by directly engaging the same particles your equations describe.
    </p>
    ''')

    # Site purpose & learning progression
    put_html(r'''
    <h3 style="font-family: monospace;">What is QubitQuest?</h3>
    <p style="font-family: monospace; font-size:14px;">
      QubitQuest guides you through a curated selection of fundamental quantum computing algorithms.
      Each lesson builds your understanding by aligning the mathematics, code, and hardware:
    </p>
    <ul style="font-family: monospace; font-size:14px;">
      <li>Start with single-qubit basics (superposition, Hadamard, Pauli gates).</li>
      <li>Progress to entanglement and multi-qubit states (Bell, GHZ, W).</li>
      <li>Dive into core algorithms: Grover’s search, Quantum Fourier Transform, Phase Estimation, and more.</li>
    </ul>
    <p style="font-family: monospace; font-size:14px;">
      Practice by writing and running code directly on real IonQ hardware, reinforcing quantum mechanics from the ground up.
    </p>
    ''')

    # “▶ Begin QubitQuest” button
    put_buttons(
        ["▶ Begin QubitQuest"],
        onclick=[lambda: _enter_tutorial()]
    )

def _enter_tutorial():
    """
    Clear the landing page and invoke the main() function
    to start the QubitQuest tutorial directly.
    """
    clear()
    main()

if __name__ == "__main__":
    # Serve only landing(), with MathJax enabled via CDN
    start_server(landing, port=8080, cdn=True)


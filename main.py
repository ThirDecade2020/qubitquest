# main.py

import os
from pywebio import start_server
from pywebio.output import put_text, put_buttons, put_code, put_html, clear
import run_counter
import update_counter
from utils.qpu_runner import submit_to_ionq

# Load metadata for all 25 blocks at startup
BLOCKS = []
for block_id in [
    "block01", "block02", "block03", "block04", "block05",
    "block06", "block07", "block08", "block09", "block10",
    "block11", "block12", "block13", "block14", "block15",
    "block16", "block17", "block18", "block19", "block20",
    "block21", "block22", "block23", "block24", "block25",
]:
    code_path = os.path.join("blocks", f"{block_id}.py")
    with open(code_path, "r") as f:
        code_content = f.read()

    desc_path = os.path.join("descriptions", f"{block_id}.md")
    with open(desc_path, "r") as f:
        desc_content = f.read()

    formula_path = os.path.join("formulas", f"{block_id}.tex")
    with open(formula_path, "r") as f:
        formula_content = f.read()

    title = {
        "block01": "Hadamard Superposition",
        "block02": "Bell State",
        "block03": "Swap Test",
        "block04": "Quantum Teleportation",
        "block05": "GHZ State",
        "block06": "W State",
        "block07": "Grover’s Oracle (One Solution)",
        "block08": "Grover’s Diffusion Operator",
        "block09": "Phase Kickback (Controlled Phase)",
        "block10": "Deutsch–Jozsa Algorithm",
        "block11": "Quantum Fourier Transform (QFT)",
        "block12": "Inverse Quantum Fourier Transform (IQFT)",
        "block13": "Quantum Phase Estimation",
        "block14": "Time Evolution (Trotter)",
        "block15": "3-Qubit Bit-Flip Code",
        "block16": "Custom Native Gate (RXX)",
        "block17": "Initialize |0> & Measure",
        "block18": "Pauli-X Gate",
        "block19": "H → X → H (Interference)",
        "block20": "Z-Basis Measurement",
        "block21": "State Vector Visualization",
        "block22": "Biased Superposition (RY)",
        "block23": "Two Qubits |00>",
        "block24": "W State & Measure",
        "block25": "Bell State with Mid-Circuit Measurement",
    }.get(block_id, block_id)

    BLOCKS.append({
        "id": block_id,
        "title": title,
        "code": code_content,
        "description": desc_content,
        "formula": formula_content,
    })


def main():
    clear()
    put_text("# QubitQuest Tutorial")
    put_text("Select a code block to explore:")
    for blk in BLOCKS:
        put_buttons(
            [blk["title"]],
            onclick=[lambda b=blk: display_block(b)]
        )


def display_block(block):
    clear()
    put_text(f"## {block['title']}\n")
    put_text(block["description"])
    put_html(f"<p><b>Mathematical Representation:</b><br>\\[{block['formula']}\\]</p>")
    put_code(block["code"], language="python")

    put_buttons(
        ["Run on IonQ QPU", "Back to List"],
        onclick=[
            lambda b=block: run_on_qpu(b),
            lambda: main()
        ]
    )


def run_on_qpu(block):
    clear()
    put_text(f"### Running {block['title']} on IonQ QPU with 10 shots…\n")

    # Execute block code in a shared namespace so imports stick
    namespace = {}
    exec(block["code"], namespace, namespace)

    build = namespace.get("build")
    if not callable(build):
        put_text("Error: build() function not found in block code.")
        put_buttons(["Back to List"], onclick=[lambda: main()])
        return

    circuit = build()

    try:
        # Reduced from 100 to 10 shots
        counts = submit_to_ionq(circuit, shots=10)
    except Exception as e:
        put_text(f"Error during QPU submission: {e}")
        put_buttons(["Back to List"], onclick=[lambda: main()])
        return

    put_text("**Results (bitstring → counts):**")
    for bitstr, cnt in counts.items():
        put_text(f"{bitstr}: {cnt}")

    update_counter.increment_run(block["id"])
    total = run_counter.run_counts.get(block["id"], 0)
    put_text(f"\n**Total runs for '{block['title']}':** {total}\n")

    put_buttons(
        ["Back to List"],
        onclick=[lambda: main()]
    )


if __name__ == "__main__":
    start_server(main, port=8080, cdn=True)


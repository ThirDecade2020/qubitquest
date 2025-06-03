# main.py

from pywebio import start_server
from pywebio.output import put_text, put_buttons, put_code, put_html, clear
import run_counter
import update_counter
from utils.executor import execute_code
import os

# Load metadata for all 25 blocks at startup
BLOCKS = []
for block_id in [
    "block01", "block02", "block03", "block04", "block05",
    "block06", "block07", "block08", "block09", "block10",
    "block11", "block12", "block13", "block14", "block15",
    "block16", "block17", "block18", "block19", "block20",
    "block21", "block22", "block23", "block24", "block25",
]:
    # Read Python code
    code_path = os.path.join("blocks", f"{block_id}.py")
    with open(code_path, "r") as f:
        code_content = f.read()

    # Read description (Markdown)
    desc_path = os.path.join("descriptions", f"{block_id}.md")
    with open(desc_path, "r") as f:
        desc_content = f.read()

    # Read LaTeX formula
    formula_path = os.path.join("formulas", f"{block_id}.tex")
    with open(formula_path, "r") as f:
        formula_content = f.read()

    # Assign a human-readable title based on block_id
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
    """
    Main entry point for QubitQuest tutorial.
    Displays a list of available code blocks for the user to select.
    """
    clear()
    put_text("# QubitQuest Tutorial")
    put_text("Select a code block to explore:")

    # Render a button for each block in BLOCKS
    for blk in BLOCKS:
        put_buttons(
            [blk["title"]],
            onclick=[lambda b=blk: display_block(b)]
        )


def display_block(block):
    """
    Displays the selected block’s code, description, formula,
    and provides options to run locally or go back.
    """
    clear()
    # Block title
    put_text(f"## {block['title']}\n")

    # Description (rendered as plain text)
    put_text(block["description"])

    # Mathematical formula rendered with MathJax
    put_html(
        f"<p><b>Mathematical Representation:</b><br>\\[{block['formula']}\\]</p>"
    )

    # Show the Python code for this block
    put_code(block["code"], language="python")

    # Buttons: Run Locally or Back to List
    put_buttons(
        ["Run Locally", "Back to List"],
        onclick=[
            lambda b=block: run_locally(b),
            lambda: main()
        ]
    )


def run_locally(block):
    """
    Executes the block’s Python code locally using executor.execute_code(),
    displays the output, and updates the run counter.
    """
    clear()
    put_text(f"### Running {block['title']} Locally...\n")

    # Execute the user’s code and capture output
    result = execute_code(block["code"])

    # Display the execution result
    put_text("**Output:**")
    put_text(result)

    # Increment and show the run count
    update_counter.increment_run(block["id"])
    count = run_counter.run_counts.get(block["id"], 0)
    put_text(f"\n**Run count for '{block['title']}':** {count}\n")

    # Offer a “Back to List” button after execution
    put_buttons(
        ["Back to List"],
        onclick=[lambda: main()]
    )


if __name__ == "__main__":
    # Start the PyWebIO server on port 8080 with MathJax enabled via CDN
    start_server(main, port=8080, cdn=True)


import run_counter

def increment_run(block_id):
    if block_id in run_counter.run_counts:
        run_counter.run_counts[block_id] += 1
        save_run_counts()

def save_run_counts():
    with open("run_counter.py", "w") as f:
        f.write("# Auto-updated run count database\n")
        f.write(f"run_counts = {repr(run_counter.run_counts)}\n")
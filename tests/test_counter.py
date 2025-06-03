import run_counter, update_counter

def test_increment():
    block_id = "block01"
    before = run_counter.run_counts[block_id]
    update_counter.increment_run(block_id)
    after = run_counter.run_counts[block_id]
    assert after == before + 1
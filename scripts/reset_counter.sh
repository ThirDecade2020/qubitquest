#!/bin/bash
# Reset run counts to zero
cat > run_counter.py <<EOL
run_counts = {
    "block01": 0,
    "block02": 0
}
EOL
echo "Run counters reset."
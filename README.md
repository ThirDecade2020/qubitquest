# QubitQuest

QubitQuest is a Python-only, NES-themed educational web application that teaches quantum computing through progressively complex code blocks. Users can run code locally or on IonQ's real quantum hardware via AWS Braket.

## Setup

1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Configure AWS credentials (`aws configure`) with access to IonQ on Braket.
4. Run the landing page:
   ```
   cd qubitquest
   bash scripts/run_server.sh
   ```

## Usage

- Navigate to `http://localhost:8080` in your browser.
- Click "Begin QubitQuest" to enter the tutorial.
- Select a code block, view the explanation and formula, and run the code.

## Testing

Run tests using:
```
bash scripts/test.sh
```
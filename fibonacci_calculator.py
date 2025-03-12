import logging
from typing import List

# Configure structured logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def get_fibonacci(n: int) -> List[int]:
    """
    Generate the Fibonacci sequence up to the nth number.
    
    - Uses an iterative approach for efficiency (O(n) time, O(1) space).
    - Validates input to ensure correctness and prevent unexpected errors.
    
    :param n: The number of Fibonacci numbers to generate.
    :return: A list containing the first 'n' Fibonacci numbers.
    :raises ValueError: If input is not a non-negative integer.
    """
    
    # Input validation: ensure 'n' is a non-negative integer
    if not isinstance(n, int) or n < 0:
        logging.error("Invalid input: n must be a non-negative integer")
        raise ValueError("Input must be a non-negative integer")

    # Handle base cases explicitly
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the Fibonacci sequence
    sequence = [0, 1]  # First two numbers of the sequence
    
    # Iteratively compute the next Fibonacci numbers
    for _ in range(2, n):
        next_value = sequence[-1] + sequence[-2]  # Sum of last two numbers
        sequence.append(next_value)

    return sequence


if __name__ == "__main__":
    """ Main execution block for safe script execution. """
    
    try:
        num = 35  # Change this value to generate a different sequence length
        logging.info(f"Generating Fibonacci sequence for n={num}")
        
        # Compute Fibonacci sequence
        sequence = get_fibonacci(num)

        # Print the sequence in a structured format
        for idx, value in enumerate(sequence):
            print(f"Fib[{idx}]: {value}")

        logging.info("Fibonacci sequence generation completed successfully.")

    except ValueError as e:
        logging.exception("An error occurred while computing the Fibonacci sequence.")

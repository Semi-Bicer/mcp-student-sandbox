"""Data processing module with tax/fee calculations."""

from typing import List, Union
import logging
from pathlib import Path

# Configuration constants
TAX_MULTIPLIER = 1.15  # 15% increase factor
LOG_FILE_PATH = Path("log.txt")

# Set up logging
logging.basicConfig(
    filename=str(LOG_FILE_PATH),
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)


def calculate_totals(values: List[Union[int, float]]) -> List[float]:
    """
    Calculate adjusted total for each value.

    Args:
        values: List of numeric values to process

    Returns:
        List of calculated totals (original value * TAX_MULTIPLIER)

    Raises:
        ValueError: If values list is empty or contains non-numeric values
        TypeError: If values is not iterable
    """
    if not values:
        raise ValueError("Input values cannot be empty")

    results = []
    try:
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError(f"Expected numeric value, got {type(value).__name__}")
            total = value * TAX_MULTIPLIER
            results.append(total)
    except (TypeError, ValueError) as e:
        logging.error(f"Error processing values: {e}")
        raise

    return results


def format_totals(totals: List[float]) -> List[str]:
    """Format numeric totals as strings for display."""
    return [f"Total: {total:.2f}" for total in totals]


def log_results(totals: List[float]) -> None:
    """Log processing results to file."""
    try:
        logging.info(f"Processed {len(totals)} values: {totals}")
    except Exception as e:
        logging.error(f"Failed to log results: {e}")


def process_data(values: List[Union[int, float]],
                 log: bool = True,
                 print_output: bool = False) -> List[float]:
    """
    Process numeric data by applying tax multiplier.

    Args:
        values: List of numeric values
        log: Whether to log results (default: True)
        print_output: Whether to print results (default: False)

    Returns:
        List of calculated totals
    """
    totals = calculate_totals(values)

    if log:
        log_results(totals)

    if print_output:
        formatted = format_totals(totals)
        for item in formatted:
            print(item)

    return totals

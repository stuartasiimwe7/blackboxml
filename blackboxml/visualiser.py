import json
import matplotlib.pyplot as plt
import os
from typing import Optional
import logging

logger = logging.getLogger("blackboxml")

def visualise_metrics(filepath: str, save_path: Optional[str] = None, show: bool = True) -> None:
    """
    Visualise training/validation metrics from a JSON file.

    Args:
        filepath (str): Path to the metrics JSON file.
        save_path (str, optional): Directory to save plots as image files. If None, plots are not saved.
        show (bool, optional): If True, display plots interactively. If False, do not display.

    The function will plot each metric (and its validation counterpart, if present) vs. epochs.
    If save_path is provided, each plot is saved as <metric>_vs_epochs.png in that directory.
    """
    try:
        with open(filepath, 'r') as f:
            metrics = json.load(f)
    except FileNotFoundError:
        logger.error(f"[BlackBoxML] Metrics file not found: {filepath}")
        return
    except json.JSONDecodeError:
        logger.error(f"[BlackBoxML] Metrics file is not valid JSON: {filepath}")
        return
    except Exception as e:
        logger.error(f"[BlackBoxML] Unexpected error reading metrics file: {e}")
        return

    try:
        epochs = range(1, len(next(iter(metrics.values()))) + 1)
    except Exception as e:
        logger.error(f"[BlackBoxML] Error parsing metrics: {e}")
        return

    if save_path:
        os.makedirs(save_path, exist_ok=True)

    for key in metrics:
        if 'val_' in key:  # plot validation metrics separately
            continue
        plt.figure()
        try:
            plt.plot(epochs, metrics[key], label=key)
            val_key = f"val_{key}"
            if val_key in metrics:
                plt.plot(epochs, metrics[val_key], label=val_key)
            plt.xlabel("Epochs")
            plt.ylabel(key)
            plt.title(f"{key} vs Epochs")
            plt.legend()
            plt.grid(True)
            if save_path:
                filename = os.path.join(save_path, f"{key}_vs_epochs.png")
                plt.savefig(filename)
                logger.info(f"[BlackBoxML] Saved plot: {filename}")
            if show:
                plt.show()
            else:
                plt.close()
        except Exception as e:
            logger.error(f"[BlackBoxML] Error plotting metric '{key}': {e}")

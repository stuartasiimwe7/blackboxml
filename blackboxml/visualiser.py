import json
import matplotlib.pyplot as plt

def visualise_metrics(filepath):
    with open(filepath, 'r') as f:
        metrics = json.load(f)

    epochs = range(1, len(next(iter(metrics.values()))) + 1)

    for key in metrics:
        if 'val_' in key:  #plot validation metrics separately
            continue
        plt.figure()
        plt.plot(epochs, metrics[key], label=key)
        val_key = f"val_{key}"
        if val_key in metrics:
            plt.plot(epochs, metrics[val_key], label=val_key)
        plt.xlabel("Epochs")
        plt.ylabel(key)
        plt.title(f"{key} vs Epochs")
        plt.legend()
        plt.grid(True)
        plt.show()

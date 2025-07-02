import os
import json
import datetime
from contextlib import AbstractContextManager
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar

def autopilot() -> None:
    """
    Automatically patches tf.keras.Model.fit() to log training metrics to a JSON file in blackboxml_logs/.
    After calling this function, every Keras model.fit() call will save metrics automatically.
    """
    try:
        import tensorflow.keras.models as models  # type: ignore
        original_fit: Callable = models.Model.fit

        def patched_fit(self: Any, *args: Any, **kwargs: Any) -> Any:
            """
            Replacement for Model.fit(). Logs metrics to blackboxml_logs/ after training.
            Args:
                self: The Keras model instance.
                *args: Positional arguments for fit().
                **kwargs: Keyword arguments for fit().
            Returns:
                The History object returned by the original fit().
            """
            print("[BlackBoxML] Auto-logging metrics from model.fit()")

            history = original_fit(self, *args, **kwargs)
            metrics = history.history

            os.makedirs("blackboxml_logs", exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"blackboxml_logs/metrics_{timestamp}.json"

            with open(filename, "w") as f:
                json.dump(metrics, f)

            print(f"[BlackBoxML] Metrics logged to {filename}")
            return history

        models.Model.fit = patched_fit
        print("[BlackBoxML] Patched model.fit() to log metrics.")

    except Exception as e:
        print(f"[BlackBoxML] Autopilot failed. Error: {e}")
        print("[BlackBoxML] Auto-logging disabled.")


class Tracker(AbstractContextManager):
    """
    Context manager for experiment tracking and logging in BlackBoxML.
    Provides a Keras callback to log experiment metadata and final logs to blackboxml_logs/.
    """
    def __init__(self, experiment_name: str, tags: Optional[List[str]] = None) -> None:
        """
        Args:
            experiment_name (str): Name of the experiment.
            tags (list, optional): List of tags for the experiment.
        """
        self.experiment_name: str = experiment_name
        self.tags: List[str] = tags or []
        self.start_time: datetime.datetime = datetime.datetime.now()
        self.filename: str = ""  # Always a string

    def __enter__(self) -> "Tracker":
        print(f"[BlackBoxML] Starting experiment: {self.experiment_name}")
        return self

    def get_keras_callback(self) -> Any:
        """
        Returns a Keras Callback that logs experiment metadata and final logs to blackboxml_logs/.
        Returns:
            keras.callbacks.Callback: The BlackBoxML callback for logging.
        """
        from tensorflow.keras.callbacks import Callback  # type: ignore

        class BlackBoxMLCallback(Callback):
            def on_train_end(inner_self: Any, logs: Optional[Dict[str, Any]] = None) -> None:
                logs = logs or {}
                log_data = {
                    "experiment": self.experiment_name,
                    "tags": self.tags,
                    "timestamp": self.start_time.strftime("%Y%m%d_%H%M%S"),
                    "final_logs": logs
                }

                os.makedirs("blackboxml_logs", exist_ok=True)
                self.filename = f"blackboxml_logs/metrics_{self.start_time.strftime('%Y%m%d_%H%M%S')}.json"
                with open(self.filename, "w") as f:
                    json.dump(log_data, f)
                print(f"[BlackBoxML] Final logs saved to {self.filename}")

        return BlackBoxMLCallback()

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Any) -> None:
        print(f"[BlackBoxML] Finished experiment: {self.experiment_name}")
        if exc_type:
            print(f"[BlackBoxML] Error during experiment: {exc_value}")
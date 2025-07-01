import os
import json
import datetime
from contextlib import AbstractContextManager

def autopilot():
    try:
        import tensorflow.keras.models as models  # type: ignore
        original_fit = models.Model.fit

        def patched_fit(self, *args, **kwargs):
            print("[Traceml] Auto-logging metrics from model.fit()")

            history = original_fit(self, *args, **kwargs)
            metrics = history.history

            os.makedirs("blackbox_logs", exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"blackbox_logs/metrics_{timestamp}.json"

            with open(filename, "w") as f:
                json.dump(metrics, f)

            print(f"[Traceml] Metrics logged to {filename}")
            return history

        models.Model.fit = patched_fit
        print("[Traceml] Patched model.fit() to log metrics.")

    except Exception as e:
        print(f"[Traceml] Autopilot failed. Error: {e}")
        print("[Traceml] Auto-logging disabled.")


class Tracker(AbstractContextManager):
    def __init__(self, experiment_name, tags=None):
        self.experiment_name = experiment_name
        self.tags = tags or []
        self.start_time = datetime.datetime.now()
        self.filename = None

    def __enter__(self):
        print(f"[Traceml] Starting experiment: {self.experiment_name}")
        return self

    def get_keras_callback(self):
        from tensorflow.keras.callbacks import Callback  # type: ignore

        class TracemlCallback(Callback):
            def on_train_end(inner_self, logs=None):
                logs = logs or {}
                log_data = {
                    "experiment": self.experiment_name,
                    "tags": self.tags,
                    "timestamp": self.start_time.strftime("%Y%m%d_%H%M%S"),
                    "final_logs": logs
                }

                os.makedirs("blackbox_logs", exist_ok=True)
                self.filename = f"blackbox_logs/metrics_{self.start_time.strftime('%Y%m%d_%H%M%S')}.json"
                with open(self.filename, "w") as f:
                    json.dump(log_data, f)
                print(f"[Traceml] Final logs saved to {self.filename}")

        return TracemlCallback()

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"[Traceml] Finished experiment: {self.experiment_name}")
        if exc_type:
            print(f"[Traceml] Error during experiment: {exc_value}")
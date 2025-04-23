import os
import sys
import json
import datetime

def autopilot():
    try:
        import tensorflow.keras.models as models # type: ignore #fix this issue
        original_fit = models.Model.fit

        def patched_fit(self, *args, **kwargs):
            print("[BlackBoxML] Auto-logging metrics from model.fit()")

            history = original_fit(self, *args, **kwargs)

            metrics = history.history
            os.makedirs("blackbox_logs", exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"blackbox_logs/metrics_{timestamp}.json"

            with open(filename, "w") as f:
                json.dump(metrics, f)
            print(f"[BlackBoxML] Metrics logged to {filename}")
            
            return history
        
        models.Model.fit = patched_fit
        print("[BlackBoxML] Patched model.fit() to log metrics.")

    except Exception as e:
        print(f"[BlackBoxML] Autopilot failed:Error: {e}")
        print("[BlackBoxML]  Auto-logging disabled.")

        return
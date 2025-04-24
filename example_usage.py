from blackboxml import autopilot, Tracker  # Updated import
import tensorflow as tf
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D  # type: ignore
from tensorflow.keras.datasets import mnist  # type: ignore
from tensorflow.keras.utils import to_categorical  # type: ignore
from blackboxml.visualiser import visualise_metrics  # Updated import

# Patch model.fit() (optional if autopilot() is auto-run in __init__.py)
autopilot()

# Load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Define model
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Log metrics to a file using the Tracker context manager
with Tracker("mnist_cnn", tags=["keras", "mnist", "cnn"]) as tracker:
    history = model.fit(
        x_train, y_train,
        validation_data=(x_test, y_test),
        epochs=2,
        batch_size=64,
        callbacks=[tracker.get_keras_callback()]
    )

'''
Expected Result: 
You should see a .json file saved in blackbox_logs/ 
with training & validation metrics — automatically.
'''

# After training, visualise the most recent metrics
import glob
log_files = sorted(glob.glob("blackbox_logs/metrics_*.json"), reverse=True)
if log_files:
    visualise_metrics(log_files[0])
else:
    print("No metrics log files found.")

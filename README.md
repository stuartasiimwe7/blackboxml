# 📦 BlackBoxML
 A Python package that auto-patches tf.keras.Model.fit() to log training metrics automatically, with zero changes to your code workflow, even if you forgot to set it up.

## Why?

We’ve all been there:
- You train a model in Colab or Jupyter
- It takes 10+ hours
- You forget to log the `training_loss` or `validation_loss` in the process
- Now you want to plot training and validation loss over epochs, 
- BUT can't because you forgot to log & plot them during training!

**BlackBoxML** has got your back!
Whether you're building CNNs, Transformers, or experimental models, BlackBoxML ensures you never lose your training history again.

No setup overhead.
No excuses.
Just pure productivity.
Just import and forget it.

## Project Structure

```
blackboxml/
├── blackboxml/
│   ├── __init__.py
│   ├── autopilot.py
│   ├── visualiser.py
├── setup.py
├── README.md
├── LICENSE
```

## Installation

To get started with **BlackBoxML**, follow these steps to set up your environment and install the package:

### Step 1: Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```

### Step 3: Install BlackBoxML

Once the virtual environment is activated, install the package using pip:

```bash
pip install blackboxml
```

And now you aree all set! 

## 🧩 How It Works

BlackBoxML integrates seamlessly into your workflow by patching `model.fit()` to log metrics automatically. Here's how you can use it:

### Basic Usage

```python
from blackboxml import autopilot
import tensorflow as tf

# Patch model.fit() once
autopilot()

# Build your model as usual
model = tf.keras.Sequential([...])

model.compile(...)
model.fit(...)  # Metrics are logged automatically
```

### Advanced Usage with Experiment Tracking

For more advanced tracking, you can specify experiment names and tags:

```python
from blackboxml import autopilot

# Use autopilot with experiment details
with autopilot("mnist_cnn", tags=["keras", "cnn", "mnist"]) as tracker:
    model.fit(..., callbacks=[tracker.get_keras_callback()])
```

This approach allows you to organize and tag your experiments for better tracking and analysis.

### 📊 Visualizing Metrics

After training, you can visualize the logged metrics using the `visualiser` module:

```python
from blackboxml.visualiser import visualise_metrics

# Visualize after training
visualise_metrics("blackbox_logs/metrics_20250424_221132.json")
```

This will generate plots for training and validation metrics, helping you analyze your model's performance effortlessly.

## Output

After training your model, **BlackBoxML** will automatically generate a log file containing all the recorded metrics. Here's an example of the output directory structure:

```
blackbox_logs/
└── metrics_YYYYMMDD_HHMMSS.json
```

Each log file is timestamped for easy identification and contains metrics such as training loss, validation loss, accuracy, and any other metrics tracked during training.
### Sample Metrics File

```json
{
    "accuracy": [0.95, 0.98],
    "loss": [0.1, 0.05],
    "val_accuracy": [0.96, 0.97],
    "val_loss": [0.08, 0.06]
}
```
## Why BlackBoxML?

- **Save Time**: No more rewriting callbacks for every project.
- **Increase Reproducibility**: Metrics stored automatically for experiment comparisons.
- **Focus on Research, Not Bookkeeping**: Let BlackBoxML handle the boring stuff.

## Contributing

We welcome contributions of all kinds! Whether it's reporting a bug, suggesting a feature, improving documentation, or submitting a pull request, your help is greatly appreciated. 

Please see our [Contributing Guidelines](/.githubCONTRIBUTING.md) for more information on how to get started. Together, we can make **BlackBoxML** even better!

To report a bug, please use our [Bug Report Template](/.github/ISSUE_TEMPLATE/bug_report.md). This will help us address issues more efficiently.

To suggest a new feature or enhancement, please use our [Feature Request Template](./.github/ISSUE_TEMPLATE/feature_request.md). Your ideas and feedback are invaluable in improving **BlackBoxML**.

We take security seriously and strive to ensure that **BlackBoxML** is safe to use. If you discover any security vulnerabilities or have concerns, please report them to us immediately by creating an issue or contacting us directly. For more details, refer to our [Security Policy](/.github/SECURITY.md).

We are committed to fostering an open and welcoming environment for everyone. By participating in this project, you agree to abide by our [Code of Conduct](/.github/CODE_OF_CONDUCT.md). Please read it to understand the standards we expect from our community members.

## License

This project is licensed under the Apache License 2.0. You are free to use, modify, and distribute this software, provided that you comply with the terms of the license. For more details, see the [LICENSE](./LICENSE) file.

## Author

Built by [Stuart Asiimwe](https://www.linkedin.com/in/stuartasiimwe/)
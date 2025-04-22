# blackboxml
 A Python package that auto-patches tf.keras.Model.fit() to log training metrics automatically, with zero changes to your code workflow, even if you forgot to set it up.

## Why?

We’ve all been there:
- You train a model in Colab or Jupyter
- It takes 10+ hours
- You forget to log the `training_loss` over `validation_loss` in the process
- Now you want to plot training and validation loss over epochs

**BlackBoxML** has got your back!

## Project Structure

```
blackboxml/
├── __init__.py
├── autopilot.py
├── visualizer.py         # (optional, for visualizations)
├── utils.py              # (optional, for helper functions)
├── logs/                 # where logs will be stored
└── README.md
setup.py
LICENSE
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

You're all set! 🎉

## Usage

```python
import blackboxml  # Auto-patches keras.Model.fit()

# Then use your normal training code:
model.fit(...)
```

It will automatically log:

- Training & validation loss
- Accuracy
- All metrics in `.json` format in `./blackbox_logs/`

## Output

Example file structure:

```
blackbox_logs/
└── metrics_20250420_134513.json
```

🎯 No changes to your training loop. Just import and forget it.
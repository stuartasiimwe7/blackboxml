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

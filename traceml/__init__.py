import warnings

print("[DEPRECATION WARNING] The 'blackboxml' package is deprecated and will be renamed to 'traceml'. Please update your dependencies and imports to use 'traceml' instead. This package will no longer be maintained under the old name.\nTo install the new package, run: pip install traceml")
warnings.warn(
    "The 'blackboxml' package is deprecated and will be renamed to 'traceml'. Please install and use 'traceml' instead. To install, run: pip install traceml. See the documentation for migration instructions.",
    DeprecationWarning,
    stacklevel=2
)

from .autopilot import autopilot, Tracker

# Patch model.fit when imported
autopilot()
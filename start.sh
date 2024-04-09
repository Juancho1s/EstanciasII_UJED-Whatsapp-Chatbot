#!/bin/bash

# Exit early on errors
set -eu

# Python buffers stdout. Without this, you won't see what you "print" in the Activity logs
export PYTHONUNBUFFERED=true

# Install the requrements
python3 -m pip install -r requirements.txt

# Run a server
python3 ./src/app.py
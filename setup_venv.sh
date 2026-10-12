#!/bin/bash

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies (if requirements.txt exists)
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

echo "Virtual environment ready!"

# then run: source setup_venv.sh 
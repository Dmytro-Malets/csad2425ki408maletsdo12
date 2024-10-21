#!/bin/bash

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/ --cov=src --cov-report=html

# Create artifacts directory
mkdir -p artifacts

# Copy binaries and test reports
cp -r htmlcov artifacts/test-coverage
cp -r src/*.py artifacts/

# Deactivate virtual environment
deactivate
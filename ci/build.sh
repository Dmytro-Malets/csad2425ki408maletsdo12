#!/bin/bash

# Exit on any error
set -e

echo "Starting build process..."

# Check if running in CI environment
if [ -z "$CI" ]; then
    # Create virtual environment if not in CI
    echo "Creating virtual environment..."
    python -m venv venv
    source venv/bin/activate
else
    echo "Running in CI environment, skipping venv creation..."
fi

# Install dependencies
echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run tests with coverage
echo "Running tests..."
python -m pytest tests/ --cov=src --cov-report=html --cov-report=term-missing

# Create artifacts directory
echo "Creating artifacts..."
mkdir -p artifacts/src

# Copy binaries and test reports
cp -r htmlcov artifacts/test-coverage
cp -r src/*.py artifacts/src/

# Copy additional project files
cp requirements.txt artifacts/
cp README.md artifacts/ 2>/dev/null || echo "No README.md found"

# Create version file
echo "Build date: $(date)" > artifacts/build-info.txt
echo "Git commit: $(git rev-parse HEAD)" >> artifacts/build-info.txt

if [ -z "$CI" ]; then
    # Deactivate virtual environment if not in CI
    deactivate
fi

echo "Build completed successfully!"
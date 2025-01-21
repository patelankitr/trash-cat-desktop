#!/bin/bash

# Set script to exit on any error
set -e

# Define report file name and test directory
REPORT_NAME="test_report.html"
TEST_DIR="E:/D Folder/Trash Cat Desktop/app/test_play_trash_cat.py"  # Path with spaces

# Step 1: Install required dependencies
echo "Installing pytest and pytest-html..."
pip install --upgrade pytest pytest-html

# Step 2: Run pytest and generate HTML report
echo "Running tests and generating HTML report..."
pytest "$TEST_DIR" --html="$REPORT_NAME" --self-contained-html

# Step 3: Confirm report generation
if [ -f "$REPORT_NAME" ]; then
    echo "HTML report generated successfully: $REPORT_NAME"
else
    echo "Failed to generate the HTML report."
    exit 1
fi

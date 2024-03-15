# Cognitive Tests Data Processing Suite: Serial Addition

This repository houses a suite of Python scripts designed to process cognitive performance test data, leveraging the Streamlit framework for an intuitive user interface. The scripts facilitate the transformation of raw text files into structured CSV formats, supporting both individual and batch processing with options for combined or separated outputs.

## Scripts Overview

1. **serialAddition_bulk_text_to_csv_zip.py**: Converts multiple text files into individual CSV files and packages them into a single ZIP file for download. Ideal for scenarios requiring separate data files for each test subject or session.

2. **serialAddition_bulk_text_to_single_csv.py**: Aggregates data from multiple text files into a single CSV file, appending each file's data into one comprehensive dataset. This script is perfect for users who need to consolidate data for batch analysis.

## Features

- **Batch Processing**: Supports processing of multiple files at once.
- **Flexible Output**: Choose between individual CSVs (zipped) or a single combined CSV file.
- **Streamlit Interface**: Provides an easy-to-use web interface for file uploads and data downloads.

## Installation

Ensure Python 3.x is installed on your system, then clone this repository and install the required dependencies:

```bash
git clone https://github.com/caddickzac/CognitiveTestsProcessors.git
cd CognitiveTestsProcessors
pip install pandas streamlit
```

Usage
Each script is designed as a Streamlit app. To run an app, navigate to the script's directory in your command line and execute the appropriate command:

For serialAddition_bulk_text_to_csv_zip.py:
```bash
streamlit run serialAddition_bulk_text_to_csv_zip.py
```


For serialAddition_bulk_text_to_single_csv.py:
```bash
streamlit run serialAddition_bulk_text_to_single_csv.py
```
Follow the on-screen instructions in the Streamlit interface to upload your text files and download the processed CSV data.

## Input File Format
- Predefined Headers: Each file should start with a set of predefined headers that correspond to the data fields expected by the script. These headers should match exactly with those expected by the scripts, including the correct order and spelling.
- Data Rows: Following the headers, each file should contain rows of data representing the cognitive test results and associated metadata. Each data field must be separated by a specific delimiter (e.g., comma, tab) as expected by the script.
- No Spaces in File Names: Ensure that the file names do not include spaces. Use underscores (_) or hyphens (-) as separators if necessary.



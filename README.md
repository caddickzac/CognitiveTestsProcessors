# Cognitive Performance Data Processing Suite

This repository is dedicated to processing raw data from various cognitive performance tests, including the Psychomotor Vigilance Task (PVT), Digit Symbol Substitution Test (DSST), and Serial Addition tests. Utilizing Python, Pandas, and the Streamlit framework, it offers a suite of scripts designed for an intuitive user interface, allowing for the efficient transformation of raw test outputs into structured CSV formats.

## Overview

Each script within this suite is tailored to a specific cognitive test, facilitating both individual and batch processing of test data. The scripts support various output options, including combined and separated outputs, providing flexibility for data analysis and research purposes.

- **PVT Processing Scripts**:
  - `pvt_bulk_text_to_csv_zip.py`: Packages multiple PVT test outputs into individual CSV files and zips them into a single file.
  - `pvt_bulk_text_to_single_csv.py`: Combines multiple PVT test outputs into a single CSV file.
- **DSST Processing Scripts**:
  - Scripts for processing DSST test data will follow a similar pattern, focusing on extracting, transforming, and consolidating test results.
- **Serial Addition Test Processing Scripts**:
  - `serialAddition_bulk_text_to_csv_zip.py`:  Packages multiple PVT test outputs into individual CSV files and zips them into a single file.
  - `serialAddition_bulk_text_to_single_csv.py`: Combines multiple PVT test outputs into a single CSV file.

## Installation

1. Ensure Python 3.x and pip are installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/caddickzac/CognitiveTestsProcessors.git
   cd CognitiveTestsProcessors
   ```

Install required dependencies:
```bash
pip install pandas streamlit
```

## Usage
Each script is designed to be run as a Streamlit app. To operate an app, navigate to the script's directory and run the appropriate command in your command line:
```bash
streamlit run script_name.py
```

Replace script_name.py with the name of the script you wish to run (e.g., pvt_bulk_text_to_csv_zip.py). Follow the on-screen instructions to upload your text files and download the processed data.

## Input File Format
Input files for each cognitive test must adhere to specific formatting guidelines, including predefined headers and data structure. Ensure that:
- Files do not contain spaces in their names or within data fields.
- The appropriate headers are present at the beginning of each file.
- Data rows follow directly after the headers, with fields separated by the expected delimiter.

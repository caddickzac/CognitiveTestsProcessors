# Cognitive Performance Data Processing Suite

This repository is dedicated to post-processing raw data from various cognitive performance tests within E-Prime, including the [Psychomotor Vigilance Task (PVT)](https://support.pstnet.com/hc/en-us/articles/360008697713-Psychomotor-Vigilance-Task-PVT-30113), [Digit Symbol Substitution Test (DSST)](https://support.pstnet.com/hc/en-us/articles/360007837614-Digit-Symbol-Substitution-Test-DSST-30114), and Serial Addition tests. Utilizing Python, Pandas, and the Streamlit framework, it offers a suite of scripts designed for an intuitive user interface, allowing for the efficient transformation of unprocessed test outputs into structured CSV formats.

## Screenshot of Application
![Application](https://github.com/caddickzac/CognitiveTestsProcessors/blob/main/AppScreenshot/CTP_Screenshot.png)

## Overview

Each script within this suite is tailored to a specific cognitive test, facilitating both individual and batch processing of test data. The scripts support various output options, including combined and separated outputs, providing flexibility for data analysis and research purposes.

### Main Streamlit Script
- `CognitiveTestsProcessors.py`: Script that runs Streamlit application. 

### Processing Scripts
- **PVT**:
  - `PVT_to_ZippedCSVs.py`: Packages multiple PVT test outputs into individual CSV files and zips them into a single file.
  - `PVT_to_CombinedCSV.py`: Combines multiple PVT test outputs into a single CSV file.
- **DSST**:
  - Scripts for processing DSST test data will follow a similar pattern, focusing on extracting, transforming, and consolidating test results.
- **Serial Addition Test**:
  - `serialAddition_to_ZippedCSVs.py`:  Packages multiple PVT test outputs into individual CSV files and zips them into a single file.
  - `serialAddition_to_CombinedCSV.py`: Combines multiple PVT test outputs into a single CSV file.

## Installation

1. Ensure Python 3 and pip are installed on your system. Additionally, the Python libraries Pandas and Streamlit are required.
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
Each of the processing scripts are designed to run within the main Streamlit app. To operate the app navigate to the main directory and run the following command in your command line:
```bash
streamlit run CognitiveTestsProcessors.py
```

Follow the on-screen instructions to upload your text files and download the processed data.

## Input File Format
Input files for each cognitive test must be text (.txt) files.

## Create a batch file to run program
1. Create text document on desktop
2. Enter code below, changing "[working directory]" to your local directory where the streamlit app is saved. 

```bash
@echo off
REM set working directory
cd [working directory]

REM Activate the virtual environment
call venv/Scripts/activate

REM Run the Streamlit app using the Python installation in the virtual environment
streamlit run CognitiveTestsProcessors.py

REM Pause command to keep the terminal open after the script runs (optional)
pause
```
3. Save and close text document.
4. Change file type from ".txt" to ".bat"

# Cognitive Tests Data Processing Suite

This repository houses a suite of Python scripts designed to process cognitive performance test data, leveraging the Streamlit framework for an intuitive user interface. The scripts facilitate the transformation of raw text files into structured CSV formats, supporting both individual and batch processing with options for combined or separated outputs.

## Scripts Overview

1. **pvt_bulk_text_to_csv_zip.py**: Converts multiple text files into individual CSV files and packages them into a single ZIP file for download. Ideal for scenarios requiring separate data files for each test subject or session.

2. **pvt_bulk_text_to_single_csv.py**: Aggregates data from multiple text files into a single CSV file, appending each file's data into one comprehensive dataset. This script is perfect for users who need to consolidate data for batch analysis.

## Features

- **Batch Processing**: Supports processing of multiple files at once.
- **Flexible Output**: Choose between individual CSVs (zipped) or a single combined CSV file.
- **Metadata Extraction**: Extracts and includes relevant metadata in the CSV outputs.
- **Streamlit Interface**: Provides an easy-to-use web interface for file uploads and data downloads.
- **Customizable Data Processing**: Easily adaptable scripts to accommodate different cognitive test data formats.

## Installation

Ensure Python 3.x is installed on your system, then clone this repository and install the required dependencies:

```bash
git clone https://github.com/caddickzac/CognitiveTestsProcessors.git
cd CognitiveTestsProcessors
pip install pandas streamlit
```

Usage
Each script is designed as a Streamlit app. To run an app, navigate to the script's directory in your command line and execute the appropriate command:

For pvt_bulk_text_to_csv_zip.py:

```bash
Copy code
streamlit run pvt_bulk_text_to_csv_zip.py
```
For pvt_bulk_text_to_single_csv.py:
```

bash
Copy code
streamlit run pvt_bulk_text_to_single_csv.py
Follow the on-screen instructions in the Streamlit interface to upload your text files and download the processed CSV data.

Input File Format
Input text files should conform to a specific format, detailed in each script's documentation. Typically, files should include a set of predefined headers followed by data rows corresponding to cognitive test results and metadata.

Contributing
Contributions are welcome! If you have suggestions for improving the scripts or extending their functionality, please feel free to fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thank you to all the contributors who have helped refine and enhance these scripts.
Gratitude to the cognitive science community for their invaluable input and feedback.

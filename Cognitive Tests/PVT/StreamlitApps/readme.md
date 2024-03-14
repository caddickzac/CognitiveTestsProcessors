# Cognitive Data Batch Processor to ZipCSV

This Python script, `CognitiveDataBatchProcessor_to_ZipCSV.py`, streamlines the processing of cognitive performance test data. It combines batch processing with a user-friendly Streamlit web interface, allowing users to upload multiple text files, process them, and download the results as a single zipped CSV file.

## Features

- **Batch Processing**: Processes multiple text files simultaneously.
- **Data Extraction**: Extracts essential metadata and performance data from each file.
- **Combined Output**: Consolidates data into a single zipped CSV file for download.
- **Streamlit Interface**: Offers a straightforward web interface for easy uploads and downloads.

## Installation

To set up and use the Cognitive Data Batch Processor:

1. **Clone the Repository**:

git clone https://github.com/yourusername/CognitiveTestsProcessors.git
cd CognitiveTestsProcessors


2. **Install Dependencies**:
Ensure Python 3.x is installed on your system. Then, install required packages:

pip install pandas streamlit

3. **Run Streamlit App**: Execute the command, replacing `scriptName.py` with your script's name:

streamlit run scriptName.py

Example:

streamlit run pvt_bulk_text_to_single_csv.py

4. **Use the App**: Streamlit will open your web browser to the app. Follow instructions to upload files and download the processed data.

## Input File Format

Ensure input text files are correctly formatted, including appropriate headers and data structure as specified in the script documentation.

## Contributing

Contributions to enhance functionality or fix issues are welcome. Fork the repository, make changes, and submit a pull request.

## License

This project is under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments

- Thanks to all contributors and the cognitive science community for valuable feedback.
- Everyone who contributed to this project.



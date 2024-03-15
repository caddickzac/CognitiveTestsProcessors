import streamlit as st

def main():
    st.title("Cognitive Tests Processors ")

    st.write("Python scripts for efficiently processing data from cognitive tests (PVT, DSST, and Serial Addition)")

    st.markdown("## Overview")
    st.markdown("Each script within this suite is tailored to a specific cognitive test, facilitating both individual and batch processing of test data. The scripts support various output options, including combined and separated outputs, providing flexibility for data analysis and research purposes.")

    st.markdown("## Processing Scripts")
    st.markdown("**PVT**:")
    st.markdown(" - `PVT_to_ZippedCSVs.py`: Packages multiple PVT test outputs into individual CSV files and zips them into a single file.")
    st.markdown(" - `PVT_to_CombinedCSV.py`: Combines multiple PVT test outputs into a single CSV file.")

    st.markdown("**DSST**:")
    st.markdown(" - Scripts for processing DSST test data will follow a similar pattern, focusing on extracting, transforming, and consolidating test results.")

    st.markdown("**Serial Addition Test**:")
    st.markdown(" - `serialAddition_to_ZippedCSVs.py`: Packages multiple PVT test outputs into individual CSV files and zips them into a single file.")
    st.markdown(" - `serialAddition_to_CombinedCSV.py`: Combines multiple PVT test outputs into a single CSV file.")

if __name__ == "__main__":
    main()

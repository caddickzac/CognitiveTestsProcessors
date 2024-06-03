import streamlit as st

def main():
    st.title("Cognitive Tests Processors ")

    st.write("Python scripts for efficiently processing data from cognitive tests (PVT, DSST, and Serial Addition)")

    st.markdown("## Overview")
    st.markdown("Each script within this suite is tailored to a specific E-Prime cognitive test.")

    st.markdown("## Processing Scripts")
    st.markdown("**DSST**:")
    st.markdown(" - `DSST_to_CombinedCSV.py`: Combines multiple PVT test outputs into a single CSV file.")

    st.markdown("**PVT**:")
    st.markdown(" - `PVT_to_CombinedCSV.py`: Combines multiple PVT test outputs into a single CSV file.")

    st.markdown("**Serial Addition Test**:")
    st.markdown(" - `serialAddition_to_CombinedCSV.py`: Combines multiple PVT test outputs into a single CSV file.")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import os
import zipfile
import tempfile

def extract_metadata_from_content(content_lines):
    """
    Extracts metadata from content lines based on specified headers.
    """
    headers = [
        "Experiment",
        "SessionDate",
        "SessionTime",
        "Subject",
        "Session",
        "DataFile.Basename",
        "RandomSeed",
        "Group",
        "Display.RefreshRate"
    ]
    
    meta_data = {}
    
    for line in content_lines:
        parts = line.split(": ", 1)
        if len(parts) == 2:
            key, value = parts
            if key in headers:
                meta_data[key] = value
    
    return meta_data

def extract_data_from_log_frames(content_lines, headers):
    """
    Extracts data from log frames based on specified headers.
    """
    data = []
    current_frame_data = {}
    for line in content_lines:
        if line.strip() == '*** LogFrame Start ***':
            if current_frame_data:  # Save previous frame data
                data.append(current_frame_data)
            current_frame_data = {}  # Reset for new frame
        elif line.strip() == '*** LogFrame End ***':
            continue  # Skip end marker
        else:
            for header in headers:
                header_with_colon = header + ":"
                if line.startswith(header_with_colon):
                    key = header  # Use header without colon as the key
                    value = line.replace(header_with_colon, "").strip()
                    current_frame_data[key] = value
                    break

    if current_frame_data:  # Add the last frame if not empty
        data.append(current_frame_data)

    return data

# Streamlit app
def main():
    st.title("PVT Output Conversion: Multiple Text Files to Zipped CSV Files")

    uploaded_files = st.file_uploader("Choose your files", type="txt", accept_multiple_files=True)

    if uploaded_files:
        # Create a temporary directory to hold the CSVs
        with tempfile.TemporaryDirectory() as tmpdirname:
            zip_name = os.path.join(tmpdirname, "processed_files.zip")

            for uploaded_file in uploaded_files:
                # Process each file
                base_name = os.path.splitext(uploaded_file.name)[0]
                output_file_name = f"{base_name}.csv"
                
                content = uploaded_file.getvalue().decode("utf-16").replace("\t", "").splitlines()
                
                # Your existing processing code here, for each uploaded file
                meta_data = extract_metadata_from_content(content)
                meta_data_df = pd.DataFrame([meta_data])
            
                headers = [
                    "TrialList", "Procedure", "Stimulus", "CorrectResponse", "Wait", "WaitDuration",
                    "WaitResponse", "TrialList.Cycle", "TrialList.Sample", "Running", "RandomWait.OnsetDelay",
                    "RandomWait.OnsetTime", "RandomWait.DurationError", "RandomWait.RTTime", "RandomWait.ACC",
                    "RandomWait.RT", "RandomWait.RESP", "RandomWait.CRESP", "RandomWait.OnsetToOnsetTime",
                    "RandomWait.DEVICE", "Stim.OnsetDelay", "Stim.OnsetTime", "Stim.DurationError", "Stim.RTTime",
                    "Stim.ACC", "Stim.RT", "Stim.RESP", "Stim.CRESP", "Stim.OnsetToOnsetTime", "Stim.DEVICE"
                ]

                log_frame_data = extract_data_from_log_frames(content, headers)
                df_log_frames = pd.DataFrame(log_frame_data)
                df_log_frames.insert(0, 'TrialNum', range(1, len(df_log_frames) + 1))

                repeated_meta_data_df = pd.concat([meta_data_df] * len(df_log_frames), ignore_index=True)
                final_df = pd.concat([repeated_meta_data_df, df_log_frames], axis=1)

                st.dataframe(final_df)

                csv_file_path = os.path.join(tmpdirname, f"{os.path.splitext(uploaded_file.name)[0]}.csv")
                
                # Save DataFrame to CSV
                final_df.to_csv(csv_file_path, index=False)
            
            # Zip all the CSV files in the temporary directory
            with zipfile.ZipFile(zip_name, 'w') as zipf:
                for file in os.listdir(tmpdirname):
                    file_path = os.path.join(tmpdirname, file)
                    zipf.write(file_path, arcname=file)

            with open(zip_name, 'rb') as f:
                st.download_button(label="Download All CSVs as ZIP",
                    data=f.read(),
                    file_name="processed_csvs.zip",
                    mime="application/zip")

if __name__ == "__main__":
    main()
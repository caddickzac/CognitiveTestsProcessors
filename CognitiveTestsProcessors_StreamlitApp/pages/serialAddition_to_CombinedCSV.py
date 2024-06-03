import streamlit as st
import pandas as pd
import os
import tempfile

def extract_metadata_from_content(content_lines, uploaded_file_name):
    """
    Extracts metadata from content lines based on specified headers and includes the uploaded file name.
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
    
    meta_data = {"DataFile.Uploadedname": uploaded_file_name}  # Add uploaded file name to metadata
    
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

# Streamlit app main function
def main():
    st.title("Serial Addition Output Conversion: Multiple Text Files to Single CSV File")

    uploaded_files = st.file_uploader("Choose your files", accept_multiple_files=True, type="txt")

    if uploaded_files:
        all_data_frames = []
        file_counter = 0

        for uploaded_file in uploaded_files:
            content = uploaded_file.getvalue().decode("utf-16").replace("\t", "").splitlines()

            if not content:  # Check if the file is empty
                st.warning(f"File {uploaded_file.name} is empty and will be skipped.")
                continue  # Skip the rest of the loop for this file
            
            file_counter += 1  # Increment counter for each new file

            # Your processing code to extract metadata and log frame data
            meta_data = extract_metadata_from_content(content, uploaded_file.name)
            meta_data_df = pd.DataFrame([meta_data])

            headers = [
                    "TrialList", "Procedure", "Stimulus1", "Stimulus2", "CorrectResponse", "TrialList.Cycle", 
                    "TrialList.Sample", "Running",
                    "ProblemSlide.OnsetDelay", "ProblemSlide.OnsetTime", "ProblemSlide.DurationError", 
                    "ProblemSlide.RTTime", "ProblemSlide.ACC", "ProblemSlide.RT", "ProblemSlide.RESP",
                    "ProblemSlide.CRESP", "ProblemSlide.OnsetToOnsetTime", "ProblemSlide.DEVICE", 
                    "TestDuration",
                ]

            log_frame_data = extract_data_from_log_frames(content, headers)
            df_log_frames = pd.DataFrame(log_frame_data)
            
            # Add the "TxtFileNum" column as the leftmost column
            df_log_frames.insert(0, 'TxtFileNum', file_counter)
            
            # Then add "TrialNum" column
            df_log_frames.insert(1, 'TrialNum', range(1, len(df_log_frames) + 1))

            # Combine metadata and log frame data
            repeated_meta_data_df = pd.concat([meta_data_df] * len(df_log_frames), ignore_index=True)
            final_df = pd.concat([repeated_meta_data_df, df_log_frames], axis=1)

            # Append the DataFrame for this file to the list
            all_data_frames.append(final_df)

        if all_data_frames:  # Check if there's any data to combine
            # Combine all individual file DataFrames into one
            combined_df = pd.concat(all_data_frames, ignore_index=True)

            # Reorder columns to place "DataFile.Uploadedname" before "DataFile.Basename"
            columns = combined_df.columns.tolist()
            columns.insert(columns.index("DataFile.Basename"), columns.pop(columns.index("DataFile.Uploadedname")))
            combined_df = combined_df[columns]

            # Show and provide download for the combined DataFrame
            st.dataframe(combined_df)
            combined_csv = combined_df.to_csv(index=False).encode('utf-8')
            st.download_button(label="Download Combined CSV",
                               data=combined_csv,
                               file_name="combined_processed_data.csv",
                               mime='text/csv')
        else:
            st.warning("No data to process. Please upload valid files.")

if __name__ == "__main__":
    main()

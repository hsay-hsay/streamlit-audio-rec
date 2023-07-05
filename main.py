import streamlit as st
from st_custom_components import st_audiorec
import os
import wave
import speech_recognition as sr

folder_path = 'audio_files'  
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def audiorec_demo_app():
    wav_audio_data = st_audiorec() # tadaaaa! yes, that's it! :D
    # add some spacing and informative messages
    col_info, col_space = st.columns([0.57, 0.43])
    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            # st.audio(wav_audio_data, format='audio/wav')
            file_path = os.path.join(folder_path, '1.wav')
            with open(file_path, 'wb') as file:
                file.write(wav_audio_data)
                st.warning(f"Audio file saved at: {os.path.abspath(file_path)}")

audiorec_demo_app()

# saved_file = wave.open(os.path.join(folder_path, '1.wav'))

# if saved_file is not None:
#     st.audio(saved_file, format='audio/wav')


file_path = '/app/streamlit-audio-rec/audio_files/1.wav'  
    # Replace with the actual file path

    # Check if the file exists before proceeding
    if os.path.exists(file_path):  
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            text=""
            audio = recognizer.record(source)  # Read the entire audio file
            # Use the recognizer to convert audio to text
            text = recognizer.recognize_google(audio)
            st.write("You said:",text)
            print("You said:", text)
            question = text
            # Additional code to utilize the 'text' variable as needed
    else:
        print(f"File '{file_path}' does not exist. Cannot perform audio recognition.")

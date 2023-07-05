import streamlit as st
from st_custom_components import st_audiorec
import os
# import speech_recognition as sr

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
            st.audio(wav_audio_data, format='audio/wav')
            file_path = os.path.join(folder_path, '1.wav')
            with open(file_path, 'wb') as file:
                file.write(wav_audio_data)
            print(f"Audio file saved at: {file_path}")
            
audiorec_demo_app()
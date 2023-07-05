import streamlit as st
from st_custom_components import st_audiorec

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # display audio data as received on the backend
    # st.audio(wav_audio_data, format='audio/wav')
    pass
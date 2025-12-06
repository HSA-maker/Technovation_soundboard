import streamlit as st

def button_click(col):
    speech_container.audio(speechArr[col], format='audio/mpeg')
st.title("Soundbpard App")
st.subheader(
    "Click on the perosn to hear a famous speech by tht person."
)

Names = ['Martin Luther king', 'Kamala Harris', 'Ketanji Brown Jackson']
imgArr = ['assets/mlk.jpg', 'assets/kamalaharris.png', 'assets/brownjackson.jpg' ]
speechArr = ['assets/mlk.mp3', 'assets/kamala.mp3', 'assets/brownjackson.mp3' ]
cols = st.columns(3)

for c in range(0, len(Names)):
    cols[c].image(imgArr[c])
    cols[c].button(Names[c], on_click=button_click, args=[c,], use_container_width=True)

speech_container= st.container(border=True)
speech_container.write('Audio:')
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#load assets
lottie_coding = load_lottieur("https://assets6.lottiefiles.com/packages/lf20_jvxwtdtp.json")

# header section
st.subheader("Hi, I'm Annie :two_hearts:")
st.title("A third-year student studying at UofT.")
st.write("I am in the field of public health and hope to pursue a career in strive for better access to healthcare for all individuals.")
st.write("[Follow Me >](https://www.instagram.com/anniewngg/)")

# what i do 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Fun Facts About Me")
        st.write("##")
        st.write(
            """
            - I'm an only child
            - INFP mbti
            - I love going to the gym
            - Taro mochi is my favourite dessert
            - I have a cat named sesame
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#tell me about yourself
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Tell Me More About You!")
        st.write("##")

import datetime
import streamlit as st

d = st.date_input(
    "When\'s your birthday?",
    datetime.date(2002, 10, 18))
st.write('Your birthday is:', d)


import streamlit as st

genre = st.radio(
    "How are you feeling today?",
    ('On top of the world', 'Mid', 'Down in the dumps'))

if genre == 'On top of the world':
    st.write('You selected On top of the world!')
else:
    st.write("You didn\'t select On top of the world ):")
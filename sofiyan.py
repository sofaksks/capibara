from PIL import Image
import requests 
import streamlit as st
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="My Webpage",page_icon=":tada:")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding="https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
img_contact_form=Image.open("images/capybara.webp")
img_lottie_animation=Image.open("images/capybara.webp")

st.write("Hellew")

with st.container():
    st.subheader("Hi, I am Sofiya :wave:")
    st.title("A student from Kazakhstan")
    st.write("I am in 9th grade, learning IT")
    st.write("[Learn more >](https://youtu.be/zTgQ_VnrP_s?si=K9o5zK4RuP52EDFn)")

with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("##")
        st.write(
            """
            On this video u can see a cool capybara, i love capybara,they are so chill, also i love dogs, i dont care what type, i love dogs. There is a link with dogs and puppys
            """
        )
        st.write("[Link>](https://youtu.be/pxn0wL_uSm4?si=mBTTpXdfaDMV62r7)")
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("integrate Lottie Animation Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more cool
            Tap the link for tutorial
            """
        )
        st.markdown("[Tutorial](https://youtu.be/TXSOitGoINE)")
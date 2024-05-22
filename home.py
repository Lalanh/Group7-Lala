import streamlit as st
import requests
from streamlit_lottie import st_lottie
import base64
import plotly.express as px
from PIL import Image 


def app():
    # Function to load Lottie animation from URL
    def load_lottie_url(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
        # Load Lottie animation for coding section
    lottie_coding_url = "https://lottie.host/09c5154e-938a-463a-944a-54f04f69a5ab/sIAiNjzV8v.json"
    lottie_coding = load_lottie_url(lottie_coding_url)
    with st.container():
    # Header Section
        st.title("Customer Segmentation Website")
        # Creating two columns layout
        left_column, right_column = st.columns(2)

        with right_column:
            
            st.markdown(
                """
                <style>
                .lottie-container {
                    display: flex;
                    justify-content: center;
                }
                </style>
                """, unsafe_allow_html=True
                 )
            st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
            st_lottie(lottie_coding, height=350, key="coding")

        with left_column:
            st.header("Business Problem")
            # st.write('A customer file can be considered an important part of a business or organization because it contains information about current and potential customers. To identify the right customer base, we will use available sales data and use analytics tools to explore it. But a business customer data is very large and diverse, and it takes a lot of time and effort to analyze and gain insights from such a huge data file.')
            st.markdown(
                """
                <style>
                .justified-text {
                    text-align: justify;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            # Văn bản cần căn đều hai bên
            st.markdown(
                """
                <div class="justified-text">
                A customer file can be considered an important part of a business or organization because it contains information about current and potential customers. To identify the right customer base, we will use available sales data and use analytics tools to explore it. But a business customer data is very large and diverse, and it takes a lot of time and effort to analyze and gain insights from such a huge data file.
                </div>
                """,
                unsafe_allow_html=True
            )

    # Introduce about myself:
    with st.container():
       
        line_length = 80  
        st.markdown(f"*{''.join(['_' for _ in range(line_length)])}*")
        
        
        left_column, right_column= st.columns(2)
        with left_column:
            st.header("Our Goals")
            st.write("##")
            st.markdown(
                """
                <style>
                .justified-text {
                    text-align: justify;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            # Văn bản cần căn đều hai bên
            st.markdown(
                """
                <div class="justified-text">
                Our goal is to process company data to be able to create customer classification information to identify potential customers for several company departments, such as sales department, marketing department, etc.
                </div>
                """,
                unsafe_allow_html=True
            )

            # Văn bản thứ hai cần căn đều hai bên
            st.markdown(
                """
                <div class="justified-text">
                By gathering customer information and analyzing their purchasing data over different time periods, we are able to grasp the attributes that influence the shopping behavior of individual customers.
                </div>
                """,
                unsafe_allow_html=True
            )


        with right_column:
            lottie_coding_url = "https://lottie.host/3088300b-6ef1-4a19-ad0a-fa4fb141d75e/H4PoeWE5YO.json"
            lottie_coding = load_lottie_url(lottie_coding_url)
            st.markdown(
                """
                <style>
                .lottie-container {
                    display: flex;
                    justify-content: center;
                }
                </style>
                """, unsafe_allow_html=True
                 )
            st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
            st_lottie(lottie_coding, height=350, key="hi")
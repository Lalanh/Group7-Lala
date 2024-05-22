import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import auth
import json
import requests


def app():
    def t():
        st.session_state.signedout = False
        st.session_state.main = False
        st.session_state.username = ''         
    st.text('Name: '+st.session_state.username)
    st.text('Email id: '+st.session_state.useremail)
    st.button('Sign out', on_click=t)
            

import streamlit as st
from streamlit_option_menu import option_menu
import os

import home, analytics, account, about, dataset

def app():

        with st.sidebar:        
            app = option_menu(
                menu_title='Main Menu',
                options=['Home','Dataset','Analytics','Account','About'],
                icons=['house-fill','bar-chart-fill', 'lightbulb','person-circle','info-circle-fill'],
                menu_icon='cast',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'white'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","text-align": "left", "margin":"0px", "--hover-color": "#f2f2f2"},
        "nav-link-selected": {"background-color": "lightgreen", "font-weight":"normal"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Analytics":
            analytics.app()
        if app == "Account":
            account.app()       
        if app == 'About':
            about.app()          
        if app == 'Dataset':
            dataset.app()          
          
             
         
         

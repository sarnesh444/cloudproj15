import streamlit as st
import streamlit.components.v1 as components

def l3():
    # embed streamlit docs in a streamlit app
    st.write("The dashboard has been built using Power BI, in order to view the dashboard, user has to sign in using their credentials, in order to do so launch app.powerbi.com in a new tab and refresh this page and sign-in.")
    components.iframe("https://app.powerbi.com/reportEmbed?reportId=5e7a1d22-2cb7-4349-9691-8d52580ce98b&autoAuth=true&ctid=f5222e6c-5fc6-48eb-8f03-73db18203b63",1000,500)
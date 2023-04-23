from screens.Datascience_writeup import l5
from screens.File_Upload import l4
from screens.Dashboard import l3
from screens.Dynamic_Data_Pull import l2
from screens.Static_Data_Query import l1
import streamlit as st
from sec import make_hashes,check_hashes
import json
import sqlite3
import streamlit as st
from pathlib import Path
from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import _on_pages_changed, get_pages
import os
import logging

# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()

# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(fname TEXT,lname TEXT,email TEXT,username TEXT,password TEXT)')

def add_userdata(fname,lname,email,username,password):
    c.execute('INSERT INTO userstable(fname,lname,email,username,password) VALUES (?,?,?,?,?)',(fname,lname,email,username,password))
    conn.commit()

def login_user(username,password,email):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ? and email = ?',(username,password,email))
    data = c.fetchall()
    return data

# session state 
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def main():
    st.set_page_config(layout="wide")
    try:
        st.title("Cloud Final Project")
        st.write("Final Project Spring 2023 Group 15 : Venkata Naga Sai Rakesh Kamisetty M15214204, Sowmya Jonnalagadda M15195429, Sairam Talishetti M15171363")
        st.markdown(""" <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style> """, unsafe_allow_html=True)
        
        menu = ["Login", "Sign Up"] if not st.session_state["logged_in"] else ["Static Data Query", "Dynamic Data Pull", "Dashboard", "File Upload","Data Science Write Up","Logout"]
        choice = st.selectbox(
            "Select one option ▾",
            menu,
        )
        # Default choice
        if choice == "":
            st.subheader("Login")
        
        elif(choice == "Login"):
            st.write("-------")
            with st.form('Login'):
                username = st.text_input("User Name")
                email = st.text_input("Email Id", placeholder="email")
                password = st.text_input("Password", type="password")
                login_button = st.form_submit_button('Login')
                
            if login_button:
                create_usertable()
                hashed_pswd = make_hashes(password)
                result = login_user(username,check_hashes(password,hashed_pswd),email)
                if result:
                        st.session_state["logged_in"] = True
                        st.success("Logged In Sucessfully")
                        st.experimental_rerun()
                else:
                    st.warning("Incorrect Email Id/Password")

        elif(choice == "Sign Up"):
            st.write("-----")
            st.subheader("Create New Account")
            with st.form('Create New Account'):
                new_fname = st.text_input("First Name")
                new_lname = st.text_input("Last Name")
                new_email = st.text_input("Email")
                new_user = st.text_input("Username")
                new_password = st.text_input("Password",type='password')

                signup_button = st.form_submit_button('SignUp')
                
                if signup_button:
                    
                    if new_user == "":  # if user name empty then show the warnings
                        st.warning("Inavlid user name")
                    elif new_email == "":  # if email empty then show the warnings
                        st.warning("Invalid email id")
                    elif new_password == "":  # if password empty then show the warnings
                        st.warning("Invalid password")
                    else:
                        create_usertable()
                        add_userdata(new_fname,new_lname,new_email,new_user,make_hashes(new_password))
                        st.success("You have successfully created a valid Account")
                        st.info("Go to Login Menu to login")
        
        elif(choice == "Logout"):
            st.session_state["logged_in"] = False
            st.success("Logged Out Sucessfully")
            st.experimental_rerun()
        
        elif(choice == "Static Data Query"):
            st.write("-----")
            l1()

        elif(choice == "Dynamic Data Pull"):
            st.write("-----")
            l2()

        elif(choice == "Dashboard"):
            st.write("-----")
            l3()
        
        elif(choice == "File Upload"):
            st.write("-----")
            l4()
        elif(choice == "Data Science Write Up"):
            st.write("-----")
            l5()
        # # session state checking
        # if st.session_state["logged_in"]:
        #     show_all_pages()  # call all page
        #     hide_page(DEFAULT_PAGE.replace(".py", ""))  # hide first page
        #     switch_page(SECOND_PAGE_NAME)   # switch to second page
        # else:
        #     clear_all_but_first_page()  # clear all page but show first page
    except Exception as e:
        logging.error('This is an error message', e)


if __name__ == '__main__':
    main()

import streamlit as st
import os
import pandas as pd
from upload_local_to_adls import azure_upload_df

def save_uploadedfile(uploadedfile):
     if os.path.exists("./localdata"):
         pass
     else:
         os.mkdir("./localdata")
     with open(os.path.join("./localdata",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to localdata".format(uploadedfile.name))

def file_input():
    #accept household
    household_file = st.file_uploader("Upload Household File",type=['csv'])
    #accept product
    product_file = st.file_uploader("Upload Product File",type=['csv'])
    #accept transactions
    transactions_file = st.file_uploader("Upload Transactions File",type=['csv'])

    if household_file is not None:
        file_details = {"FileName":household_file.name,"FileType":household_file.type}
        df  = pd.read_csv(household_file)
        st.dataframe(df)
        save_uploadedfile(household_file)
        fph = "1.raw/landing/households"
        resp = azure_upload_df("cloudprojdatastore",df,household_file.name,fph)
        st.success(resp)
    
    if product_file is not None:
        file_details = {"FileName":product_file.name,"FileType":product_file.type}
        df  = pd.read_csv(product_file)
        st.dataframe(df)
        save_uploadedfile(product_file)
        fpp = "1.raw/landing/products"
        resp = azure_upload_df("cloudprojdatastore",df,product_file.name,fpp)
        st.success(resp)

    if transactions_file is not None:
        file_details = {"FileName":transactions_file.name,"FileType":transactions_file.type}
        df  = pd.read_csv(transactions_file)
        st.dataframe(df)
        save_uploadedfile(transactions_file)
        fpt = "1.raw/landing/transactions"
        resp = azure_upload_df("cloudprojdatastore",df,transactions_file.name,fpt)
        st.success(resp)
import streamlit as st
from st_acpt_sav_file_locally import file_input

def l4():
    st.write("""Note: The backend in Azure is built using 
           1. Azure Data Factory(Event Listener Trigger - on datalake)
           2. Azure Databricks(Transformation Engine)
           3. Azure DataLake(To store the data)
           """)
    st.markdown("Note: The event-based-trigger is activated only when the transactions file is uploaded, so please do make sure to upload the transactions file for new data.")
    file_input()
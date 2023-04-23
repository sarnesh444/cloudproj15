from databricks import sql
from pandas import DataFrame
import streamlit as st

def l2():
  st.write("Dynamic Data Pull")
  st.write("""Note: The backend in Azure is built using 
           1. Azure Data Factory(Event Listener Trigger - on datalake)
           2. Azure Databricks(Transformation Engine)
           3. Azure DataLake(To store the data)
           """)
  st.markdown("Note: In case the queries are slow initially,it could be because the databricks cluster is spinning up, a configuration has been made in the backend to turn off the cluster after 20 mins of inactivity to save costs,please wait for a few mins and data should appear.")
  st.markdown("Note: After uploading the file, the new hashnumber might not be visible immediately since the pipeline has to be executed and data load should happen for new data, please try in about 2 mins and it should work.")
  
  hn = st.text_input("HashNumber")
  with sql.connect(server_hostname = "adb-3105568704852454.14.azuredatabricks.net",
                  http_path       = "sql/protocolv1/o/3105568704852454/0423-001657-4dfss5fl",
                  access_token    = "dapi82f38b54aee578d84721cc989a70ab4b-3") as connection:

    with connection.cursor() as cursor:
      if(hn):
          res = cursor.execute(f"SELECT * FROM lakehouse.datapull where Hshd_Num={hn} LIMIT 1000")
          df = DataFrame(res.fetchall())
          df.columns=[x[0] for x in res.description]
          st.write(f"Data Pull for HSHD_NUM {hn} by joining household, transaction, and products tables")
          st.dataframe(df)
          st.write("Displaying only top 1000 rows")

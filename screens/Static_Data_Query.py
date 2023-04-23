from databricks import sql
from pandas import DataFrame
import streamlit as st

def l1():
  with sql.connect(server_hostname = "adb-3105568704852454.14.azuredatabricks.net",
                  http_path       = "sql/protocolv1/o/3105568704852454/0423-001657-4dfss5fl",
                  access_token    = "dapi82f38b54aee578d84721cc989a70ab4b-3") as connection:

    with connection.cursor() as cursor:
      res = cursor.execute("SELECT * FROM lakehouse.datapullhshd10 LIMIT 1000")
      
      df = DataFrame(res.fetchall())
      df.columns=[x[0] for x in res.description]
      st.write("Data Pull for HSHD_NUM #10 by joining household, transaction, and products tables")
      st.markdown("Note: In case the queries are slow initially,it could be because the databricks cluster is spinning up, a configuration has been made in the backend to turn off the cluster after 20 mins of inactivity to save costs,please wait for a few mins and data should appear.")
      st.dataframe(df)
      st.write("Displaying only top 1000 rows")

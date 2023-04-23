from databricks import sql
from pandas import DataFrame
import streamlit as st

with sql.connect(server_hostname = "adb-3105568704852454.14.azuredatabricks.net",
                 http_path       = "sql/protocolv1/o/3105568704852454/0423-001657-4dfss5fl",
                 access_token    = "dapi82f38b54aee578d84721cc989a70ab4b-3") as connection:

  with connection.cursor() as cursor:
    res = cursor.execute("SELECT * FROM lakehouse.datapull LIMIT 1000")
    
    df = DataFrame(res.fetchall())
    df.columns=[x[0] for x in res.description]
    st.dataframe(df)
    st.write("Displaying only top 1000 rows")

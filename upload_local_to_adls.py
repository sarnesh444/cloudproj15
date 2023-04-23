import os, uuid
from io import BytesIO
from datetime import datetime
from urllib.parse import urlparse
from azure.storage.blob import BlobServiceClient
import pandas as pd
import logging

def azure_upload_df(container=None, dataframe=None, filename=None,fp=None):
    """
    Upload DataFrame to Azure Blob Storage for given container
    Keyword arguments:
    container -- the container name (default None)
    dataframe -- the dataframe(df) object (default None)
    filename -- the filename to use for the blob (default None)
    
    Function uses following enviornment variables 
    AZURE_STORAGE_CONNECTION_STRING -- the connection string for the account
    OUTPUT -- the ouput folder name
    eg: upload_file(container="test", dataframe=df, filename="test.csv")
    """
    if all([container, len(dataframe), filename,fp]):
        file_path = fp
        upload_file_path = os.path.join(file_path, f"{filename}")
        connect_str = "DefaultEndpointsProtocol=https;AccountName=cloudprojadls;AccountKey=i2bapy9Bvxe17E5Khl1q/aL5UDn6mKBtqAkLbd7+zxzXp5kGxEf7vb4UspKQ63FSyPEUepefDhpB+AStQUf/xg==;EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(
            container=container, blob=upload_file_path
        )
        try:
            output = dataframe.to_csv(index=False, encoding="utf-8")
        except Exception as e:
            logging.error('adls', e)
            pass
        try:
            blob_client.upload_blob(output, blob_type="BlockBlob",overwrite=True)
            return f"{filename} successfully uploaded to ADLS"
        except Exception as e:
            logging.error('adls-blob', e)
            pass

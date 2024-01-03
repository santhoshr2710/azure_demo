from flask import Flask, render_template, request, redirect, url_for
from azure.storage.blob import BlobServiceClient
import os
import uuid

app = Flask(__name__)

# Azure Storage credentials
AZURE_STORAGE_CONNECTION_STRING = 'your_storage_connection_string'
CONTAINER_NAME = 'your_container_name'

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
blob_container_client = blob_service_client.get_container_client(CONTAINER_NAME)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # Check if the file is empty
        if file.filename == '':
            return redirect(request.url)
        
        # Generate a unique filename
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        
        # Upload the file to Azure Blob Storage
        blob_client = blob_container_client.get_blob_client(filename)
        blob_client.upload_blob(file)

    # List all files in the Azure Blob Storage container
    blob_list = blob_container_client.list_blobs()
    files = [blob.name for blob in blob_list]

    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)

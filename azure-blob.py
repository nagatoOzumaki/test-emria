import os, time
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Variables globales
DATASET=["mini-file.txt","ISO-IEC-27001-2013F-full-permission.pdf","MITRE-ATTACKS.pdf","bufferOverflow.pdf",
         "Guide-PME-pour-la-mise-en-place-de-l-ISO-IEC-27001.pdf","kubernetes-handbook.pdf",
         "tor-browser.tar.xz","vedio.mp4","kali-linux.zip", "kali-linux.vmdk"]
ACCOUNT_URL = "https://riadstorage.blob.core.windows.net/blob-storage-container"
CONTAINER_NAME="blob-storage-container"

# Utilisez les informations d'identification définies par l'hôte AWS CLI
default_credential = DefaultAzureCredential()

# Créez l'objet BlobServiceClient
blob_service_client = BlobServiceClient(ACCOUNT_URL, credential=default_credential)

# Fonction pour obtenir la taille d'un fichier et calculer la latence
def get_file_size(file_name):
    size = os.path.getsize(os.path.join(r'./data/',file_name))
    return size

# Fonction pour télécharger le fichier
def download_file(blob_service_client: BlobServiceClient, CONTAINER_NAME, blob):
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob)
    with open(file=os.path.join(r'./data', blob_client.blob_name), mode="wb") as sample_blob:
        download_stream = blob_client.download_blob()
        sample_blob.write(download_stream.readall())

# Fonction pour mesurer la vitesse de téléchargement d'un fichier
def download_file_speed(filename):
    start_time = time.time()
    download_file(blob_service_client, CONTAINER_NAME, filename)
    end_time = time.time()
    file_size = get_file_size(filename)
    speed = file_size / (end_time - start_time)
    print("File : " + str(filename) + "         Size : " + str(file_size) + "            Download speed : " + str(speed))

# Fonction pour téléverser le fichier
def upload_file(file_name):
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file_name)
    with open(file=os.path.join(r'./data/', file_name), mode="rb") as data:
        blob_client.upload_blob(data)

# Fonction pour mesurer la vitesse de téléversement d'un fichier
def upload_file_speed(filename):
    file_size = get_file_size(filename)
    start_time = time.time()
    upload_file(filename)
    end_time = time.time()
    speed = file_size / (end_time - start_time)
    print("File : " + str(filename) + "         Size : " + str(file_size) + "            Upload speed : " + str(speed))

# Fonction principale
def main():
    for file in DATASET:
        # upload_file_speed(file)  # Cette ligne est pour tester les performances de téléversement
        download_file_speed(file)  # Cette ligne est pour tester les performances de téléchargement
        print("------------------------------")

# Exécutez la fonction principale
main()

import boto3
import time
import os

 
DATASET=["mini-file.txt","ISO-IEC-27001-2013F-full-permission.pdf","MITRE-ATTACKS.pdf","bufferOverflow.pdf","Guide-PME-pour-la-mise-en-place-de-l-ISO-IEC-27001.pdf","kubernetes-handbook.pdf", "tor-browser.tar.xz","vedio.mp4","kali-linux.zip",
  "kali-linux.vmdk"]
BUCKET_NAME="object-storage-s3"
   
   

# get the size of a file to calculate latency
def get_file_size(file_name):
    size = os.path.getsize(os.path.join(r'./data/',file_name))
    return size


s3 = boto3.client('s3')


def download_file(file_name):
    local_file_path = os.path.join("./data", os.path.basename(file_name))
    s3.download_file(BUCKET_NAME, file_name,local_file_path)


def upload_file(file_name):
    with open(file=os.path.join(r'./data/', file_name),mode="rb") as f:
        s3.upload_fileobj(f, BUCKET_NAME,file_name)




def download_file_speed(filename):
    start_time = time.time()
    download_file(filename)
    end_time = time.time()
    file_size = get_file_size(filename)
    speed=file_size / (end_time - start_time)
    print("File : "+str(filename)+"         Size :"+str(file_size)+"            Download speed : "+str(speed))


def upload_file_speed(filename):
    file_size = get_file_size(filename)
    start_time = time.time()
    upload_file(filename)
    end_time = time.time()
    speed=file_size / (end_time - start_time)
    print("File : "+str(filename)+"         Size :"+str(file_size)+"            Upload speed : "+str(speed))



def main():
    for file in DATASET:

        # upload_file_speed(file) # this line for testing upload performance

        download_file_speed(file) # this line for testing download performance

        print("------------------------------")
        


main()
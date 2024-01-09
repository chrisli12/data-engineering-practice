import requests
import os
from pathlib import Path
import validators
import zipfile

download_urls = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def download_file(url):
    filename = url.split('/')[-1]   #get filename
    with requests.get(url, stream=True) as response:
        with open(filename, mode="wb") as file:
            file.write(response.content)
    

def main():
    # your code here
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #make new dir if not exist, if exists change dir to downloads
    if not os.path.exists(dir_path + "/downloads"):
        os.mkdir(dir_path + "/downloads")
    
    #change dir to downloads
    os.chdir(dir_path + "/downloads")
    
    #download files one by one
    for url in download_urls:
        #make sure the url is valid
        if validators.url(url):
            download_file(url)

    #Unzip file one by one 
    for file in os.listdir():
        #make sure the zip is valid
        if zipfile.is_zipfile(file):
            with zipfile.ZipFile(file) as item:
                item.extractall()
        os.remove(file)
                

if __name__ == "__main__":
    main()

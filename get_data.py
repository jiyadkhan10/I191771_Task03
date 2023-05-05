mport os
import wget

# data from https://www.kaggle.com/datasets/dissfya/atp-tennis-2013-2023?resource=download
# Download the zipped dataset
url = 'https://www.kaggle.com/datasets/dissfya/atp-tennis-2013-2023'
file_name = "data.csv"
wget.download(url, file_name)

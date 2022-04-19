from google.colab import drive
import os
import shutil
import json

def get_ds(name=None):
    if name:
        drive.mount('/content/drive', force_remount=True)
        if not (os.path.isdir("~/.kaggle") | os.path.isdir("kaggle")):
            os.mkdir("/root/.kaggle")
            os.mkdir("kaggle")
        shutil.copy("/content/drive/MyDrive/kaggle/kaggle.json", "/root/.kaggle")
        import kaggle
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(name, path='/root/.kaggle', unzip=True)

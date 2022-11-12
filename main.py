import os
import json
import time
import shutil



class DownloadDirectoryManager:

    download_directory = r"C:\Users\Dominik\Downloads"
    #download_directory = os.getcwd()
    json_file = open('files_info.json')
    files_info = json.load(json_file)
    downloaded_files = []

    def create_directories(self):
        for data in self.files_info['file_types']:
            self.folder_directory = os.path.join(self.download_directory, data['folder_name'])
            if not os.path.exists(self.folder_directory):
                os.makedirs(self.folder_directory)

    def list_of_files(self):
        self.all_files = os.listdir(self.download_directory)
        for file in self.all_files:
            self.file_path = os.path.join(self.download_directory, file)
            if os.path.isfile(self.file_path):
                self.downloaded_files.append(self.file_path)

        return self.downloaded_files
        
    def copy_files(self):
        ###jesli plik juz istnieje w jakims folderze to zmiana jego nazwy
        for file_path in DDM.list_of_files():
            self.file_extension = os.path.basename(file_path)
            self.file_extension = os.path.splitext(self.file_extension)
            self.file_extension = self.file_extension[1]
            
            for data in self.files_info['file_types']:
                if data['file_extensions'] == []:
                    data['file_extensions'] = self.file_extension
                if self.file_extension in data['file_extensions']:
                    try:
                        shutil.move(file_path, os.path.join(self.download_directory, data['folder_name']))
                    except:
                        pass

DDM = DownloadDirectoryManager()

while True:
    DDM.create_directories()
    DDM.copy_files()
    time.sleep(1)
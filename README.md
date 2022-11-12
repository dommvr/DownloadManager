# DownloadManager

Simple project that manage your download folder by automatically segregating downloaded files to right extension folders.

# Setup

 - Change download folder path
``` 
    download_directory = r"C:\Users\Dominik\Downloads"
```

 - You can change names and add new directories with another files category by editing json file  `files_info.json`
 - You can also add more extensions to files category, not all of them are included in json file
 ``` 
 {
    "file_types": [
        {
            "file_type": "image",
            "file_extensions": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tif", ".tiff", ".eps", ".raw"],
            "folder_name": "Images"
        },
 ```
- If you want program to run automatically in the background you can follow this tutorial: https://medium.com/analytics-vidhya/easiest-way-to-run-a-python-script-in-the-background-4aada206cf29

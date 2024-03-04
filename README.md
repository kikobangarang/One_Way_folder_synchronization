# One_Way_folder_synchronization

# Overview
This Folder Synchronization Tool is a Python script designed to automatically synchronize the contents of a source folder with a replica folder at specified intervals. The tool ensures that any changes made in the source folder, including the creation, modification, or deletion of files and directories, are mirrored in the replica folder. It provides detailed logging of all operations for easy monitoring.

# Features
* File Synchronization: Compares files in both source and replica folders and synchronizes them to ensure both folders have identical contents.
* Directory Synchronization: Recursively synchronizes the contents of subdirectories.
* Change Detection: Detects additions, modifications, and deletions in the source folder and applies them to the replica folder.
* Logging: Records all synchronization activities, including file and directory creation, modification, and deletion, with timestamps.

# Requirements
Python 3.x, libraries used are included, no need for installation.

# Usage
The script is executed from the command line with optional arguments to specify the source and replica folder paths, the path to the log file, and the synchronization period.

`python folder_sync.py --source /path/to/source --replica /path/to/replica --log_path /path/to/logfile.txt --period 60`


# Arguments
* --source: Path to the source folder. Default is "source".
* --replica: Path to the replica folder. Default is "replica".
* --log_path: Path to the log file where synchronization activities will be recorded. Default is 'logfile.txt'.
* --period: Time interval (in seconds) between each synchronization operation. Default is 30 seconds.







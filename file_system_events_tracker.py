import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/lenovo/Downloads"
# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created (self,event):
        print(f"Hi,{event.src_path} has been created")
    #2_on_deleted
    def on_deleted (self,event):
        print(f"opps! some one deleted {event.src_path}")
    #3_on_modified
    def on_modified (self,event):
        print(f"{event.src_path} has been modified")
    #4_on_moved
    def on_moved (self,event):
        print(f"Moved from {event.src_path} to {event.dest_path}")
        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt

while True:
    time.sleep(2)
    print("running...")







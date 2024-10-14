import time
import logging
import os
import checker
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
logging.basicConfig(filename='logging.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
class watcher(FileSystemEventHandler):
    def on_created(self, event: FileSystemEvent):
        if not event.is_directory:
            _, file_extension = os.path.splitext(event.src_path)
            if file_extension.lower() != '.dfq':
                pass
            else
        
    
    def on_deleted(self, event: FileSystemEvent):#删除文件触发删除事件写入路径到log文件
        return super().on_deleted(event)

observer=Observer()
handler1=watcher()
observer.schedule(handler1,path=r'C:\Users\David\Desktop\messen-monitoring',recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
        #print(eventpath)
except KeyboardInterrupt:
    observer.stop()
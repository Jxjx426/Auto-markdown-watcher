import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from markitdown import MarkItDown

# 自动定位到当前用户的桌面创建 To_AI 文件夹
home = os.path.expanduser("~")

onedrive_desktop = os.path.join(home, "OneDrive", "Desktop")
desktop = os.path.join(home, "Desktop")

if os.path.exists(onedrive_desktop):
    WATCH_DIR = os.path.join(onedrive_desktop, "To_AI")
else:
    WATCH_DIR = os.path.join(desktop, "To_AI")


md = MarkItDown()

class AutoConvertHandler(FileSystemEventHandler):
    def on_created(self, event):
        # 忽略文件夹，且只处理非 .md 文件
        if not event.is_directory and not event.src_path.endswith('.md'):
            file_path = event.src_path
            print(f"[INFO] New file detected: {file_path}. Converting...")
            try:
                # 稍微等待确保文件完全写入
                time.sleep(1) 
                result = md.convert(file_path)
                
                # 生成同名的 .md 文件
                output_path = os.path.splitext(file_path)[0] + ".md"
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result.text_content)
                print(f"[SUCCESS] Convert completed: {output_path}")
                
            except Exception as e:
                print(f"[ERROR] Convert failed: {e}")

if __name__ == "__main__":
    if not os.path.exists(WATCH_DIR):
        os.makedirs(WATCH_DIR)
    
    event_handler = AutoConvertHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIR, recursive=False)
    observer.start()
    
    # 替换成了纯英文打印，彻底解决 cp1252 编码报错
    print(f"==================================================")
    print(f" Watching folder: {WATCH_DIR}")
    print(f" Drop files here to convert them to Markdown automatically!")
    print(f" Press Ctrl+C to stop.")
    print(f"==================================================")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
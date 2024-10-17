from pathlib import Path
import dfq_reader
# 设置你想要迭代的目录
directory = Path(r'C:\Users\David\Desktop\messen-monitoring\RE')

# 遍历目录及其子目录下的所有文件
for file_path in directory.rglob('*'):
    if file_path.is_file():
        dfq_reader.read_dfq_file(file_path)

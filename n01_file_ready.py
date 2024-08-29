import os
import shutil
import pandas as pd
import time

def get_latest_xlsx_file(folder_path):
    # 获取文件夹中的所有文件
    files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]
    
    # 如果文件夹中没有xlsx文件，返回None
    if not files:
        return None
    
    # 获取文件的完整路径和创建时间
    files_with_ctime = [
        (f, os.path.getctime(os.path.join(folder_path, f)))
        for f in files
    ]
    
    # 按创建时间排序，获取最新的文件
    latest_file = max(files_with_ctime, key=lambda x: x[1])[0]
    
    return os.path.join(folder_path, latest_file)

def remove_file(source_file,destination_folder):
  # 移动文件
    shutil.move(source_file, destination_folder)


    

if __name__ == "__main__":
    folder_path = "xlsx"  # 替换为你的文件夹路径
    read_latest_xlsx(folder_path)
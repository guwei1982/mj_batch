import configparser
import n01_file_ready
import n02_xlsx
import mj
import conver
import download
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
#from google.colab import files

jobs = 3 #定义线程数

def process_prompt(item, j, file_name, cookie):
    # Process a single prompt item
    first_value = str(item[0])
    second_value = str(item[0]) + item[1]
    job_id = mj.mj_send(second_value, cookie)
    urls = conver.mj_url_convert(job_id)
    for i, url in enumerate(urls):
        download.download_image(url, f"{first_value}-{j}-{i}", file_name)
        n02_xlsx.add_to_excel(job_id, url, first_value, file_name)
    return f"Prompt {first_value}-{j} 下载完成"

def main(repeat):
    # 创建配置解析器对象
    config = configparser.ConfigParser(interpolation=None)
    # 读取配置文件
    with open('config.ini', 'r', encoding='utf-8') as f:
        config.read_file(f)

    folder_path = "xlsx01"
    latest_file = n01_file_ready.get_latest_xlsx_file(folder_path)
    file_name = os.path.splitext(os.path.basename(latest_file))[0]
    file_name = os.path.join('img', file_name)

    if latest_file:
        print(f"读取文件: {latest_file}")
        cookie = config.get("mj01", 'cookie')
        prompts = n02_xlsx.process_excel(latest_file)
        print(prompts)

        # Using ProcessPoolExecutor for parallel processing
        with ProcessPoolExecutor(max_workers=jobs) as executor:
            futures = []
            for item in prompts:
                # Submit tasks to the executor
                for j in range(repeat):
                    futures.append(executor.submit(process_prompt, item, j + 1, file_name, cookie))

            # Collect results as they complete
            for future in as_completed(futures):
                print(future.result())
        #os.system(f"zip -r '{file_name}.zip' '{file_name}'")
        #print("压缩完成")
        n01_file_ready.remove_file(latest_file, "finish")
        #files.download(f'img/{file_name}.zip')

    else:
        print("文件夹中没有xlsx文件,等待60秒")
        time.sleep(60)

if __name__ == "__main__":
    main(1)
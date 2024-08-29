import requests
import os
import time
#from google.colab import files
#def download_image(image_link, img_name, folder_path, cookie):
def download_image(image_link, img_name, folder_path):
  # 确保目标文件夹存在，如果不存在则创建
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)

  # 定义请求头
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    #'Cookie': cookie,
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'Sec-Ch-Ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
  }

  # 遍历链接并尝试下载

  for i in range(15):
    try:
      # 发送HTTP GET请求，并附加改过的头信息
      response = requests.get(image_link, headers=headers, timeout=330)
      response.raise_for_status()  # 如果响应状态码不是200，将引发HTTPError异常
      # 格式化图片文件名
      filename = f"{img_name}.png"
      file_path = os.path.join(folder_path, filename)

      # 将内容写入文件
      with open(file_path, 'wb') as f:
          f.write(response.content)
      #files.download(file_path)
      print(f"下载成功: {filename}")
      return file_path
    except requests.exceptions.RequestException as e:
      i = i + 1
      print(f"下载出现异常: {e}. 第{i}次重试中...")
      time.sleep(30)


if __name__ == "__main__":
    prompt = "https://test-1251554225.cos.ap-beijing.myqcloud.com/img/a.png"
    ttt = download_image(prompt,'c51001bc-56e3-482d-a685-d377275000cb-1','img')
    print(ttt)
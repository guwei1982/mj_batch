import requests
import json
import time

def mj_send(prompt,cookie):
  # 请求的URL
  url = 'https://www.midjourney.com/api/app/submit-jobs'
  # 请求headers
  headers = {
  "accept": "*/*",
  "accept-encoding":"gzip, deflate, br, zstd",
  "accept-language": "zh-CN,zh;q=0.9",
  "content-type": "application/json",
  "origin":"https://www.midjourney.com",
  "pragma": "no-cache",
  "priority": "u=1, i",
  "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"127\", \"Google Chrome\";v=\"127\"",
  "sec-ch-ua-arch": "\"x86\"",
  "sec-ch-ua-bitness": "\"64\"",
  "sec-ch-ua-full-version": "\"127.0.6533.120\"",
  "sec-ch-ua-full-version-list": "\"Not/A)Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"127.0.6533.89\", \"Google Chrome\";v=\"127.0.6533.89\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-model": "\"\"",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-ch-ua-platform-version": "\"10.0.0\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
  "x-csrf-protection": "1",
  "cookie": cookie,
  "Referer": "https://www.midjourney.com/imagine",
  }

  # 请求payload
  payload = {
    "f": {
      "mode": "relaxed",
      "private": False
    },
    "channelId": "singleplayer_00884594-5a7c-40ee-8a85-1144263cfb88",
    "roomId": None,
    "metadata": {
      "imagePrompts": 0,
      "imageReferences": 0,
      "characterReferences": 0
    },
    "t": "imagine",
    "prompt": prompt
  }

  for _ in range(3):
    try:
      # 发送POST请求
      response = requests.post(url, headers=headers, json=payload)
      response.raise_for_status()  # 如果响应状态码不是200，将引发HTTPError异常
      #print(response.content)
      json_data = response.json()  # 将字符串解析为 JSON 对象
      decoded_content = json_data["success"][0]["job_id"]
      print("生成成功", decoded_content)
      return decoded_content
    except requests.exceptions.RequestException as e:
      print(response.content)
      print(f"生成失败: {e}. 10秒后重试...")
      time.sleep(10)


if __name__ == "__main__":
  cookie = "AMP_MKTG_437c42b22c=JTdCJTdE; _gcl_au=1.1.1466556077.1724665436; _ga=GA1.1.1926917397.1724665436; __stripe_mid=1731f818-926b-4472-9721-64a4b9402aafd79341; cf_clearance=chuGH_GSqFPEs0GNrq48QkF1O8GL8WOSLfIyxfsRDQw-1724666911-1.2.1.1-Z5N6P8KEbGpwsp6Wby.K4pz8aV76yYC9cxv_yOzNtUySWik4Hk0RDVwKvfiuuntR0VJMA7BNtdR9hLajmxd85mApoXLzzb7yuVhhgSPRui2LacMFbgm7iISAVLQwY18XVSYR1ZQ3gS95FrWAFDInJARR0JxKq4iz0W2l2mqAVjs2LfT53EOWzZG2IJGZXJngt47bjOvj5pD00fF2xPzRErUA53U93Igha1ekkPMgrzZe.w1RyAdo43fwHYC9iJ3NWuCWAQHhvt1n5efAfHEuDxWfO3UYH45nXaAI.pajuVdQdEdSU5mxDhBYOHErQCla4M8lXvmYWAfEuYa8h7uGx_VNFjWU0f1mXCeN4JP9kVw5leKanEPUq3kHRwJ0coSPwZgtF96Vqr5czG1Hd82nYw; __cf_bm=mTBPu8nx2IxEz0HX92DN59If4IgT9SCDGzoJ6xqbPYU-1724683800-1.0.1.1-2Ml0aN2nfdzo9l8MWNe6fEq_usCJhX_Co5rFnDz5MYnz5RKT3R6E4ev.OCVawnt1GPYhmLmT3vlxW_jKu6JUhg; __Host-Midjourney.AuthUserToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiZmlyZWJhc2UiLCJpZFRva2VuIjoiZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqRXhZemhpTW1SbU5HTTFOVGxrTWpoak9XUmxOV1EwTVRBeE5ERmlNekJrT1dVeVltTmxNMklpTENKMGVYQWlPaUpLVjFRaWZRLmV5SnVZVzFsSWpvaWJYbHRhakEySWl3aWJXbGthbTkxY201bGVWOXBaQ0k2SWpjeE1qWTFZak5oTFdVNE0yVXROR1F6WXkwNE5tWm1MV1ZpWXpObU5XTXpNbUpqTkNJc0ltbHpjeUk2SW1oMGRIQnpPaTh2YzJWamRYSmxkRzlyWlc0dVoyOXZaMnhsTG1OdmJTOWhkWFJvYW05MWNtNWxlU0lzSW1GMVpDSTZJbUYxZEdocWIzVnlibVY1SWl3aVlYVjBhRjkwYVcxbElqb3hOekkwTmpZMk1EQTVMQ0oxYzJWeVgybGtJam9pYURVNE1ubG9WVkJMU1dSYWRXcGpaVFJtVG5BeE5VUXdObGQ1TVNJc0luTjFZaUk2SW1nMU9ESjVhRlZRUzBsa1duVnFZMlUwWms1d01UVkVNRFpYZVRFaUxDSnBZWFFpT2pFM01qUTJPRFF5T0RRc0ltVjRjQ0k2TVRjeU5EWTROemc0TkN3aVpXMWhhV3dpT2lKdGVYTnJNVUJ4Y1M1amIyMGlMQ0psYldGcGJGOTJaWEpwWm1sbFpDSTZkSEoxWlN3aVptbHlaV0poYzJVaU9uc2lhV1JsYm5ScGRHbGxjeUk2ZXlKa2FYTmpiM0prTG1OdmJTSTZXeUl4TVRRek5EWTFPRFl4TlRReU16RTRNRGt3SWwwc0ltVnRZV2xzSWpwYkltMTVjMnN4UUhGeExtTnZiU0pkZlN3aWMybG5ibDlwYmw5d2NtOTJhV1JsY2lJNkltUnBjMk52Y21RdVkyOXRJbjE5LlRoRUE3eW8tZUYyOWFpbjM3cHhONW9CQVY5Wmt2cHIzY2NkSktKdEVyRkMwVE5Fay1PSXJJY2NiMXlnX0tralVzdnM4aFVSc3RPY0twaEQ5WWZZYzF2ZGtXaFF3ZzNoUHlXbzRKV2tzZ2lnb2pmdEpaS1Y5MVdnWi1GTTlQWEQ3TmR0cWJiTGVtbG83QVNDUDZMQWtoa19UTEVEYWw0VnZKY3Nub280NnEzUTFMYjVXNzNEQ0kwY2RzbmVpS1c4T3NpMXppMEZ5b2N1WmJUdG9ORkdObzVST016NnBGeDM3akQyeGl2am5oODF5cU5GMFdZRWF3Mzl6UkJuVUtuTlZDbVZqcGhlUFRadXlDOHBNSUs3alhPWElsbUtCOGtDZ3NOZUJDT2RJUXRpZC1kc3FrMllGV3FBaDJHdG1hLUVkV1hSRXoydTBYTHRJQVRTRHluSXdYUSIsInJlZnJlc2hUb2tlbiI6IkFNZi12QnpiMmNKWHdnYlFtZzBYcnZlYmtnUnZCTERRbW54OGVWUnlBdW12S0NJWjFOSWR4WmhxWkMxd1F1Qkp3UHJaamlrbGtydHQ2SzRYZzZZVWxZLVlUcVBxeEtScXNkc3pSTnhuWHRBU0ltNUdXd3J5S25aWDBfSExxU1VqcHk3LU1oOUlaa3ZtYi02VmRBXzI2WVQtSjM3aGNnUW80UmVGdjRaVzY3NnB0OTVRQi1qOGs1djJWc1VYaHc3bkpidTExX3JtZFhPSnkxSEMxWVo2NS01QjZQV0RWdmYyNDlGeHlsMS1MdGNjU21aNVVON1pWYWNteU0yU0NTcVJOck1FdVY2a3pxaHYiLCJpYXQiOjE3MjQ2ODQyODR9.ytRmFcYLqDX_FE4ki5ZarpvJ6KQ4OMRYjh95mt7Z9Rs; _ga_Q0DQ5L7K0D=GS1.1.1724684583.2.0.1724684583.0.0.0; AMP_437c42b22c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJiYTU2ZjI1ZS1hMGJmLTQxODgtOTJjYy1iOGQzYzc0NzVlYTElMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI3MTI2NWIzYS1lODNlLTRkM2MtODZmZi1lYmMzZjVjMzJiYzQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzI0Njg0NjExODQ5JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTE4JTdE"

  mj_send("two chinese old man --ar 16:9 --v 6.1",cookie)

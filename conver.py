#图像链接转换
def mj_url_convert(job_id):
  prefix = "https://cdn.midjourney.com/"
  suffix1 = "/0_0.png"
  suffix2 = "/0_1.png"
  suffix3 = "/0_2.png"
  suffix4 = "/0_3.png"

  download_url1 = prefix + job_id + suffix1
  download_url2 = prefix + job_id + suffix2
  download_url3 = prefix + job_id + suffix3
  download_url4 = prefix + job_id + suffix4

  download_urls = [download_url1,download_url2,download_url3,download_url4]
  print(download_urls)
  return download_urls
  
  
if __name__ == "__main__":
    mj_url_convert("c51001bc-56e3-482d-a685-d377275000cb")
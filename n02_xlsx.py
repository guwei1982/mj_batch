import pandas as pd
import os
#读取xlsx并返回元组
def process_excel(file_path):
    # 读取Excel文件的第一个表格
    df = pd.read_excel(file_path, sheet_name=0)
    
    # 存储结果的列表
    results = []
    
    # 遍历每一行，合并第一列和第二列到第十列的内容
    for index, row in df.iterrows():
        first_column = row.iloc[0]
        combined_columns = ' '.join(map(str, row.iloc[1:10]))  # 将第二列到第十列内容合并
        results.append((first_column, combined_columns))
    
    return results

  
#写入xlsx
def add_to_excel(a, b, c, file_path):
  file_path = f"{file_path}.xlsx"
  # 检查文件是否存在
  if os.path.exists(file_path):
    #加载存量数据
    df = pd.read_excel(file_path)
  else:
    #如果文件不存在，则使用标头创建一个新的DataFrame
    df = pd.DataFrame(columns=['Column A', 'Column B', 'Column C'])
  #新增一行
  new_row = pd.DataFrame([[a, b, c]], columns=['Column A', 'Column B', 'Column C'])
  df = pd.concat([df, new_row], ignore_index=True)
  #保存表格
  df.to_excel(file_path, index=False)
  print(f"Data ({a}, {b}, {c}) added to {file_path}")


if __name__ == "__main__":
  # 示例调用
  file_path = 'finish/cccttt'  # 请替换为你的文件路径
  #output = process_excel(file_path)
  a = "ssdfsdfsdf"
  b = "http://ccc.com/ccc.png"
  c = "2544-1-2"
  add_to_excel(a, b, c, file_path)
  #print(output)   


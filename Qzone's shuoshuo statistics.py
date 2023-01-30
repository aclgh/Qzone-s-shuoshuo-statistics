import os
import json
import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

os.remove("timestamp_to_date.txt")
# 遍历文件夹中的所有json文件
for file_name in os.listdir("shuoshuo"):
    if file_name.endswith(".json"):
        file_path = os.path.join("shuoshuo", file_name)
        try:
            with open(file_path, "r", encoding="gb18030",errors='ignore')  as file:
                data = json.load(file)
        except json.JSONDecodeError as error:
            print(f"An error occurred: {error}")        
                # 取出 "msglist" 列表
        msglist = data.get("msglist")
        if msglist is not None:
            for msg in msglist:
            # 取出 "commentlist" 列表
                commentlist = msg.get("commentlist")
                if commentlist is not None:
                    for comment in commentlist:
                    # 读取 "create_time" 的值
                        create_time = comment.get("create_time")
                        # 跳过 None 值
                        if create_time is not None:
                            #print(create_time)
                            # 将时间戳转换成日期格式
                            #date = datetime.datetime.fromtimestamp(create_time).strftime('%Y-%m-%d %H:%M:%S\n')
                            date = create_time
                            # 将时间戳保存到文件中
                            with open('timestamp_to_date.txt', 'a') as file:
                                date=str(date)
                                date+="\n"
                                file.write(date)
# 把时间戳保存至数组
with open("timestamp_to_date.txt", "r") as file:
     timestamps = file.read().split('\n')
timestamps.pop()
#print(timestamps)
# 统计对应月份并存入字典
timestamps_dict = defaultdict(int)
for timestamp in timestamps:
     ym = datetime.datetime.fromtimestamp(int(timestamp))
     year_month = (ym.year, ym.month)
     timestamps_dict[year_month] += 1
print(timestamps_dict)

#绘图
x = [f"{year}.{month}" for year, month in timestamps_dict.keys()]
y = timestamps_dict.values()
Sum = sum(y)

plt.xticks(rotation=45)
plt.bar(x, y)
plt.xlabel("year")
plt.ylabel("Times of shuoshuo")
plt.title(f"Shuoshuo of Qzone ——sum:{Sum}")
for i, v in enumerate(y):
    plt.text(i, v + 0.5, str(v), ha='center')
plt.show()

import pandas as pd
import sqlite3
import json

# 读取 JSON 文件
with open('school_detail.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取 'data' 部分
df = pd.json_normalize(data['data'])

# 创建 SQLite 数据库连接
conn = sqlite3.connect('school_detail.sqlite')
cursor = conn.cursor()

# # 创建带有主键和外键的空表
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS school_detail (
#         school_id TEXT PRIMARY KEY,
#         school_name TEXT,
#         city_name TEXT,
#         department TEXT,
#         nature_name TEXT,
#         level_name TEXT,
#         ruanke_level TEXT,
#         ruanke_rank TEXT,
#         tag_name TEXT,
#         type_name TEXT
#     )
# ''')

# 将 DataFrame 写入 SQLite 数据库
df.to_sql('school_detail', conn, if_exists='append', index=False)

# 关闭数据库连接
conn.close()
print("Done!")
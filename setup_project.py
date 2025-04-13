import os

# 定義資料夾與檔案結構
project_structure = {
    "LLM_Project": [
        "data",
        "data/raw",
        "scripts",
        "logs"
    ]
}

files = [
    "data/raw/raw_data.json",         # 儲存電影的資料
    "scripts/movie_scraper.py",       # 爬蟲腳本
    "scripts/movie_llm.py",           # LLM 用來詢問並推薦電影的腳本
    "main.py",                        # 主程式
    "requirements.txt",               # 需要安裝的套件
    "README.md"                       # 專案說明
]

# 建立資料夾
for folder, subfolders in project_structure.items():
    os.makedirs(folder, exist_ok=True)
    for subfolder in subfolders:
        os.makedirs(os.path.join(folder, subfolder), exist_ok=True)

# 建立檔案
for file in files:
    file_path = os.path.join("LLM_Project", file)
    with open(file_path, "w") as f:
        pass  # 建立空檔案

print("✅ 專案檔案結構已建立完成！")
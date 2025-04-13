import requests
import json
import os
from dotenv import dotenv_values

# TMDb API Key
BASE_URL = "https://api.themoviedb.org/3" #api網域名使用v3
config = dotenv_values("key.env")
API_KEY  = config["TMDB_API_KEY"]

# 爬取電影資料
def fetch_movie_data(movie_name):
    """根據電影名稱從 TMDb API 獲取電影資料"""
    search_url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}&language=zh-TW"    
    response = requests.get(search_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# 解析電影資料
def parse_movie_data(movie_data):
    """解析電影資料並格式化"""
    if not movie_data or 'results' not in movie_data:
        return "找不到相關電影資料"
    if not movie_data.get('results'):  # 檢查 'results' 是否存在且非空
        print("⚠️ 查無此電影，請確認名稱是否正確！")
        return ("⚠️ 查無此電影，請確認名稱是否正確！")  # 返回 None，避免 IndexError
    
    movie_info = movie_data['results'][0]  # 取第一部電影結果
    title = movie_info.get("title", "未知")
    overview = movie_info.get("overview", "無簡介")
    release_date = movie_info.get("release_date", "未知")
    rating = movie_info.get("vote_average", "無評分")
    
    # 返回格式化後的電影資訊
    return {
        "title": title,
        "overview": overview,
        "release_date": release_date,
        "rating": rating
    }

# 存儲電影資料到檔案
def save_movie_data(movie_info):
    """將電影資料儲存到 JSON 檔案"""
    # 設定檔案路徑
    folder_path = os.path.join("..", "data", "raw")
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "raw_data.json")
    
    with open(file_path, "a", encoding="utf-8") as file:
        json.dump(movie_info, file, ensure_ascii=False, indent=4)
        file.write("\n")
    
    print(f"電影資料已儲存至 {file_path}")

# 主程式
def scraper(llmmovie):
    movie_name = llmmovie
    movie_data = fetch_movie_data(movie_name)
    movie_info = parse_movie_data(movie_data)
    
    if isinstance(movie_info, dict):
        # 儲存資料
        save_movie_data(movie_info)

        return movie_info
        
    else:
        return None

if __name__ == "__main__":
    scraper()
from scripts.movie_llm import interact_with_user
from scripts.movie_scraper import scraper

def main():
    print("🎬 歡迎使用電影推薦與查詢系統 🎬")
    
    while True:
        # 讓使用者輸入偏好，並由 LLM 產生電影推薦
        serchmovie = interact_with_user()
        
        if not serchmovie:
            print("⚠️ 無法獲取電影名稱，請重新輸入您的偏好。")
            continue  # 重新詢問

        print(f"\n🔍 正在查詢電影：{serchmovie}...\n")
        
        # 調用爬蟲獲取電影資訊
        movie_info = scraper(serchmovie)
        print(movie_info)
        
        # 如果未找到電影資訊
        if movie_info is None:
            print("❌ 抱歉，未找到相關電影資訊。請嘗試其他電影或關鍵字。")
        else:
            print("\n🎥 電影資訊 📜")
            print("=" * 40)
            print(f"📌 電影名稱: {movie_info['title']}")
            print(f"📝 簡介: {movie_info['overview']}")
            print(f"📅 上映日期: {movie_info['release_date']}")
            print(f"⭐ 評分: {movie_info['rating']}")
            print("=" * 40)

        # 詢問使用者是否要繼續
        again = input("\n是否要繼續查詢？(y/n): ").strip().lower()
        if again != 'y':
            print("👋 感謝使用電影推薦系統，再見！")
            break  # 跳出迴圈，結束程式

if __name__ == "__main__":
    main()
# Movie Recommendation & Scraping System

這是一個基於 **LLM** 和 **爬蟲** 的電影推薦系統。用戶可以輸入關鍵字或電影名稱，並得到電影的相關資訊，包括簡介、上映日期和評分。系統使用 **LangChain** 來進行 LLM 的問答，並使用 **爬蟲** 從網頁抓取電影資料。


請輸入電影名稱: 羅密歐與茱麗葉
🔍 正在查詢電影：羅密歐與茱麗葉...
電影名稱: 羅密歐與茱麗葉
簡介: ...
上映日期: 1996-11-01
評分: 6.788

搜尋過的電影資訊會被儲存在data/raw裡
!注意 使用前請在key.env檔案裡輸入你的API_KEY(預設OPENAI)以及TMDB電影網取得的API_KEY
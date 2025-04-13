import os
import re
from dotenv import dotenv_values
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 設置 OpenAI API 金鑰
config = dotenv_values("key.env")
os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# 設定 LangChain 的提示模板
prompt_template = PromptTemplate(
    input_variables=["preferences"],
    template="請只提供一部符合以下偏好的電影名稱，不要其他描述: {preferences}",
    max_tokens = 50,
    stop=["》"] #當遇到 `》` 就停止輸出 抓取第一部電影後減少TOKEN數目
)

# 創建 LLMChain 實例
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

def recommend_movies_based_on_preferences(preferences):
    """根據用戶偏好推薦電影"""
    return llm_chain.run(preferences)

# 從推薦文本中提取電影標題
def extract_movie_title(recommendation_text):
    """從推薦的文本中提取電影標題"""
    match = re.search(r"[《“\"](.*?)[》”\"]|\((.*?)\)", recommendation_text)
    if match:
        return match.group(1)
    return recommendation_text

# 這是一個示範的交互式功能
def interact_with_user():
    """用來處理與用戶的交互"""
    print("歡迎來到電影推薦系統！")

    # 用戶給出電影偏好，並進行推薦
    preferences = input("\n請輸入您的電影偏好 (例如: 喜劇, 冒險, 由導演斯皮爾伯格執導，如果想要不同推薦可以多嘗試幾次): ")
    recommendations = recommend_movies_based_on_preferences(preferences)

    # 提取電影標題
    movie_title = extract_movie_title(recommendations)

    print(f"\n基於您的偏好，這是我們推薦的電影：\n{recommendations}")
    return movie_title #用於爬蟲

# ______________________________________________________________________________________
if __name__ == "__main__":
    interact_with_user()

import streamlit as st
import requests

st.set_page_config(page_title="MNQ 交易監控", layout="wide")
st.title("📊 MNQ 自動交易監控中心")

# --- 關鍵：請在這裡填入你的 Ngrok 網址 ---
# 注意：網址結尾一定要加上 /command
NGROK_URL = "https://dustin-loath-shemeka.ngrok-free.dev/command" 

# 模擬顯示數據
col1, col2, col3 = st.columns(3)
col1.metric("帳號餘額", "$50,250", "+250")
col2.metric("當日回撤", "-$120", "安全", delta_color="normal")
col3.metric("目前持倉", "1口 MNQ (多)")

st.divider()

st.subheader("遠端控制測試")
if st.button("🔴 發送緊急停損指令 (測試電腦彈窗)"):
    try:
        # 發送 POST 請求到你家電腦
        response = requests.post(NGROK_URL)
        if response.status_code == 200:
            st.success("指令已發送！請查看電腦螢幕。")
        else:
            st.error(f"電腦端回傳錯誤：{response.status_code}")
    except Exception as e:
        st.error(f"連線失敗：請檢查電腦 Ngrok 是否開啟。")

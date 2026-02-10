import streamlit as st

st.set_page_config(page_title="MNQ 交易監控", layout="wide")
st.title("📊 MNQ 自動交易監控中心")

# 模擬數據
col1, col2, col3 = st.columns(3)
col1.metric("帳號餘額", "$50,250", "+250")
col2.metric("當日回撤", "-$120", "安全", delta_color="normal")
col3.metric("目前持倉", "1口 MNQ (多)")

if st.button("🔴 緊急平倉測試 (傳送指令)"):
    st.warning("指令已發送至中繼伺服器...")

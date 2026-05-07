import streamlit as st

st.set_page_config(page_title="Smart Farming AI", layout="wide")

# ---------- LOAD CSS ----------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="header">🌾 Smart Farming AI Platform 🌾</div>', unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <h1>🌾🚜 Welcome to Smart Farming 🌾🚜</h1>
    <p>🌾 AI-powered solutions for modern agriculture 🌾</p>
</div>
""", unsafe_allow_html=True)

# ---------- CARDS ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h2>🌱 Crop Recommendation</h2>
        <p>Find the best crop based on soil & climate</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🌿 Open Crop Recommendation"):
        st.switch_page("pages/1_crop_recommendation.py")

with col2:
    st.markdown("""
    <div class="card">
        <h2>📊 Yield Prediction</h2>
        <p>Predict crop production using ML</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📈 Open Yield Prediction"):
        st.switch_page("pages/2_yield_prediction.py")

# ---------- FOOTER ----------
st.markdown('<div class="footer">© 2026 Smart Farming AI | Thakur Vansh Rana</div>', unsafe_allow_html=True)

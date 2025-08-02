import streamlit as st
import numpy as np
import joblib
import time
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        st.error(f"Error loading animation: {e}")
        return None

@st.cache_resource
def load_model_and_scaler():
    try:
        model = joblib.load("best_fire_detection_model.pkl")
        scaler = joblib.load("scaler.pkl")
        return model, scaler
    except Exception as e:
        st.error(f"🔧 Error loading model or scaler: {e}")
        return None, None

fire_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_urbk83vw.json")
satellite_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_cg3zkg.json")
model, scaler = load_model_and_scaler()

st.set_page_config(page_title="🚀 MODIS Fire Type Classifier", layout="wide")

st.markdown("""
    <style>
        .glow {
            font-size: 40px;
            color: #fff;
            text-align: center;
            text-shadow: 0 0 10px #FF7300, 0 0 20px #FF7300, 0 0 30px #FF7300;
        }
        .small {
            font-size: 18px;
            color: #ccc;
            text-align: center;
        }
        .stButton > button {
            background-color: #FF7300;
            color: white;
            border-radius: 8px;
            font-weight: bold;
            transition: 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #e65100;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 3])
with col1:
    if satellite_animation:
        st_lottie(satellite_animation, height=250)
with col2:
    st.markdown("<div class='glow'>🔥 MODIS Fire Type Classifier</div>", unsafe_allow_html=True)
    st.markdown("<div class='small'>Predicting fire types using satellite data — Vegetation, Static Land, or Offshore.</div>", unsafe_allow_html=True)

st.divider()

st.sidebar.header("🛰️ Satellite Sensor Readings")
st.sidebar.markdown("Simulate MODIS sensor inputs:")

brightness = st.sidebar.slider("🔥 Brightness", 270.0, 400.0, 310.0)
bright_t31 = st.sidebar.slider("🌡️ Brightness T31", 270.0, 320.0, 295.0)
frp = st.sidebar.slider("🚀 Fire Radiative Power (FRP)", 0.0, 100.0, 20.0)
scan = st.sidebar.slider("📡 Scan", 0.1, 2.0, 1.1)
track = st.sidebar.slider("🧭 Track", 0.1, 2.0, 1.0)
confidence = st.sidebar.selectbox("📈 Confidence Level", ["low", "nominal", "high"])

confidence_map = {"low": 0, "nominal": 1, "high": 2}
confidence_val = confidence_map[confidence]
input_data = np.array([[brightness, bright_t31, frp, scan, track, confidence_val]])

if st.button("🔍 Analyze & Predict"):
    if model and scaler:
        with st.spinner("🛰️ Analyzing MODIS data..."):
            if fire_animation:
                st_lottie(fire_animation, height=200)

            scaled_input = scaler.transform(input_data)
            prediction = model.predict(scaled_input)[0]

            fire_types = {
                0: ("🌿 Vegetation Fire", "#00C853"),
                2: ("🏜️ Static Land Source", "#FF9800"),
                3: ("🌊 Offshore Fire", "#03A9F4")
            }

            label, color = fire_types.get(prediction, ("❓ Unknown", "#616161"))

            st.markdown(f"""
                <div style='
                    background-color: {color};
                    padding: 20px;
                    border-radius: 12px;
                    text-align: center;
                    color: white;
                    font-size: 28px;
                    box-shadow: 0 0 10px {color};
                '>
                    ✅ Predicted Fire Type: <strong>{label}</strong>
                </div>
            """, unsafe_allow_html=True)

            st.success("🎯 Prediction Successful! Data analyzed.")
            st.balloons()
    else:
        st.error("Model or scaler not loaded correctly.")

st.divider()
st.markdown("📌 Developed by **Gamana Chirumamilla** | Powered by MODIS 🔭 + Machine Learning 🤖")

# 🔥 MODIS Satellite Data Fire Classification

A machine learning web app built using **Streamlit** that classifies fire types based on MODIS satellite sensor data.  
The app uses models trained on real MODIS fire datasets and allows users to enter values like brightness, temperature, and FRP to predict the fire type.

---

## 🚀 Features

- 🔍 Input satellite parameters to classify fire type  
- 🤖 Uses Random Forest Classifier with `SMOTE` for class balancing  
- 📊 Visuals and charts powered by `matplotlib`, `seaborn`  
- 🌍 Geospatial handling via `folium`  
- 🎨 Lottie animations using `streamlit-lottie`  
- 🖥️ Easy deployment via `streamlit run app.py`

---

## 🛠️ How to Run Locally

### 1. Clone this Repository

```bash
git clone https://github.com/gamana29/MODIS-Satellite-Data-Fire-Classification.streamlit.app.git
cd MODIS-Satellite-Data-Fire-Classification.streamlit.app

python -m venv venv
venv\Scripts\activate

pip install -r Requirements.txt

pip install streamlit pandas numpy scikit-learn matplotlib seaborn joblib folium imbalanced-learn streamlit-lottie

streamlit run app.py
```

📁 File Structure
bash
Copy
Edit

├── app.py                    # Main Streamlit app
├── best_fire_detection_model.pkl  # Trained Random Forest model
├── scaler.pkl               # Feature scaler used during training
├── Requirements.txt         # (Optional) Required dependencies


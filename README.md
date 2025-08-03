<<<<<<< HEAD
# MODIS-Satellite-Data
Deforestration (Fire Classification)
AICTE Internship Project

##Problem Statement
This project utilizes data from the Moderate Resolution Imaging Spectroradiometer (MODIS) sensors mounted on NASA’s Terra and Aqua satellites. The goal is to accurately predict and classify fire anomalies (deforestation, wildfires, and related events) using thermal data and contextual algorithms provided by MODIS.

##Satellite Sources
🌍 Terra Satellite

Observes land parameters

Captures data during the morning pass

Ideal for early fire detection over vegetation zones

🌊 Aqua Satellite

Measures water vapor, cloud properties, and additional surface parameters

Captures data during the afternoon pass

Useful for monitoring ongoing events and thermal shifts

Both satellites collect critical thermal anomaly data useful in environmental monitoring.

🔬 About MODIS Data
MODIS captures data in electromagnetic bands sensitive to thermal and spectral variations on Earth’s surface.

🔥 Key Bands Used:
Band 21: 3.929–3.989 μm – Shortwave infrared

Band 22: 3.929–3.989 μm – Similar to Band 21, used in comparison

Band 32: 11.770–12.270 μm – Thermal infrared, useful for detecting heat sources

These bands enable contextual detection of:

Vegetation fires

Volcanic activity

Static land sources (e.g., chemical explosions)

Tectonic anomalies (e.g., oceanic plate movement)

🧠 Project Goal
Build a robust machine learning model that leverages MODIS data to classify fire-related thermal anomalies and help in early warning systems and environmental monitoring.

🌍 Use Cases
🔔 Real-time Wildfire Alerts

🌾 Agricultural Burning Detection

🌳 Forest Fire Management & Response Planning

🌋 Volcanic Activity Surveillance

🌊 Oceanic Plate Movement Monitoring

🧰 Tools & Technologies
Python / Jupyter Notebooks

MODIS Data (Terra & Aqua)

Pandas / NumPy / Scikit-learn / XGBoost

Google Earth Engine (Optional)

Matplotlib / Seaborn (for visualization)

📈 Future Work
Integrate with Google Earth Engine or real-time APIs

Extend to include vegetation loss prediction models

Deploy a dashboard for alerts and visualization

Combine with weather forecast data for smarter predictions














=======
#  MODIS-Satellite-Data
### Deforestation (Fire Classification) – AICTE Internship Project

A Machine Learning project leveraging thermal anomaly data from MODIS sensors (NASA’s Terra and Aqua satellites) to classify fire events such as deforestation, wildfires, and volcanic activity.

---

##  Problem Statement

This project utilizes data from the Moderate Resolution Imaging Spectroradiometer (MODIS) on NASA’s **Terra** and **Aqua** satellites to:
- Detect thermal anomalies
- Predict fire types: **Vegetation Fires**, **Static Land Sources**, or **Offshore Events**
- Enable smarter environmental monitoring and alert systems

---

## 🛰️ Satellite Data Source

###  Terra Satellite
- Observes land parameters
- Morning pass
- Effective for early fire detection in vegetation zones

###  Aqua Satellite
- Measures water vapor, cloud & surface parameters
- Afternoon pass
- Tracks ongoing fire-related thermal anomalies

Both contribute to global fire anomaly detection.

---

## About MODIS Data

MODIS captures data across electromagnetic bands for thermal and spectral analysis.

**Key Bands Used**:
- **Band 21** (3.929–3.989 μm) – Shortwave IR
- **Band 22** (3.929–3.989 μm) – Redundant for consistency
- **Band 32** (11.770–12.270 μm) – Longwave thermal IR

These are crucial in detecting:
- 🌿 Vegetation fires
- 🌋 Volcanic activity
- 🧨 Chemical explosions
- 🌊 Oceanic plate anomalies

---

##  Project Goal

Build an ML model to classify fire anomalies from MODIS data, enabling:
- Real-time wildfire detection
- Forest management alerts
- Volcanic activity monitoring
- Integration with dashboards and APIs for field use

---

##  Use Cases

- Real-time Wildfire Alerts
- Agricultural Burning Detection
- Forest Fire Management & Response
- Volcanic Activity Surveillance
- Oceanic Plate Movement Monitoring

---

##  Tech Stack

| Component | Tools Used |
|----------|------------|
| Language | Python |
| ML Model | Scikit-learn |
| Data | MODIS (Terra & Aqua) |
| Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web UI | Streamlit |
| Deployment | GitHub / Localhost |

---

## Installation

Clone the repo:

```bash
git clone https://github.com/your-username/MODIS-Satellite-Data.git
cd MODIS-Satellite-Data
>>>>>>> b63ea7e4afc205bafae459cac3de23089c4adb0c

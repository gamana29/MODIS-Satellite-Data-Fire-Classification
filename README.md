#  MODIS-Satellite-Data
### Deforestation (Fire Classification) – AICTE Internship Project

A Machine Learning project leveraging thermal anomaly data from MODIS sensors (NASA’s Terra and Aqua satellites) to classify fire events such as deforestation, wildfires, and volcanic activity.

<img width="1910" height="929" alt="image" src="https://github.com/user-attachments/assets/50eddb0e-ff0d-41e0-bf07-05e5d10f2927" />


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

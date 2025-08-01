# MODIS-Satellite-data
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















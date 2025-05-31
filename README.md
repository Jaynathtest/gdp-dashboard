
# 📊 Cultural Tourism in India: A Data-Driven Streamlit Dashboard

This project explores the intersection of cultural heritage and tourism in India using interactive data visualizations built with **Streamlit** and powered by open government data.

## 🌏 Overview

India's diverse cultural landscape is a major driver of tourism. This dashboard highlights the **share of tourism in the Gross State Domestic Product (GSDP)** across Indian states and union territories, offering a data-first perspective to uncover patterns, underexplored cultural regions, and opportunities for responsible tourism development.

## 🚀 Features

- 📍 **State-wise tourism impact** visualization
- 📈 **Interactive bar charts** using Plotly
- 🧮 KPI cards showing highest, lowest, and average tourism contributions
- 🔍 Filterable and searchable data table
- 📦 Ready to deploy on **Streamlit Cloud** or **Snowflake**

## 🗃️ Dataset

- **Source:** [data.gov.in](https://data.gov.in)
- **Title:** Estimated share of tourism (direct + indirect) in GSDP of Indian States/UTs
- **File Used:** `RS Session 247 AS 7.1.csv`

## 🛠 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Visualization:** [Plotly](https://plotly.com/python/)
- **Data Processing:** [Pandas](https://pandas.pydata.org/)
- **Optional Backend:** [Snowflake](https://www.snowflake.com/)

## 🧪 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Jaynathtest/gdp-dashboard
   cd cultural-tourism-dashboard
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run streamlit_app.py
   ```

## 🌐 Deploy on Snowflake

If you’re using Snowflake’s Streamlit integration:

* Go to **Snowsight > Streamlit**
* Click **"Create App"**
* Paste the code into `streamlit_app.py` section
* Add dependencies via the environment editor
* Launch and explore your app natively inside Snowflake

## 📸 Screenshots

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/85b0ebbf-69da-4370-a5b5-91ec459f92bf" />
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/602594bf-a760-4fac-90f2-cb71c9525e8f" />
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/1031083c-1f36-4dcf-83cd-12ba6a38d35b" />


## 🧭 Future Improvements

* Integration with seasonal tourism datasets
* Cultural asset tagging by art form and festival
* Geospatial map views
* Responsible tourism metrics (sustainability, local impact)

Made with ❤️ for a Hackathon to celebrate India's cultural richness.


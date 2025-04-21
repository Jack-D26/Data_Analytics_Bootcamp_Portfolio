# F1 Drivers Performance Dashboard 🏎️📊

🔗 **[View the live app on Render →](https://software-dev-proyect-f1-app.onrender.com)** 

This project is a personal initiative focused on building a fully functional and interactive web application using **Streamlit**, powered by **real Formula 1 data**. It allows users to visually explore the performance of top F1 drivers from the year 2000 onwards.

---

## Objective

To practice software development tools and web deployment skills by turning exploratory data analysis into a clean, shareable, and engaging web app.

Key goals include:

- Processing and merging multiple raw F1 datasets
- Building dynamic visualizations with Plotly
- Deploying the final Streamlit app to the cloud using Render

This project demonstrates how to transform raw motorsport data into a usable web application with accessible insights. It combines data wrangling, storytelling through visuals, and full-stack deployment skills.

---

## Data Sources

The app uses public datasets covering F1 results from 1950 to 2024. These include:

- `driver_standings.csv`
- `drivers.csv`
- `races.csv`

These were merged using a custom script to create:

- `combined_driver_standings.csv`

---

## Features

The app allows users to:

- View a **horizontal bar chart** of the top 10 drivers by total points since 2000
- Select specific years to display **driver wins** using interactive checkboxes
- Track **cumulative points evolution** per driver using a year slider

All visualizations are interactive and responsive, built with Plotly.

---

## Project Structure

Software_Dev_Proyect_F1_app/ ├── app.py # Streamlit app code ├── data_processing.py # Script to generate the final dataset ├── data/ │ ├── driver_standings.csv │ ├── drivers.csv │ ├── races.csv │ └── combined_driver_standings.csv ├── notebooks/ │ └── EDA_F1.ipynb # Initial exploratory data analysis ├── requirements.txt ├── .gitignore └── README.md

---

## How to Run Locally

1. Clone this repository:

```bash
git clone https://github.com/Jack-D26/Software_Dev_Proyect_F1_app.git
cd Software_Dev_Proyect_F1_app
```

2. (Optional) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # On Mac/Linux
.\venv\Scripts\activate # On Windows

3. Install the required libraries:

pip install -r requirements.txt

4. Launch the Streamlit app:

streamlit run app.py

---

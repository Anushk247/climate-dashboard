# 🌍 Web-Based Climate Data Dashboard

## 📌 About The Project
Climate datasets stored in NetCDF (`.nc`) format are typically large, complex, and difficult to interpret without specialized, heavy tools. Non-experts often struggle to analyze and visualize this critical climate data. 

This project provides a **Web-Based Climate Dashboard** that transforms complex NetCDF files into accessible, interactive visualizations directly in the browser. It acts as a quick platform for exploring temperature, precipitation, and other climate trends without needing advanced technical expertise.

---

## 🚀 Key Features
1. **Dataset Upload:** Simple drag-and-drop or file selection to upload `.nc` files directly into the dashboard.
2. **Interactive Global Heatmap:** Explores spatial climate distribution with dynamic color mapping (contour plots).
3. **Time-Series Graph:** Analyzes historical climate trends (global averages) over time with interactive line plots.
4. **User-Friendly Interface:** Clean, intuitive UI built for fast rendering and easy exploration.

---

## 🛠️ Technology Stack
**Frontend:**
* HTML5 / CSS3
* JavaScript (Vanilla)
* Plotly.js (For interactive rendering of heatmaps and line charts)

**Backend:**
* Python 3.x
* Flask (Web framework for handling APIs and routing)
* Gunicorn (WSGI HTTP Server for deployment)

**Data Processing:**
* `xarray` & `netCDF4` (To read and parse multidimensional scientific data)
* `pandas` & `numpy` (For data manipulation and aggregation)

---

## 📂 Project Structure
```text
climate_dashboard/
│
├── application.py         # Main Flask backend file (Named application.py for AWS EB)
├── requirements.txt       # List of Python dependencies
├── README.md              # Project documentation
│
└── templates/             # MUST be named exactly 'templates' for Flask
    └── index.html         # Frontend UI and Plotly.js logic

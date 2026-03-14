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
├── app.py         # Main Flask backend file (Named application.py for AWS EB)
├── requirements.txt       # List of Python dependencies
├── README.md              # Project documentation
│
└── templates/             # MUST be named exactly 'templates' for Flask
    └── index.html         # Frontend UI and Plotly.js logic

---

💻 Local Setup Instructions (Step-by-Step)
Follow these steps to run the project on your own computer:

Step 1: Install Python
Ensure that Python is installed on your computer. You can download it from python.org.
(Important for Windows users: While installing, check the box that says "Add Python to PATH").

Step 2 : Install required python libraries mentioned in the requirement.txt

Step 2: Open Terminal
Open your project folder (climate_dashboard) in VS Code or Terminal.

Step 3: Create a Virtual Environment
Run this command to create an isolated environment for the project:

Bash
python -m venv venv
Step 4: Activate the Virtual Environment

Windows:

Bash
venv\Scripts\activate
Mac/Linux:

Bash
source venv/bin/activate
Step 5: Install Required Libraries
Install all the necessary packages using the requirements file:

Bash
pip install -r requirements.txt
Step 6: Run the Server
Start the backend server:

Bash
python application.py
Step 7: Open the Dashboard
Open your web browser and paste this exact link:
👉 http://127.0.0.1:5000

(Note: Do NOT double-click the index.html file to open it directly. It will cause a CORS error. Always use the local server link).

📖 How to Use the Dashboard
Ensure you have a .nc (NetCDF) file containing climate data.

Click the "Choose File" button on the dashboard and select your .nc file.

Click "Upload & Analyze".

Scroll down to view the Global Heatmap and Time-Series Plot. Use the interactive Plotly tools on the top right of the graphs to zoom and hover over data points.

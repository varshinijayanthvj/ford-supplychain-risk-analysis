AI-Powered Supply Chain Risk Analysis
Case Study: Ford Motor Company
Disclaimer: This project is a conceptual case study created for educational and portfolio purposes.
 It is not affiliated with or endorsed by Ford Motor Company.

1. Project Overview
Simulates supplier risk evaluation for a global manufacturer.
Predicts and visualizes supply chain vulnerabilities such as delays, shortages, and unreliable suppliers.
Provides real-time insights to help decision-makers choose safer suppliers.
Built as an interactive Streamlit dashboard.


2. Tech Stack
Python 
Pandas — Data processing
Matplotlib — Visualization
Streamlit — Dashboard interface
Faker — Sample data generation


3. Features
-Calculates risk scores for each supplier.
-Classifies suppliers into Low, Medium, High risk.
-Ranks suppliers based on risk score.
-Interactive filters for Material Type and Risk Level.
-Visual representation through bar charts.


4. Risk Score Calculation
Factors considered:
Reliability Score (0–1) — Based on past delivery performance.
Distance to Plant (km) — Logistics and delay potential.
Formula (simplified example):
Risk_Score = (1 - Reliability_Score) * 0.7 + (Distance_to_Plant / Max_Distance) * 0.3
Lower score indicates safer supplier.


5. Data Files
plants.csv
Contains Ford plant details: location, country, production capacity
suppliers.csv
Supplier information: name, material type, reliability, distance
supplier_risk.csv
Computed risk scores for all suppliers
supplier_ranking.csv
Suppliers ranked by safety (low to high risk)
app.py
Streamlit dashboard script
requirements.txt
List of Python libraries needed


6. Project Structure
Ford_SupplyChain_Project/
│
├─ data/
│   ├─ plants.csv
│   └─ suppliers.csv
│
├─ scripts/
│   ├─ data_generation.py
│   ├─ risk_logic.py
│   ├─ supplier_ranking.py
│   └─ visualization.py
│
├─ app.py
├─ requirements.txt
└─ README.md


7. How to Run
Clone the repository:
git clone https://github.com/varshinijayanthvj/ford-supplychain-risk.git
cd ford-supplychain-risk

Install dependencies:
pip install -r requirements.txt

Run the Streamlit dashboard:
streamlit run app.py

Open http://localhost:8501 in a web browser.


8. Future Enhancements
-Integration with live supplier data through APIs.
-AI-based predictive modeling for future shortages.
-Real-time alerts for high-risk suppliers.
-Deployment on cloud platforms for wider access.


9. Author
Varshini Jayanth
 AI & Data Science Enthusiast | CSE(AIML) Student | Aspiring Product Engineer
Email: varshinijayanthvj@gmail.com
LinkedIn Profile: https://www.linkedin.com/in/varshini-jayanth-90a6ab38b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

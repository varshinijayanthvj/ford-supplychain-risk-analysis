import pandas as pd
import os

# Load data
plants = pd.read_csv("data/plants.csv")
suppliers = pd.read_csv("data/suppliers.csv")

print("✅ Data loaded successfully!")
print(f"Plants: {len(plants)} rows | Suppliers: {len(suppliers)} rows")

# Add a random simulated risk score based on reliability and distance
risk_scores = []
for i, row in suppliers.iterrows():
    reliability = row["Reliability_Score"]
    distance = row["Distance_to_Plant_km"]
    # Basic formula: more distance = more risk, lower reliability = more risk
    risk = (1 - reliability) * 0.6 + (distance / 500) * 0.4
    risk_scores.append(round(risk, 3))

suppliers["Risk_Score"] = risk_scores

# Categorize risk
suppliers["Risk_Level"] = suppliers["Risk_Score"].apply(
    lambda x: "High" if x > 0.6 else ("Medium" if x > 0.4 else "Low")
)

# Save results
os.makedirs("data", exist_ok=True)
suppliers.to_csv("data/supplier_risk.csv", index=False)

print("✅ Supplier risk analysis completed and saved as supplier_risk.csv")

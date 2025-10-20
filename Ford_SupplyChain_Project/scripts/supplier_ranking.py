import pandas as pd
import os

# Load the risk data
risk_data_path = "data/supplier_risk.csv"

if not os.path.exists(risk_data_path):
    print("❌ Risk file not found! Please run risk_logic.py first.")
    exit()

suppliers = pd.read_csv(risk_data_path)

print("✅ Risk data loaded successfully!")
print(f"Suppliers: {len(suppliers)} rows")

# Rank suppliers based on Risk_Score (lower = better)
suppliers["Rank"] = suppliers["Risk_Score"].rank(method="dense", ascending=True).astype(int)

# Sort suppliers by rank
suppliers_sorted = suppliers.sort_values("Rank")

# Save final ranking
suppliers_sorted.to_csv("data/supplier_ranking.csv", index=False)

print("✅ Supplier ranking completed and saved as supplier_ranking.csv")

# Display top 5 safest suppliers
print("\n🏆 Top 5 Safest Suppliers:")
print(suppliers_sorted[["Supplier_ID", "Supplier_Name", "Risk_Score", "Risk_Level", "Rank"]].head())

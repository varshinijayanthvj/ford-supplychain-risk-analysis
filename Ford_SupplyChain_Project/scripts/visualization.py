import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the ranked suppliers
ranking_path = "data/supplier_ranking.csv"

if not os.path.exists(ranking_path):
    print("❌ Ranking file not found! Please run supplier_ranking.py first.")
    exit()

suppliers = pd.read_csv(ranking_path)

print("✅ Supplier ranking data loaded successfully!")

# Plot: Risk Score of Top 10 Suppliers
top_suppliers = suppliers.sort_values("Rank").head(10)

plt.figure(figsize=(10,6))
plt.bar(top_suppliers["Supplier_Name"], top_suppliers["Risk_Score"], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Supplier")
plt.ylabel("Risk Score")
plt.title("Top 10 Supplier Risk Scores")
plt.tight_layout()

# Save figure
os.makedirs("output", exist_ok=True)
plt.savefig("output/top10_supplier_risk.png")
plt.show()

print("✅ Visualization saved as output/top10_supplier_risk.png")

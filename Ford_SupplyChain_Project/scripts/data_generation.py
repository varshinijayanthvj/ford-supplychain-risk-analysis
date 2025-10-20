import pandas as pd
from faker import Faker
import random

# Initialize faker
fake = Faker()

# ---------- Generate Plant Data ----------
plants = []
for i in range(3):
    plant = {
        "Plant_ID": i + 1,
        "Plant_Name": fake.company(),
        "Location": fake.city(),
        "Country": fake.country(),
        "Production_Capacity": random.randint(5000, 20000)
    }
    plants.append(plant)

plants_df = pd.DataFrame(plants)
plants_df.to_csv("data/plants.csv", index=False)

# ---------- Generate Supplier Data ----------
suppliers = []
for i in range(10):
    supplier = {
        "Supplier_ID": i + 1,
        "Supplier_Name": fake.company(),
        "Material_Type": random.choice(["Aluminum", "Steel", "Semiconductors", "Plastic", "Rubber"]),
        "Reliability_Score": round(random.uniform(0.5, 1.0), 2),
        "Distance_to_Plant_km": random.randint(10, 500)
    }
    suppliers.append(supplier)

suppliers_df = pd.DataFrame(suppliers)
suppliers_df.to_csv("data/suppliers.csv", index=False)

print("✅ Data generated: plants.csv and suppliers.csv saved in /data folder.")

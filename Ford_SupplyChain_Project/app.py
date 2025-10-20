import streamlit as st
import pandas as pd

# Load supplier ranking data
suppliers = pd.read_csv("data/supplier_ranking.csv")

st.title("🚗 Ford Supplier Risk Dashboard")

# Sidebar filter: Material
materials = suppliers["Material_Type"].unique()
selected_material = st.sidebar.selectbox("Select Material", materials)

# Filter suppliers by selected material
filtered_suppliers = suppliers[suppliers["Material_Type"] == selected_material]

# Critical alert messages
if len(filtered_suppliers) == 0:
    st.warning(f"⚠️ No suppliers found for {selected_material}!")
elif all(risk == "High" for risk in filtered_suppliers["Risk_Level"]):
    st.error(f"❌ All suppliers for {selected_material} are HIGH risk! Immediate attention required.")

# Display bar chart of risk levels
risk_counts = filtered_suppliers["Risk_Level"].value_counts().reindex(["Low", "Medium", "High"], fill_value=0)
st.subheader(f"Risk Distribution for {selected_material}")

st.bar_chart(
    pd.DataFrame({
        "Risk Level": ["Low", "Medium", "High"],
        "Count": [risk_counts["Low"], risk_counts["Medium"], risk_counts["High"]]
    }).set_index("Risk Level")
)

# Supplier table
st.subheader(f"Suppliers for {selected_material}")
st.dataframe(filtered_suppliers[["Supplier_ID", "Supplier_Name", "Material_Type", "Risk_Score", "Risk_Level", "Rank"]])

# Top 5 safest suppliers
st.subheader("🏆 Top 5 Safest Suppliers (Overall)")
st.dataframe(suppliers.sort_values("Rank")[["Supplier_ID", "Supplier_Name", "Material_Type", "Risk_Score", "Risk_Level", "Rank"]].head())

import pandas as pd

def generate_gemini_summary(suppliers_df):
    summaries = []

    for _, row in suppliers_df.iterrows():
        if row["Risk_Level"] == "Low":
            summary = f"{row['Supplier_Name']} is reliable and safe. Minimal risk for Ford."
        elif row["Risk_Level"] == "Medium":
            summary = f"{row['Supplier_Name']} is somewhat risky. Monitor closely before major orders."
        else:  # High
            summary = f"{row['Supplier_Name']} is high-risk. Ford should consider alternatives."
        summaries.append(summary)

    suppliers_df["Gemini_Summary"] = summaries
    return suppliers_df

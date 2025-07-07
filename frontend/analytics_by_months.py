
import streamlit as st
from datetime import datetime
import requests
import pandas  as pd

API_URL = "https://expense-api-xyz.onrender.com"




def anlystics_months_tab():
    if st.button("Get Monthly Analytics"):
        response = requests.get(f"{API_URL}/month_analytics/")
        response = response.json()

        data = {
            "Month Name": list(response.keys()),
            "Total": [response[month]["total"] for month in response],
            "Percentage": [response[month]["percentage"] for month in response],
            "Month Number": [response[month]["month_number"] for month in response]
        }

        df = pd.DataFrame(data)
        df_stored = df.sort_values(by="Month Number", ascending=True)

        st.title("Expense Breakdown by Months")
        st.bar_chart(data=df_stored.set_index("Month Name")["Total"], width=0, height=0, use_container_width=True)

        df_stored["Total"] = df_stored["Total"].map("{:.2f}".format)
        df_stored["Percentage"] = df_stored["Percentage"].map("{:.2f}%".format)

        df_stored = df_stored.rename(columns={"month_number": ""})


        st.table(df_stored)



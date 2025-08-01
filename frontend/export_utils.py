import pandas as pd
import streamlit as st
import io


def download_df_as_excel(df, file_name="report.xlsx", button_label="Download Excel"):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    st.download_button(
        label=button_label,
        data=output.getvalue(),
        file_name=file_name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

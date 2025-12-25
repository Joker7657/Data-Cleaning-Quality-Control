import streamlit as st
import pandas as pd


st.set_page_config(page_title="Data Quality Dashboard", layout="wide")


st.title("📊 Data Cleaning & Validation Dashboard")


# Load data
valid_path = "data/processed/validos.csv"
invalid_path = "data/processed/rejeitados.csv"
report_path = "data/reports/validation_report.txt"


valid_df = pd.read_csv(valid_path) if str(valid_path) else None
invalid_df = pd.read_csv(invalid_path) if str(invalid_path) else None


# Metrics section
col1, col2 = st.columns(2)


col1.metric("Registros Válidos", len(valid_df))
col2.metric("Registros Rejeitados", len(invalid_df))


# Report section
st.subheader("📝 Relatório de Validação")
try:
    with open(report_path, "r") as f:
        report_text = f.read()
        st.code(report_text)
except:
    st.write("Relatório não encontrado. Execute primeiro o main.py")


# Tables section
st.subheader("✔️ Dados Validados")
st.dataframe(valid_df, use_container_width=True)


st.subheader("❌ Dados Rejeitados")
st.dataframe(invalid_df, use_container_width=True)
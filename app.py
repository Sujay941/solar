import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Power Generation Dashboard",
    page_icon="⚡",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Plant_1_Generation_Data.csv")
    return df

df = load_data()

# -------------------------
# Title
# -------------------------
st.title("⚡ Power Generation Analytics Dashboard")
st.markdown("Simple Streamlit Dashboard for Power Plant Data")

# -------------------------
# Data Preview
# -------------------------
st.subheader("Dataset Preview")
st.dataframe(df.head())

# -------------------------
# KPIs
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Records",
    len(df)
)

if "DC_POWER" in df.columns:
    col2.metric(
        "Total DC Power",
        f"{df['DC_POWER'].sum():,.0f}"
    )

if "AC_POWER" in df.columns:
    col3.metric(
        "Total AC Power",
        f"{df['AC_POWER'].sum():,.0f}"
    )

st.divider()

# -------------------------
# AC Power Distribution
# -------------------------
if "AC_POWER" in df.columns:

    st.subheader("AC Power Distribution")

    fig = px.histogram(
        df,
        x="AC_POWER",
        nbins=30,
        title="AC Power Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# DC Power Distribution
# -------------------------
if "DC_POWER" in df.columns:

    st.subheader("DC Power Distribution")

    fig2 = px.histogram(
        df,
        x="DC_POWER",
        nbins=30,
        title="DC Power Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# AC vs DC Power
# -------------------------
if "AC_POWER" in df.columns and "DC_POWER" in df.columns:

    st.subheader("AC Power vs DC Power")

    fig3 = px.scatter(
        df,
        x="DC_POWER",
        y="AC_POWER",
        title="Relationship Between AC and DC Power"
    )

    st.plotly_chart(fig3, use_container_width=True)

# -------------------------
# Summary Statistics
# -------------------------
st.subheader("Summary Statistics")
st.write(df.describe())

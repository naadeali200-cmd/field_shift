import streamlit as st
import pandas as pd
import base64

def set_background(path):
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)),
                              url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

set_background("dan-meyers-IQVFVH0ajag-unsplash.jpg.jpg")

st.title("SkySprout")
st.write("What should follow your wheat?")

st.header("A bigger heading")
st.markdown("Text with **bold** and *italics*")

choice = st.radio("What matters most?", ["Save water", "Rebuild soil", "Steady income"])
st.write("You picked:", choice)

amount = st.slider("How much rain change?", -40, 40, 0)
st.write("Rain change:", amount)

monthly = pd.read_csv("data/monthly_climate_full.csv", index_col=0, parse_dates=True)
st.dataframe(monthly.head())

rain = monthly.groupby(monthly.index.month)["PRECTOTCORR"].mean()
st.bar_chart(rain)
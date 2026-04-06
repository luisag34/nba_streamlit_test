"""
🏀 NBA Streamlit Test - ULTRA MINIMAL
Purpose: Test if Streamlit Cloud works at all
"""

import streamlit as st

st.set_page_config(page_title="NBA Test", layout="centered")

st.title("🏀 NBA Streamlit Test - ULTRA MINIMAL")
st.write("If you see this, Streamlit Cloud is working!")

# Simple test
name = st.text_input("Enter your name:", "Luis")
if st.button("Say hello"):
    st.success(f"Hello {name}! Streamlit works! 🎉")

# Display success
st.balloons()
st.success("✅ Streamlit Cloud deployment successful!")
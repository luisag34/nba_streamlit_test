"""
🏀 NBA Test - NO REQUIREMENTS VERSION
Testing if Streamlit Cloud works without requirements.txt
"""

import streamlit as st

st.set_page_config(page_title="NBA No-Req Test")

st.title("🏀 NBA Test - No Requirements")
st.write("Testing if Streamlit Cloud works WITHOUT requirements.txt")

# Remove requirements.txt if it exists
import os
if os.path.exists("requirements.txt"):
    st.warning("requirements.txt exists - this test may fail")
else:
    st.success("No requirements.txt found - good!")

# Simple test
st.success("If you see this, Streamlit works without pip install!")

st.info("""
This test removes the requirements.txt dependency.
If it works: Streamlit Cloud has issues with pip installation.
If it fails: Streamlit Cloud has broader issues.
""")
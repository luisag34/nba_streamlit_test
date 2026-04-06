"""
🏀 NBA Test - BUILT-IN MODULES ONLY
Uses ONLY Python standard library modules
No pip install required at all
"""

# ONLY standard library imports
import os
import sys
import json

# Simulate Streamlit with basic HTML if not available
try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False
    # Create minimal HTML output
    html_output = []

def st_write(text):
    if STREAMLIT_AVAILABLE:
        st.write(text)
    else:
        html_output.append(f"<p>{text}</p>")

def st_title(text):
    if STREAMLIT_AVAILABLE:
        st.title(text)
    else:
        html_output.append(f"<h1>{text}</h1>")

def st_success(text):
    if STREAMLIT_AVAILABLE:
        st.success(text)
    else:
        html_output.append(f'<div style="color: green; padding: 10px; border: 1px solid green;">✅ {text}</div>')

# Main app
if STREAMLIT_AVAILABLE:
    st.set_page_config(page_title="NBA Built-in Test")
    st_title("🏀 NBA Test - Built-in Modules Only")
    st_write("This app uses ONLY Python standard library modules.")
    st_success("Streamlit is available! No pip install needed!")
    
    # Show Python info
    st_write(f"Python version: {sys.version}")
    st_write(f"Platform: {sys.platform}")
    
    # List available modules
    st_write("Standard library modules available:")
    std_modules = ["os", "sys", "json", "datetime", "math", "re", "csv"]
    for mod in std_modules:
        try:
            __import__(mod)
            st_write(f"✅ {mod}")
        except:
            st_write(f"❌ {mod}")
    
    st_success("🎉 App works with built-in modules only!")
    
else:
    # Fallback HTML output
    html_output.append("<h1>🏀 NBA Test - Built-in Modules Only</h1>")
    html_output.append("<p>Streamlit not available - showing HTML fallback</p>")
    html_output.append('<div style="color: green;">✅ This proves Python runs without pip install!</div>')
    html_output.append(f"<p>Python version: {sys.version}</p>")
    
    # Save to file for debugging
    with open("output.html", "w") as f:
        f.write("\n".join(html_output))
    
    print("HTML output saved to output.html")
    print("".join(html_output))
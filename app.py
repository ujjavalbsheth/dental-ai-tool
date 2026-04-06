import streamlit as st
from crew_logic import run_analysis

st.title("🦷 Dental AI Planner")

age = st.number_input("Age", 1, 100)
complaint = st.text_input("Chief Complaint")
opg = st.text_area("OPG Findings")

if st.button("Analyze"):
    result = run_analysis({
        "age": age,
        "complaint": complaint,
        "opg_description": opg
    })
    st.write(result)

st.caption("For clinical decision support only")

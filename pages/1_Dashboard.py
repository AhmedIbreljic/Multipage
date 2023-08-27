import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data for student information
student_data = {
    "Major": "Electrical Engineering",
    "GPA": 3.8,
    "Advisor": "Dr. Smith",
    "Advisor Email": "smith@example.com",
    "Expected Graduation Date": "May 2024",
    "Degree Cost": "$50,000",
}

# Sample data for major breakdown
major_breakdown = {
    "Core Courses": 10,
    "General Education": 5,
    "Electives": 3,
}

# Calculate total credits
total_credits = sum(major_breakdown.values())

# Create a Plotly pie chart
fig = px.pie(
    names=list(major_breakdown.keys()),
    values=list(major_breakdown.values()),
    title="Major Breakdown",
)

# Streamlit app layout
st.set_page_config(page_title="Student Dashboard", page_icon="🎓")
st.markdown("# Student Dashboard")
st.sidebar.header("Student Dashboard")

# Display student information
st.write("### Student Information")
st.write(f"**Major:** {student_data['Major']}")
st.write(f"**GPA:** {student_data['GPA']}")
st.write(f"**Advisor:** {student_data['Advisor']}")
st.write(f"**Advisor Email:** {student_data['Advisor Email']}")
st.write(f"**Expected Graduation Date:** {student_data['Expected Graduation Date']}")
st.write(f"**Degree Cost:** {student_data['Degree Cost']}")

# Display major breakdown pie chart
st.write("### Major Breakdown")
st.plotly_chart(fig)

# Display student's progression towards their degree
st.write("### Student's Progression")
completed_credits = st.slider("Completed Credits", 0, total_credits, 90)
remaining_credits = total_credits - completed_credits
st.write(f"Completed Credits: {completed_credits}/{total_credits}")
st.progress(completed_credits / total_credits)

st.write("### Pathway")
# Pathway code goes here (you can modify the existing Pathway code you have)

# TreeSearch code goes here (you can modify the existing TreeSearch code you have)


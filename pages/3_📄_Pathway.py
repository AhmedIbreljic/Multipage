import streamlit as st
import pandas as pd
import altair as alt
import random

def electrical_engineering_degree():
    degree_data = {
        "Year 1": [
            {"Course": "Mathematics", "Credits": random.randint(3, 5), "Type": "Math"},
            {"Course": "Introduction to EE", "Credits": random.randint(3, 5), "Type": "EE"},
            {"Course": "Physics", "Credits": random.randint(3, 5), "Type": "Science"},
        ],
        "Year 2": [
            {"Course": "Circuit Analysis", "Credits": random.randint(3, 5), "Type": "EE"},
            {"Course": "Digital Logic Design", "Credits": random.randint(3, 5), "Type": "EE"},
            {"Course": "Signals and Systems", "Credits": random.randint(3, 5), "Type": "EE"},
        ],
        "Year 3": [
            {"Course": "Electromagnetics", "Credits": random.randint(3, 5), "Type": "EE"},
            {"Course": "Control Systems", "Credits": random.randint(3, 5), "Type": "EE"},
            {"Course": "Electronics", "Credits": random.randint(3, 5), "Type": "EE"},
        ],
        "Year 4": [
            {"Course": "Power Systems", "Credits": random.randint(3, 5), "Type": "EE"},
            {"Course": "Communication Systems", "Credits": random.randint(3, 5), "Type": "EE"},
            {"Course": "Senior Design Project", "Credits": random.randint(3, 5), "Type": "Project"},
        ],
    }

    st.write("### Electrical Engineering Undergraduate Degree Courses")

    df = pd.DataFrame([(year, course["Course"], course["Credits"], course["Type"]) for year, courses in degree_data.items() for course in courses],
                      columns=["Year", "Course", "Credits", "Type"])
    st.dataframe(df)

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Year:N", title="Year"),
        y=alt.Y("sum(Credits):Q", title="Total Credits"),
        color=alt.Color("Type:N", title="Course Classification",
                        scale=alt.Scale(scheme="category20")),
        tooltip=["Year", "sum(Credits)", "Type"]
    ).properties(
        title="Total Credits per Year"
    )

    st.write("### Total Credits per Year")
    st.altair_chart(chart, use_container_width=True)

st.set_page_config(page_title="Electrical Engineering Degree", page_icon="⚡")
st.markdown("# Electrical Engineering Degree")
st.sidebar.header("Electrical Engineering Degree")
st.write(
    """This demo showcases an example of an Electrical Engineering undergraduate degree with sample courses over four years. Courses are color-coded based on their classification."""
)

electrical_engineering_degree()

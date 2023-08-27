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

    course_data = []
    for year, courses in degree_data.items():
        for course in courses:
            course_data.append({"Year": year, "Course": course["Course"], "Credits": course["Credits"], "Type": course["Type"]})
    df = pd.DataFrame(course_data)
    
    pivot_df = df.pivot(index="Course", columns="Year", values=["Credits", "Type"]).reset_index()
    pivot_df.columns = ["Course"] + [f"{year[1]} {year[0]}" for year in pivot_df.columns[1:]]

    st.dataframe(pivot_df, index=False)

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("sum(Credits):Q", title="Total Credits"),
        y=alt.Y("Course:N", title="Course"),
        color=alt.Color("Type:N", title="Course Classification",
                        scale=alt.Scale(scheme="category20")),
        tooltip=["Course", "sum(Credits)", "Type"]
    ).properties(
        title="Total Credits per Course"
    )

    st.write("### Total Credits per Course")
    st.altair_chart(chart, use_container_width=True)

st.set_page_config(page_title="Electrical Engineering Degree", page_icon="⚡")
st.markdown("# Electrical Engineering Degree")
st.sidebar.header("Electrical Engineering Degree")
st.write(
    """This demo showcases an example of an Electrical Engineering undergraduate degree with sample courses over four years. Courses are color-coded based on their classification. The table displays courses horizontally based on the year they belong in."""
)

electrical_engineering_degree()

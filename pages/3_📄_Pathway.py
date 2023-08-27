import streamlit as st
import pandas as pd
import altair as alt

def electrical_engineering_degree():
    degree_data = {
        "Year 1": ["Mathematics", "Introduction to Electrical Engineering", "Physics"],
        "Year 2": ["Circuit Analysis", "Digital Logic Design", "Signals and Systems"],
        "Year 3": ["Electromagnetics", "Control Systems", "Electronics"],
        "Year 4": ["Power Systems", "Communication Systems", "Senior Design Project"],
    }

    st.write("### Electrical Engineering Undergraduate Degree Courses")

    degree_df = pd.DataFrame(degree_data)
    st.dataframe(degree_df)

    melted_df = pd.melt(degree_df, var_name="Year", value_name="Course")
    chart = alt.Chart(melted_df).mark_bar().encode(
        x="Year:N",
        y="count()",
        color="Year:N",
        column="Year:N",
        tooltip="Course",
    )

    st.write("### Course Distribution Over Four Years")
    st.altair_chart(chart, use_container_width=True)

st.set_page_config(page_title="Electrical Engineering Degree", page_icon="⚡")
st.markdown("# Electrical Engineering Degree")
st.sidebar.header("Electrical Engineering Degree")
st.write(
    """This demo showcases an example of an Electrical Engineering undergraduate degree with sample courses over four years."""
)

electrical_engineering_degree()

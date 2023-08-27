import streamlit as st
import itertools
import plotly.express as px

def treesearch_demo():
    st.write("### Electrical Engineering Degree Tree Search")
    
    # Dummy course data (replace this with your actual course data)
    course_data = [
        {"Course": f"Course {i}", "Credits": 3 + i % 3} for i in range(45)
    ]
    
    total_credits_required = 126
    max_years = 4
    
    # Generate all possible combinations of courses
    combinations = []
    for r in range(1, len(course_data) + 1):
        combinations.extend(itertools.combinations(course_data, r))
    
    # Filter valid combinations based on total credits and years
    valid_combinations = []
    for combo in combinations:
        total_credits = sum(course["Credits"] for course in combo)
        years = len(combo)
        if total_credits >= total_credits_required and years <= max_years:
            valid_combinations.append(combo)
    
    # Create a Plotly figure
    fig = px.scatter(
        valid_combinations,
        x=[len(combo) for combo in valid_combinations],
        y=[sum(course["Credits"] for course in combo) for combo in valid_combinations],
        labels={"x": "Number of Courses", "y": "Total Credits"},
        title="Possible Combinations of EE Courses"
    )
    
    # Add constraint lines
    fig.add_hline(y=total_credits_required, line_dash="dash", line_color="green", name=f"{total_credits_required} Credits")
    fig.add_vline(x=max_years * 4, line_dash="dash", line_color="red", name=f"{max_years} Years")
    
    st.plotly_chart(fig)

    st.write(
        """This plot shows all possible combinations of Electrical Engineering courses for students to graduate in 4 years or less. Each point represents a combination with the number of courses on the x-axis and the total credits on the y-axis. The red dashed line represents the 4-year constraint, and the green dashed line represents the 126-credit constraint."""
    )

# Streamlit app layout
st.set_page_config(page_title="Tree Search Demo", page_icon="🌳")
st.markdown("# Tree Search Demo")
st.sidebar.header("Tree Search Demo")
st.write(
    """This demo generates all possible combinations of Electrical Engineering courses for students to graduate in 4 years or less. The total number of courses is 45, and the required credit amount is 126."""
)

treesearch_demo()

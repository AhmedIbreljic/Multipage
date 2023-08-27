import streamlit as st
import itertools

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
    
    # Display the plot using Streamlit's native plotting capabilities
    chart = st.line_chart(
        {
            "Number of Courses": [len(combo) for combo in valid_combinations],
            "Total Credits": [sum(course["Credits"] for course in combo) for combo in valid_combinations],
        }
    )
    
    chart.axhline(y=total_credits_required, color='green', linestyle='--', label=f'{total_credits_required} Credits')
    chart.axvline(x=max_years * 4, color='red', linestyle='--', label=f'{max_years} Years')
    chart.set_xlabel("Number of Courses")
    chart.set_ylabel("Total Credits")
    chart.set_title("Possible Combinations of EE Courses")
    chart.legend()
    
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

import itertools
import matplotlib.pyplot as plt

# Constants
TOTAL_COURSES = 45
TOTAL_CREDITS = 126
MAX_YEARS = 4

# Dummy course data (replace this with your actual course data)
course_data = [
    {"Course": f"Course {i}", "Credits": 3 + i % 3} for i in range(TOTAL_COURSES)
]

# Generate all possible combinations of courses
combinations = []
for r in range(1, TOTAL_COURSES + 1):
    combinations.extend(itertools.combinations(course_data, r))

# Filter valid combinations based on credit and years
valid_combinations = [
    combo for combo in combinations if
    sum(course["Credits"] for course in combo) >= TOTAL_CREDITS and
    len(combo) <= MAX_YEARS * 4
]

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(
    [len(combo) for combo in valid_combinations],
    [sum(course["Credits"] for course in combo) for combo in valid_combinations],
    c='blue'
)
plt.axvline(x=MAX_YEARS * 4, color='red', linestyle='--', label=f'{MAX_YEARS} Years')
plt.axhline(y=TOTAL_CREDITS, color='green', linestyle='--', label=f'{TOTAL_CREDITS} Credits')
plt.xlabel('Number of Courses')
plt.ylabel('Total Credits')
plt.title('Possible Combinations of EE Courses')
plt.legend()
plt.grid()
plt.show()

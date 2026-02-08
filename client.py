from models import StudentProfile
from server import calculate_grade_average

profile = StudentProfile(
    name="Srinath",
    id=101,
    grades=[80, 90, 85]
)

print("Average:", calculate_grade_average(profile))

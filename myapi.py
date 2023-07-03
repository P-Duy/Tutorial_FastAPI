from fastapi import FastAPI, Path

app = FastAPI()

students = {1: {"name": "John", "age": 17, "class": "year 12"}}


@app.get("/")
def index():
    return {"name": "first_name"}


@app.get("/get-students/{student_id}")
def get_students(
    student_id: int = Path(
        ..., description="The ID of the students you want to views", gt=0, lt=3
    )
):
    return students[student_id]

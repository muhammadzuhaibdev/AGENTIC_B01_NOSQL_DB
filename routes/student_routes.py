from fastapi import APIRouter
from pydantic import BaseModel
from bson.objectid import ObjectId
from config.db_connection import db

studentRouter = APIRouter()

sutudentCollection = db["students"]

class Student(BaseModel):
    studentName: str
    studentEmail: str
    studentAge: int

@studentRouter.post("/create")
def create_student(studentData: Student):
    try:
        print("Create Student API Called!")
        db_data = sutudentCollection.insert_one(
            {
                "studentName": studentData.studentName,
                "studentEmail": studentData.studentEmail,
                "studentAge": studentData.studentAge,
            }
        )

        return {
            "status": "success",
            "data": {
                "id": str(db_data.inserted_id),
                "name": studentData.studentName,
                "email": studentData.studentEmail,
                "age": studentData.studentAge,
            },
            "message": "Student Created Successfully!",
        }
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e),
        }


@studentRouter.get("/get")
def get_students():
    try:
        studentsData = list(sutudentCollection.find())

        for student in studentsData:
            student["_id"] = str(student["_id"])

        return {
            "status": "success",
            "data": studentsData,
            "message": "Student Data Fetched Successfully!",
        }
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e),
        }


@studentRouter.get("/search/{age}")
def search_students(age: str):
    try:
        studentsData = list(sutudentCollection.find({"studentEmail": age}))

        for student in studentsData:
            student["_id"] = str(student["_id"])

        return {
            "status": "success",
            "data": studentsData,
            "message": "Student Data Fetched Successfully!",
        }

    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e),
        }


@studentRouter.put("/update/{id}")
def update_student(id: str, newData: Student):
    try:
        updated_data = newData.dict()

        sutudentCollection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})

        student = sutudentCollection.find_one({"_id": ObjectId(id)})
        student["_id"] = str(student["_id"])

        return {
            "status": "success",
            "data": student,
            "message": "Student Updated Successfully!",
        }

    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e),
        }


@studentRouter.delete("/delete/{id}")
def delete_student(id: str):
    try:
        sutudentCollection.delete_one({"_id": ObjectId(id)})

        return {"status": "success", "message": "Student Deleted Successfully!"}
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e),
        }
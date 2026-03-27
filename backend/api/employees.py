from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.db.models import Employee

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/")
def get_all_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.post("/")
def add_employee(data: dict, db: Session = Depends(get_db)):
    emp = Employee(**data)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

@router.put("/{employee_id}/depart")
def mark_departed(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp.status = "departed"
    db.commit()
    return {"message": f"{emp.name} marked as departed"}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.db.models import AuditLog

router = APIRouter(prefix="/agents", tags=["Agents"])

@router.get("/audit-log")
def get_audit_log(db: Session = Depends(get_db)):
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).limit(50).all()
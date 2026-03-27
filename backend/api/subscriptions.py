from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.db.models import Subscription

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])

@router.get("/")
def get_all_subscriptions(user_id: int, db: Session = Depends(get_db)):
    return db.query(Subscription).filter(Subscription.user_id == user_id).all()

@router.get("/{subscription_id}")
def get_subscription(subscription_id: int, db: Session = Depends(get_db)):
    sub = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return sub

@router.post("/")
def create_subscription(data: dict, db: Session = Depends(get_db)):
    sub = Subscription(**data)
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return sub

@router.delete("/{subscription_id}")
def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    sub = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")
    db.delete(sub)
    db.commit()
    return {"message": "Subscription deleted"}
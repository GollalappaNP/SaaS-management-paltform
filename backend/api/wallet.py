from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.db.models import WalletLedger

router = APIRouter(prefix="/wallet", tags=["Wallet"])

@router.get("/{user_id}")
def get_wallet(user_id: int, db: Session = Depends(get_db)):
    wallet = db.query(WalletLedger).filter(WalletLedger.user_id == user_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet

@router.post("/deposit")
def deposit(user_id: int, amount: float, db: Session = Depends(get_db)):
    wallet = db.query(WalletLedger).filter(WalletLedger.user_id == user_id).first()
    if not wallet:
        wallet = WalletLedger(user_id=user_id, balance=amount)
        db.add(wallet)
    else:
        wallet.balance += amount
    db.commit()
    db.refresh(wallet)
    return wallet
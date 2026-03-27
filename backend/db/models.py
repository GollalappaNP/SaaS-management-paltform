from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db.database import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id                = Column(Integer, primary_key=True, index=True)
    user_id           = Column(Integer, nullable=False)
    vendor_name       = Column(String, nullable=False)
    amount            = Column(Float, nullable=False)
    billing_frequency = Column(String)
    next_renewal_date = Column(DateTime)
    category          = Column(String)
    status            = Column(String, default="active")
    waste_score       = Column(Float, default=0.0)
    source            = Column(String)
    detected_at       = Column(DateTime, default=datetime.utcnow)
    last_updated      = Column(DateTime, default=datetime.utcnow)


class UsageLog(Base):
    __tablename__ = "usage_logs"

    id              = Column(Integer, primary_key=True, index=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"))
    user_id         = Column(Integer, nullable=False)
    last_login      = Column(DateTime)
    login_count_30  = Column(Integer, default=0)
    login_count_60  = Column(Integer, default=0)
    login_count_90  = Column(Integer, default=0)
    active_seats    = Column(Integer, default=0)
    paid_seats      = Column(Integer, default=0)
    recorded_at     = Column(DateTime, default=datetime.utcnow)


class WalletLedger(Base):
    __tablename__ = "wallet_ledger"

    id              = Column(Integer, primary_key=True, index=True)
    user_id         = Column(Integer, nullable=False)
    balance         = Column(Float, default=0.0)
    interest_earned = Column(Float, default=0.0)
    last_updated    = Column(DateTime, default=datetime.utcnow)


class Payment(Base):
    __tablename__ = "payments"

    id              = Column(Integer, primary_key=True, index=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"))
    user_id         = Column(Integer, nullable=False)
    amount          = Column(Float, nullable=False)
    status          = Column(String, default="pending")
    due_date        = Column(DateTime)
    executed_at     = Column(DateTime)
    retry_count     = Column(Integer, default=0)


class Employee(Base):
    __tablename__ = "employees"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    email       = Column(String, unique=True, nullable=False)
    role        = Column(String)
    department  = Column(String)
    status      = Column(String, default="active")
    joined_at   = Column(DateTime, default=datetime.utcnow)
    departed_at = Column(DateTime, nullable=True)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id         = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String)
    action     = Column(String)
    details    = Column(Text)
    status     = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
"""
SQLAlchemy database models
"""
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    """User model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Document(Base):
    """Document analysis record"""
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    document_type = Column(String, index=True)
    source_language = Column(String)
    target_language = Column(String)
    original_text = Column(Text)
    translated_text = Column(Text)
    key_info = Column(JSON)
    confidence_score = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Feedback(Base):
    """User feedback"""
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    rating = Column(Integer)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

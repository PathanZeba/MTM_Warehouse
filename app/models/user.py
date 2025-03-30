from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from app import db



class User(UserMixin, db.Model):
    __tablename__ = "Users"
    __table_args__ = {"schema": "dbo"}

    Id = db.Column(UNIQUEIDENTIFIER, primary_key=True, default=lambda: str(uuid.uuid4()))
    Username = db.Column(db.String(255), unique=True, nullable=False)
    NormalizedUsername = db.Column(db.String(255), unique=True, nullable=True)
    Email = db.Column(db.String(255), unique=True, nullable=True)
    NormalizedEmail = db.Column(db.String(255), unique=True, nullable=True)
    EmailConfirmed = db.Column(db.Boolean, default=False, nullable=False)
    PasswordHash = db.Column(db.String(512), nullable=False)
    SecurityStamp = db.Column(db.String(255), nullable=True)
    ConcurrencyStamp = db.Column(db.String(255), nullable=True)
    PhoneNumber = db.Column(db.String(20), nullable=True)
    PhoneNumberConfirmed = db.Column(db.Boolean, default=False, nullable=False)
    TwoFactorEnabled = db.Column(db.Boolean, default=False, nullable=False)
    LockoutEnd = db.Column(db.DateTime, nullable=True)
    LockoutEnabled = db.Column(db.Boolean, default=True, nullable=False)
    AccessFailedCount = db.Column(db.Integer, default=0, nullable=False)

    def get_id(self):
        """Flask-Login ke liye UUID ko string mein convert karega"""
        return str(self.Id)

    def set_password(self, password):
        """Hash and set the password."""
        self.PasswordHash = generate_password_hash(password)

    def check_password(self, password):
        """Verify the password against stored hash."""
        return check_password_hash(self.PasswordHash, password)

    def __repr__(self):
        return f"<User {self.Username}>"

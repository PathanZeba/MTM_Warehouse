from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class LoginEmp(db.Model, UserMixin):
    __tablename__ = "Login_Emp"
    __table_args__ = {"schema": "dbo"}
    
    Id = Column(Integer, primary_key=True)
    Name = Column(String(30), nullable=True)
    Email = Column(String(255), unique=True, nullable=True)
    Role = Column(String(255), nullable=True)
    Username = Column(String(255), unique=True, nullable=True)
    Password_Hash = Column(String(255), nullable=False)

    # Password Hashing Methods
    def set_password(self, password):
        self.Password_Hash = generate_password_hash(password, method="pbkdf2:sha256", salt_length=16)

    def check_password(self, password):
        return check_password_hash(self.Password_Hash, password)

    # Foreign Key linking to WarehouseInfo
    Warehouse_Info_Id = Column(Integer, ForeignKey("dbo.Warehouse_Info.Warehouse_Info_Id", ondelete="SET NULL"))

    # Relationships
    warehouse_info = db.relationship(
        "WarehouseInfo",
        back_populates="warehouse_info_login_emp",
        overlaps="warehouse_info_login_emp,login_emps"
    )
    def __repr__(self):
        return f"<LoginEmp {self.Username}, Role: {self.Role}>"

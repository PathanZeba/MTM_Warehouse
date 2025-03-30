from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db  # Ensure `db` is initialized in your app

# models/emp_data.py
class EmpData(db.Model):
    __tablename__ = 'Emp_Data'
    __table_args__ = {'schema': 'dbo'}

    Emp_Data_Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Position = db.Column(db.String(100), nullable=False)
    Salary = db.Column(db.Float, nullable=False)

    Warehouse_Info_Id = db.Column(db.Integer, db.ForeignKey('dbo.Warehouse_Info.Warehouse_Info_Id'))
    def __repr__(self):
        return f"<EmpData {self.Name}, Position: {self.Position}>"

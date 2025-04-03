from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class WarehouseInfo(db.Model):
    __tablename__ = 'Warehouse_Info'
    __table_args__ = {'schema': 'dbo'}
    

    Warehouse_Info_Id = db.Column(db.Integer, primary_key=True)
    W_Name = db.Column(db.String, nullable=False)
    W_Location = db.Column(db.String, nullable=False)
    W_Pincode = db.Column(db.String, nullable=False)
    W_Total_capacity = db.Column(db.Float, nullable=False)
    W_Space_Available = db.Column(db.Float)
    W_Percent_Full = db.Column(db.Float)

    warehouse_items = db.relationship('WarehouseItems', backref='Warehouse_Info')
    emp_data = db.relationship('EmpData', backref='Warehouse_Info', lazy=True)
    
    
    warehouse_info_login_emp = db.relationship(
        "LoginEmp",
        back_populates="warehouse_info",
        overlaps="warehouse_info_login_emp,login_emps"
    )
    
    def __repr__(self):
        return f"<Warehouse {self.W_Name}, Location: {self.W_Location}>"

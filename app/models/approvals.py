from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class Approvals(db.Model):
    __tablename__ = 'Approvals'
    __table_args__ = {'schema': 'dbo'}

    Id = db.Column(db.String(255), primary_key=True)
    Applicant_Id = db.Column(db.String(255), nullable=False)
    Applicant_Name = db.Column(db.String(255), nullable=False)
    Message = db.Column(db.String(1000), nullable=False)
    Approval_job = db.Column(db.String(255), nullable=False)

    Login_Emp_Id = db.Column(Integer, db.ForeignKey('dbo.Login_Emp.Id'), nullable=True)
    Approval_Jobs_Id = db.Column(Integer, db.ForeignKey('dbo.Approval_Jobs.Id'), nullable=False)

    login_emp = db.relationship('LoginEmp')
    

    def __repr__(self):
        return f"<Approvals {self.Applicant_Name}, Job: {self.Approval_Jobs_Id}>"
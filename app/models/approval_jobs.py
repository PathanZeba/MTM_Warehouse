# models/approval_jobs.py
from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class ApprovalJobs(db.Model):
    __tablename__ = 'Approval_Jobs'
    __table_args__ = {'schema': 'dbo'}

    Id = db.Column(db.Integer, primary_key=True)
    Transport_Item = db.Column(db.String(255), nullable=False)
    Item_Space = db.Column(db.String(255), nullable=False)
    From_Warehouse = db.Column(db.String(255), nullable=False)
    To_Warehouse = db.Column(db.String(255), nullable=False)
    Item_Quantity = db.Column(db.String(255), nullable=False)
    Approval_Status = db.Column(db.String(255), nullable=False)

    Job_Progress_Id = Column(Integer, ForeignKey('dbo.Job_Progress.Job_Progress_Id'), nullable=True)

    job_progress = relationship('JobProgress', backref='Approval_Jobs')
    approvals = relationship('Approvals', backref='Approval_Jobs', uselist=False)

    def __repr__(self):
        return f"<ApprovalJobs {self.id}, Status: {self.Approval_Status}>"
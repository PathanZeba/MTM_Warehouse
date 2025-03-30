# models/job_progress.py
from app import db
from sqlalchemy.orm import relationship

class JobProgress(db.Model):
    __tablename__ = 'Job_Progress'
    __table_args__ = {'schema': 'dbo'}

    Job_Progress_Id = db.Column(db.Integer, primary_key=True)
    Progress_Status = db.Column(db.String, nullable=False)

    

    def __repr__(self):
        return f"<JobProgress {self.Progress_Status}>"
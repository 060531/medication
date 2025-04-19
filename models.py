from datetime import datetime
from app import db

class AccessLog(db.Model):
    __tablename__ = 'access_logs'

    id          = db.Column(db.Integer, primary_key=True)
    timestamp   = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    endpoint    = db.Column(db.String(128),  nullable=False)
    method      = db.Column(db.String(8),    nullable=False)
    remote_addr = db.Column(db.String(45))
    user_agent  = db.Column(db.String(256))

    def __repr__(self):
        return f'<AccessLog {self.id} {self.endpoint}>'

import datetime as dt

from voip.app import db

class Commands(db.Model):
    __tablename__ = 'commands'

    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(300), index=True)

    delivered = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    delivered_at = db.Column(db.DateTime)


    def __repr__(self):
        return '<Command: {}>'.format(self.command)

    def __init__(self, command, **kwargs):
        db.Model.__init__(self, command=command, **kwargs)

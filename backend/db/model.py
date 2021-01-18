from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Student(db.Model):
    '''
        學生名單
    '''
    id = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)  # 學號
    name = db.Column(db.String(10), unique=True, nullable=False)  # 姓名
    department = db.Column(db.String(7), unique=False, nullable=False)  # 系級
    phone = db.Column(db.String(10), unique=False, nullable=True)  # 手機號碼
    
    members = db.relationship(
        'Member',
        backref='student',
        lazy='dynamic'
    )
    
    def __init__(self, id, name, department, phone=None):
        self.id = id
        self.name = name
        self.department = department
        self.phone = phone
        
    def __repr__(self):
        return f'{self.__class__.__name__}: {self.id} ({self.name})'
    

class Committee(db.Model):
    '''
        委別
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    level = db.Column(db.Integer, nullable=True)
    
    clubs = db.relationship(
        'Club', 
        backref='committee', 
        lazy='dynamic'
    )

    def __init__(self, id, name, level=None):
        self.id = id
        self.name = name
        self.level = level

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.id} ({self.name}), level: {self.level}'


class Club(db.Model):
    '''
        社團
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    committee_id = db.Column(db.Integer, db.ForeignKey('committee.id'))
    
    members = db.relationship(
        'Member',
        backref = 'club', 
        lazy = 'dynamic'
    )

    def __init__(self, name, committee_id):
        self.name = name
        self.committee_id = committee_id

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.id} ({self.name}), committee: {self.committee_id}'
    

class Job(db.Model):
    '''
        社團內職位
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    level = db.Column(db.Integer, nullable=True)
    
    members = db.relationship(
        'Member',
        backref='job',
        lazy='dynamic'
    )

    def __init__(self, name, level=None):
        self.name = name
        self.level = level

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.id} ({self.name}), level: {self.level}'
    

class Member(db.Model):
    '''
        社團成員
        學生與社團關聯
    '''
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(10), db.ForeignKey('student.id'))
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))

    def __init__(self, student_id, club_id, job_id):
        self.student_id = student_id
        self.club_id = club_id
        self.job_id = job_id

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.id} ({self.name}), level: {self.level}'

from db.model import db, Club, Student, Indentity

def add(student_id, club_id, student_name, club_name, departments, job):

    if Student.query.filter_by(std_id = student_id).first() == None:
        student = Student(std_id = student_id, department = departments, name = student_name)
    else:
        student = Student.query.filter_by(name = student_name).first()

    if Club.query.filter_by(name = club_name).first() == None:
        club = Club(club_id = club_id, name = club_name)
    else:
        club = Club.query.filter_by(name = club_name).first()

    indentity = Indentity(job = job)

    club.indentitys.append(indentity)
    student.indentitys.append(indentity)
    db.session.add(club)
    db.session.add(student)
    db.session.add(indentity)
    db.session.commit()

def delete(student_id, club_id, job):

    delete_data = Indentity.query.filter_by(std_id = student_id, club_id = club_id, job = job).first()
    db.session.delete(delete_data)
    db.session.commit()


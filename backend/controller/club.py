from db.model import *
# import json

class ClubController:
    @staticmethod
    def get_club(student_id, club_id):
        member = Member.query.filter_by(student_id=student_id, club_id=club_id).first()
        if not member:
            return -1
        
        if member.job.level == 0:
            return -1
        
        club = Club.query.filter_by(id=club_id).first()
        
        member_list = []
        for m in Member.query.filter_by(club_id=club_id):
            member_list.append({
                'id': m.student.id,
                'name': m.student.name,
                'department': m.student.department,
                'phone': m.student.phone,
                'job': {
                    'id': m.job.id,
                    'name': m.job.name,
                    'level': m.job.level
                }
            })
            
        return {
            'id': club.id,
            'name': club.name,
            'committee_id': club.committee_id,
            'members': member_list
        }        
        
    @staticmethod
    def get_clubs(student_id):
        manage_clubs = []
        join_clubs = []
        for member in Member.query.filter_by(student_id=student_id).all():
            c = Club.query.filter_by(id=member.club_id).first()
            if c:
                if member.job.level > 0:
                    manage_clubs.append({
                        'id': c.id,
                        'name': c.name,
                        'committee_id': c.committee_id
                    })
                else:
                    join_clubs.append({
                        'id': c.id,
                        'name': c.name,
                        'committee_id': c.committee_id
                    })
        
        clubs = {}
        for committee in Committee.query.all():
            tmp = []
            for c in Club.query.filter_by(committee_id=committee.id).all():
                tmp.append({
                    'id': c.id,
                    'name': c.name,
                    'committee_id': c.committee_id
                })
            clubs[committee.name] = tmp
        
        return {
            'manage': manage_clubs,
            'join': join_clubs,
            'clubs': clubs
        }

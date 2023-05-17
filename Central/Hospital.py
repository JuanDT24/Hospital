from System.Team import Team
from Person.Doctor import ConsultantDoctor
from System.Ward import Ward
class Hospital:
    def __init__(self) -> None:
        self.__teams=[]
        self.__wards=[]

def add_team(self , consultant_doctor_id: int, team_id) -> None:
    Team=Team(team_id)
    ConsultantDoctor=ConsultantDoctor(consultant_doctor_id, Team)
    self.__teams.append(Team)
def add_junior_doctor(self, team:"Team", junior_doctor_id: int) -> None:
    JuniorDoctor=JuniorDoctor(junior_doctor_id, team)
def get_team(self, id: int) -> Team:
    for team in self.__teams:
        if team.id==id:
            return team
def add_ward(self, ward_id: int) -> None:
    Ward=Ward(ward_id)
    self.__wards.append(Ward)

def add_patient(self, ward: Ward, team:Team , patient_id: int):
    Patient=Patient(patient_id)
    ward.add_patient(Patient)
    team.add_patient(Patient)
    

        

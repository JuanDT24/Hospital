from __future__ import annotations
from System.Team import Team
from System.Ward import Ward
class Patient():
    def __init__(self, id, team:"Team", Ward:"Ward" ) -> None:
        self.__id=id
        self.__team=team
        self.__ward=Ward
        self.__appointments = ["Appointment"]
        self.__doctors=["Doctor"]
        self.__team.add_patient(self)
        self.__ward.add_patient(self)
from __future__ import annotations
from typing import List, Optional
from Person.Doctor import ConsultantDoctor, Doctor
from Person.Patient import Patient
class Team:
    def __init__(self, id:int) -> None:
        self.__id=id
        self.__team_leader=ConsultantDoctor
        self.__doctors=[]
        self.__patients=[]

    def add_doctor(self, doctor:"Doctor") -> None:
        self.__doctors.append(doctor)
    def add_patient(self, patient:"Patient") -> None:
        self.__patients.append(patient)
@property   
def id(self) -> int:
    return self.__id
@property
def team_leader(self) -> ConsultantDoctor:
    return self.__team_leader
@team_leader.setter
def team_leader(self, leader: "ConsultantDoctor") -> bool:
    self.__team_leader = leader
    return True
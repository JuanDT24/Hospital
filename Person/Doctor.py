from __future__ import annotations
from typing import List, Optional
from abc import ABC, abstractmethod
from System.Team import Team
class Doctor(ABC):
    def __init__(self, id: int, team:"Team") -> None:
        self._id = id
        self._team = team
        self._patients= []
        self._appointments = []
        self.__team.add_doctor(self)
class JuniorDoctor(Doctor):
    def __init__(self, id: int, team:"Team") -> None:
        super().__init__(id, team) 
class ConsultantDoctor(Doctor):
    def __init__(self, id: int, team:"Team") -> None:
        super().__init__(id, team) 
        self.__leader_of = team
        team.team_leader=self  
        self.__leader_of.team_leader=self
class Patient:
    def __init__(self, id: int) -> None:
        self.__id = id
        self.__team: "Team"
        self.__doctor= []
        self.__appointments = []
        self.__ward="Ward"
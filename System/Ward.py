from __future__ import annotations
from typing import List, Optional
from Person.Patient import Patient
class Ward:
    def __init__(self) -> None:
        self.__id=0
        self.__patients=[]
    def add_patient(self, patient: Patient) -> None:
        self.__patients.append(patient)
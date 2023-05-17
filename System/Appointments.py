from __future__ import annotations
from typing import List, Optional
from Person.Doctor import Doctor
from Person.Patient import Patient

class Appointment:
    def __init__(self, Doctor:"Doctor", Patient: "Patient") -> None:
       self.__Doctor=Doctor
       self.__Patient=Patient
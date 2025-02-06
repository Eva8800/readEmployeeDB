from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    name: str
    department: str
    email: str
    phone: str

    def __str__(self):
        return f"{self.id}, {self.name}, {self.department}, {self.email}, {self.phone}"

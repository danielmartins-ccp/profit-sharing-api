from dataclasses import dataclass


@dataclass(frozen=True)
class Weight:
    admission_time: int
    department: int
    salary_range: int

    def total(self):
        return sum([self.admission_time, self.department, self.salary_range])

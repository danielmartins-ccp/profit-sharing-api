from dataclasses import dataclass


@dataclass(frozen=True)
class Weight:
    admission_time: int
    department: int
    salary_range: int

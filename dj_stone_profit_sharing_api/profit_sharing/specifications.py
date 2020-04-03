from profit_calc.bags import Weight
from profit_calc.specifications import (
    AdmissionTimeInYearsBetween,
    AdmissionTimeInYearsGreaterThan,
    AdmissionTimeInYearsLessThan,
    DirectorBoard,
    SalaryBetween,
    SalaryGreaterThan,
    SalaryLessThan,
    Trainee,
)

specifications = {
    DirectorBoard()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 1, 5,),
    DirectorBoard()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 1, 5),
    DirectorBoard()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 1, 5),
    DirectorBoard()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 1, 5),
    DirectorBoard()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 1, 3),
    DirectorBoard()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 1, 3),
    DirectorBoard()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 1, 3),
    DirectorBoard()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 1, 3),
    DirectorBoard()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 1, 2),
    DirectorBoard()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 1, 2),
    DirectorBoard()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(1, 3): Weight(1, 1, 2),
    DirectorBoard()
    & SalaryLessThan(3)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 1, 1),
    DirectorBoard()
    & SalaryLessThan(3)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 1, 1),
    DirectorBoard()
    & SalaryLessThan(3)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 1, 1),
    DirectorBoard()
    & (Trainee() | SalaryLessThan(3))
    & AdmissionTimeInYearsLessThan(1): Weight(1, 1, 1),
}

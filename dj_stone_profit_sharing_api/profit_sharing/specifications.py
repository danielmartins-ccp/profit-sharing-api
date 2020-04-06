from profit_calc.bags import Weight
from profit_calc.specifications import (
    AccountingDepartment,
    AdmissionTimeInYearsBetween,
    AdmissionTimeInYearsGreaterThan,
    AdmissionTimeInYearsLessThan,
    CustomerExperienceDepartment,
    DirectorBoard,
    FacilitiesDepartment,
    FinancialDepartment,
    ITDepartment,
    SalaryBetween,
    SalaryGreaterThan,
    SalaryLessThan,
    Trainee,
)

board_rules = {
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
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 1, 2),
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

accountability_and_financial_and_it_rules = {
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 2, 5),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 2, 5),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 2, 5),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 2, 5),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 2, 3),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 2, 3),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 2, 3),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 2, 3),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 2, 2),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 2, 2),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 2, 2),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 2, 2),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsLessThan(1): Weight(1, 2, 1),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 2, 1),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 2, 1),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 2, 1),
}

facilities_rules = {
    FacilitiesDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 3, 5),
    FacilitiesDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 3, 5),
    FacilitiesDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 3, 5),
    FacilitiesDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 3, 5),
    FacilitiesDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 3, 3),
    FacilitiesDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 3, 3),
    FacilitiesDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 3, 3),
    FacilitiesDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 3, 3),
    FacilitiesDepartment()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 3, 2),
    FacilitiesDepartment()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 3, 2),
    FacilitiesDepartment()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 3, 2),
    FacilitiesDepartment()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 3, 2),
    FacilitiesDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsLessThan(1): Weight(1, 3, 1),
    FacilitiesDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 3, 1),
    FacilitiesDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 3, 1),
    FacilitiesDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 3, 1),
}

customer_xp_rules = {
    CustomerExperienceDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 5, 5),
    CustomerExperienceDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 5, 5),
    CustomerExperienceDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 5, 5),
    CustomerExperienceDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 5, 5),
    CustomerExperienceDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 5, 3),
    CustomerExperienceDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 5, 3),
    CustomerExperienceDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 5, 3),
    CustomerExperienceDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 5, 3),
    CustomerExperienceDepartment()
    & SalaryBetween(3, 8)
    & AdmissionTimeInYearsLessThan(1): Weight(1, 5, 2),
    CustomerExperienceDepartment()
    & SalaryBetween(3, 8)
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 5, 2),
    CustomerExperienceDepartment()
    & SalaryBetween(3, 8)
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 5, 2),
    CustomerExperienceDepartment()
    & SalaryBetween(3, 8)
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 5, 2),
    CustomerExperienceDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsLessThan(1): Weight(1, 5, 1),
    CustomerExperienceDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(1, 3): Weight(2, 5, 1),
    CustomerExperienceDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(3, 8): Weight(3, 5, 1),
    CustomerExperienceDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsGreaterThan(8): Weight(5, 5, 1),
}


specifications = {
    **board_rules,
    **accountability_and_financial_and_it_rules,
    **facilities_rules,
    **customer_xp_rules,
}

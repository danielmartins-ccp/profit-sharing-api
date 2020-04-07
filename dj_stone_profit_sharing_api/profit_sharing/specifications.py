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

depart_spec = {
    DirectorBoard: 1,
    AccountingDepartment: 2,
    FinancialDepartment: 2,
    ITDepartment: 2,
    FacilitiesDepartment: 3,
    CustomerExperienceDepartment: 5,
}

admission_time_spec = {
    "<1": 1,
    "1<>3": 2,
    "3<>8": 3,
    "8+": 5,
}

salary_range_spec = {"8+": 5, "5<>8": 3, "3<>5": 2, "<3": 1}


def weight_factory(department, admission_time, salary_range) -> Weight:
    return Weight(
        admission_time=admission_time_spec.get(admission_time),
        department=depart_spec.get(department),
        salary_range=salary_range_spec.get(salary_range),
    )


board_rules = {
    DirectorBoard()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(DirectorBoard, "8+", "8+"),
    DirectorBoard()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsLessThan(1): weight_factory(DirectorBoard, "<1", "8+"),
    DirectorBoard()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(DirectorBoard, "3<>8", "8+"),
    DirectorBoard()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(DirectorBoard, "1<>3", "8+"),
    DirectorBoard()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(DirectorBoard, "8+", "5<>8"),
    DirectorBoard()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(DirectorBoard, "3<>8", "5<>8"),
    DirectorBoard()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(DirectorBoard, "1<>3", "5<>8"),
    DirectorBoard()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsLessThan(1): weight_factory(DirectorBoard, ">1", "5<>8"),
    DirectorBoard()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(DirectorBoard, "8+", "3<>5"),
    DirectorBoard()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(DirectorBoard, "3<>8", "3<>5"),
    DirectorBoard()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(DirectorBoard, "1<>3", "3<>5"),
    DirectorBoard()
    & (Trainee() | SalaryLessThan(3))
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(DirectorBoard, "8+", "<3"),
    DirectorBoard()
    & (Trainee() | SalaryLessThan(3))
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(DirectorBoard, "3<>8", "<3"),
    DirectorBoard()
    & (Trainee() | SalaryLessThan(3))
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(DirectorBoard, "1<>3", "<3"),
    DirectorBoard()
    & (Trainee() | SalaryLessThan(3))
    & AdmissionTimeInYearsLessThan(1): weight_factory(DirectorBoard, "<1", "<3"),
}

accountability_and_financial_and_it_rules = {
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsLessThan(1): weight_factory(AccountingDepartment, ">1", "8+"),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        AccountingDepartment, "1<>3", "8+"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        AccountingDepartment, "3<>8", "8+"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        AccountingDepartment, "8+", "8+"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsLessThan(1): weight_factory(
        AccountingDepartment, ">1", "5<>8"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        AccountingDepartment, "1<>3", "5<>8"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        AccountingDepartment, "3<>8", "5<>8"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        AccountingDepartment, "8+", "5<>8"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsLessThan(1): weight_factory(
        AccountingDepartment, ">1", "3<>5"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        AccountingDepartment, "1<>3", "3<>5"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        AccountingDepartment, "3<>8", "3<>5"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        AccountingDepartment, "8+", "3<>5"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsLessThan(1): weight_factory(AccountingDepartment, ">1", ">3"),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        AccountingDepartment, "1<>3", ">3"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        AccountingDepartment, "3<>8", ">3"
    ),
    (AccountingDepartment() | FinancialDepartment() | ITDepartment())
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        AccountingDepartment, "8+", ">3"
    ),
}

facilities_rules = {
    FacilitiesDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsLessThan(1): weight_factory(FacilitiesDepartment, ">1", "8+"),
    FacilitiesDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        FacilitiesDepartment, "1<>3", "8+"
    ),
    FacilitiesDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        FacilitiesDepartment, "3<>8", "8+"
    ),
    FacilitiesDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        FacilitiesDepartment, "8+", "8+"
    ),
    FacilitiesDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsLessThan(1): weight_factory(
        FacilitiesDepartment, ">1", "5<>8"
    ),
    FacilitiesDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        FacilitiesDepartment, "1<>3", "5<>8"
    ),
    FacilitiesDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        FacilitiesDepartment, "3<>8", "5<>8"
    ),
    FacilitiesDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        FacilitiesDepartment, "8+", "5<>8"
    ),
    FacilitiesDepartment()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsLessThan(1): weight_factory(
        FacilitiesDepartment, ">1", "3<>5"
    ),
    FacilitiesDepartment()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        FacilitiesDepartment, "1<>3", "3<>5"
    ),
    FacilitiesDepartment()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        FacilitiesDepartment, "3<>8", "3<>5"
    ),
    FacilitiesDepartment()
    & SalaryBetween(3, 5)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        FacilitiesDepartment, "8+", "3<>5"
    ),
    FacilitiesDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsLessThan(1): weight_factory(FacilitiesDepartment, ">1", ">3"),
    FacilitiesDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        FacilitiesDepartment, "1<>3", ">3"
    ),
    FacilitiesDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        FacilitiesDepartment, "3<>8", ">3"
    ),
    FacilitiesDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        FacilitiesDepartment, "8+", ">3"
    ),
}

customer_xp_rules = {
    CustomerExperienceDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsLessThan(1): weight_factory(
        CustomerExperienceDepartment, ">1", "8+"
    ),
    CustomerExperienceDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        CustomerExperienceDepartment, "1<>3", "8+"
    ),
    CustomerExperienceDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        CustomerExperienceDepartment, "3<>8", "8+"
    ),
    CustomerExperienceDepartment()
    & SalaryGreaterThan(8)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        CustomerExperienceDepartment, "8+", "8+"
    ),
    CustomerExperienceDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsLessThan(1): weight_factory(
        CustomerExperienceDepartment, ">1", "5<>8"
    ),
    CustomerExperienceDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        CustomerExperienceDepartment, "1<>3", "5<>8"
    ),
    CustomerExperienceDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        CustomerExperienceDepartment, "3<>8", "5<>8"
    ),
    CustomerExperienceDepartment()
    & SalaryBetween(5, 8)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        CustomerExperienceDepartment, "8+", "5<>8"
    ),
    CustomerExperienceDepartment()
    & SalaryBetween(3, 8)
    & AdmissionTimeInYearsLessThan(1): weight_factory(
        CustomerExperienceDepartment, ">1", "3<>8"
    ),
    CustomerExperienceDepartment()
    & SalaryBetween(3, 8)
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        CustomerExperienceDepartment, "1<>3", "3<>8"
    ),
    CustomerExperienceDepartment()
    & SalaryBetween(3, 8)
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        CustomerExperienceDepartment, "3<>8", "3<>8"
    ),
    CustomerExperienceDepartment()
    & SalaryBetween(3, 8)
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        CustomerExperienceDepartment, "8+", "3<>8"
    ),
    CustomerExperienceDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsLessThan(1): weight_factory(
        CustomerExperienceDepartment, ">1", ">3"
    ),
    CustomerExperienceDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(1, 3): weight_factory(
        CustomerExperienceDepartment, "1<>3", ">3"
    ),
    CustomerExperienceDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsBetween(3, 8): weight_factory(
        CustomerExperienceDepartment, "3<>8", ">3"
    ),
    CustomerExperienceDepartment()
    & (SalaryLessThan(3) | Trainee())
    & AdmissionTimeInYearsGreaterThan(8): weight_factory(
        CustomerExperienceDepartment, "8+", ">3"
    ),
}


specifications = {
    **board_rules,
    **accountability_and_financial_and_it_rules,
    **facilities_rules,
    **customer_xp_rules,
}

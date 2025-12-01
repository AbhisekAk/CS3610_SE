# CompanyComposite/clientCompany.py

from CompanyComposite.OrgComposite import Department, Employee


def build_sample_company() -> Department:
    """
    Build a richer organization tree:

    Head Office
    ├── Engineering Department
    │   ├── Backend Team
    │   │   ├── Alice  (Backend Developer)
    │   │   └── Bob    (Backend Developer)
    │   ├── Frontend Team
    │   │   └── Carol  (Frontend Developer)
    │   └── Data Science Team
    │       ├── Frank  (Data Scientist)
    │       └── Grace  (ML Engineer)
    ├── HR Department
    │   ├── Recruitment Team
    │   │   ├── Hannah (Recruiter)
    │   │   └── Ian    (Recruiter)
    │   └── Payroll Team
    │       └── Julia  (Payroll Specialist)
    ├── Sales Department
    │   ├── Domestic Sales Team
    │   │   └── Kevin  (Sales Rep)
    │   └── International Sales Team
    │       └── Laura  (Sales Rep)
    └── IT Support Department
        ├── Helpdesk Team
        │   └── Mike   (Support Engineer)
        └── Infrastructure Team
            └── Nina   (SysAdmin)
    """

    # Root of the composite tree
    company = Department("Head Office")

    # Top-level departments
    eng_dept = Department("Engineering Department")
    hr_dept = Department("HR Department")
    sales_dept = Department("Sales Department")
    it_dept = Department("IT Support Department")

    # ----- Engineering sub-departments -----
    backend_team = Department("Backend Team")
    frontend_team = Department("Frontend Team")
    data_team = Department("Data Science Team")

    # Engineering employees
    alice = Employee("Alice", "Backend Developer", 7000.0)
    bob = Employee("Bob", "Backend Developer", 6500.0)
    carol = Employee("Carol", "Frontend Developer", 6800.0)
    frank = Employee("Frank", "Data Scientist", 7500.0)
    grace = Employee("Grace", "ML Engineer", 7600.0)

    backend_team.add(alice)
    backend_team.add(bob)

    frontend_team.add(carol)

    data_team.add(frank)
    data_team.add(grace)

    eng_dept.add(backend_team)
    eng_dept.add(frontend_team)
    eng_dept.add(data_team)

    # ----- HR sub-departments -----
    recruitment_team = Department("Recruitment Team")
    payroll_team = Department("Payroll Team")

    hannah = Employee("Hannah", "Recruiter", 5200.0)
    ian = Employee("Ian", "Recruiter", 5100.0)
    julia = Employee("Julia", "Payroll Specialist", 5400.0)

    recruitment_team.add(hannah)
    recruitment_team.add(ian)
    payroll_team.add(julia)

    hr_dept.add(recruitment_team)
    hr_dept.add(payroll_team)

    # ----- Sales sub-departments -----
    domestic_sales = Department("Domestic Sales Team")
    international_sales = Department("International Sales Team")

    kevin = Employee("Kevin", "Sales Representative", 6000.0)
    laura = Employee("Laura", "Sales Representative", 6300.0)

    domestic_sales.add(kevin)
    international_sales.add(laura)

    sales_dept.add(domestic_sales)
    sales_dept.add(international_sales)

    # ----- IT Support sub-departments -----
    helpdesk_team = Department("Helpdesk Team")
    infra_team = Department("Infrastructure Team")

    mike = Employee("Mike", "Support Engineer", 5800.0)
    nina = Employee("Nina", "System Administrator", 7000.0)

    helpdesk_team.add(mike)
    infra_team.add(nina)

    it_dept.add(helpdesk_team)
    it_dept.add(infra_team)

    # Attach all top-level departments to the root company
    company.add(eng_dept)
    company.add(hr_dept)
    company.add(sales_dept)
    company.add(it_dept)

    return company


def runCompositeDemo() -> None:
    """
    Demonstration of the Composite pattern with a richer hierarchy:
    - Show the company structure
    - Compute total salary
    - Assign a task to the entire company
    """
    company = build_sample_company()

    print("=== Company Organizational Structure ===")
    company.show()

    total_salary = company.getTotalSalary()
    print(f"\nTotal salary for entire company: {total_salary:.2f}\n")

    print("=== Assigning task: 'Prepare quarterly report' ===")
    company.doOperation("Prepare quarterly report")

# CompanyComposite/OrgComposite.py

from abc import ABC, abstractmethod
from typing import List


class IOrgComponent(ABC):
    """
    Component interface in the Composite pattern.

    Both Employee (Leaf) and Department (Composite) implement this so
    the client can treat them uniformly.
    """

    @abstractmethod
    def getTotalSalary(self) -> float:
        """Return the total salary cost under this node."""
        pass

    @abstractmethod
    def doOperation(self, task: str) -> None:
        """
        Perform some operation (e.g., assign a task).
        For a Department, this is delegated to children.
        For an Employee, this is executed directly.
        """
        pass

    @abstractmethod
    def show(self, indent: int = 0) -> None:
        """
        Print the organization tree starting at this component.
        `indent` is used for pretty printing (like dir(indent) in the notebook).
        """
        pass


# ===== Leaf: Employee =====

class Employee(IOrgComponent):
    """
    Leaf in the Composite tree.
    Represents an individual employee.
    """

    def __init__(self, name: str, role: str, salary: float) -> None:
        self._name = name
        self._role = role
        self._salary = salary

    @property
    def name(self) -> str:
        return self._name

    @property
    def role(self) -> str:
        return self._role

    @property
    def salary(self) -> float:
        return self._salary

    def getTotalSalary(self) -> float:
        # Leaf: just its own salary
        return self._salary

    def doOperation(self, task: str) -> None:
        # Leaf: directly performs the task
        print(f"[Employee] {self._name} ({self._role}) is assigned: {task}")

    def show(self, indent: int = 0) -> None:
        prefix = " " * indent
        print(f"{prefix}- Employee: {self._name} ({self._role}), Salary: {self._salary:.2f}")


# ===== Composite: Department =====

class Department(IOrgComponent):
    """
    Composite in the Composite tree.
    Represents a department or team which can contain Employees and/or sub-Departments.
    """

    def __init__(self, name: str) -> None:
        self._name = name
        self._children: List[IOrgComponent] = []

    @property
    def name(self) -> str:
        return self._name

    def add(self, component: IOrgComponent) -> None:
        """Add a child (Employee or Department)."""
        self._children.append(component)

    def remove(self, component: IOrgComponent) -> None:
        """Remove a child (Employee or Department) if present."""
        if component in self._children:
            self._children.remove(component)

    def getTotalSalary(self) -> float:
        """
        Total salary is the sum of all children's total salaries.
        This automatically includes nested sub-departments.
        """
        return sum(child.getTotalSalary() for child in self._children)

    def doOperation(self, task: str) -> None:
        """
        Assign a task to the entire department.
        Delegates to all children (like Folder.dir calls child.dir in the notebook).
        """
        print(f"[Department] '{self._name}' received task: {task}")
        for child in self._children:
            child.doOperation(task)

    def show(self, indent: int = 0) -> None:
        """Print the subtree starting from this department."""
        prefix = " " * indent
        print(f"{prefix}+ Department: {self._name}")
        for child in self._children:
            child.show(indent + 2)

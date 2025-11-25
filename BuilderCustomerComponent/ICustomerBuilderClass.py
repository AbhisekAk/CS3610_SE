from abc import ABC, abstractmethod

class ICustomerBuilder(ABC):

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def firstName(self, value: str):
        pass

    @abstractmethod
    def middleName(self, value: str | None):
        pass

    @abstractmethod
    def lastName(self, value: str):
        pass

    @abstractmethod
    def primaryEmail(self, value: str):
        pass

    @abstractmethod
    def secondaryEmail(self, value: str | None):
        pass

    @abstractmethod
    def primaryMobileNumber(self, value: str):
        pass

    @abstractmethod
    def secondaryMobileNumber(self, value: str | None):
        pass

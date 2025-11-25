from BuilderCustomerComponent.CustomerDirectorClass import CustomerDirector
from BuilderCustomerComponent.WebAppCustomerBuilderClass import WebAppCustomerBuilder
from BuilderCustomerComponent.MobileAppCustomerBuilderClass import MobileAppCustomerBuilder

def run_demo():
    director = CustomerDirector()

    print("From Web Application (all fields):")
    web_builder = WebAppCustomerBuilder()
    director.builder = web_builder

    c1 = director.constructCustomer(
        firstName="Macey",
        middleName="Melanie",
        lastName="Peterson",
        primaryEmail="pmacey@gmail.com",
        secondaryEmail="mmm12.e@gmail.com",
        primaryMobileNumber="123-456-8934",
        secondaryMobileNumber="780-765-4321",
    )
    c1.showComponents()

    print("From Mobile Application (mandatory fields only):")
    mobile_builder = MobileAppCustomerBuilder()
    director.builder = mobile_builder

    c2 = director.constructCustomer(
        firstName="Avi",
        middleName=None,
        lastName="Akauliya",
        primaryEmail="Avi@gmails.com",
        secondaryEmail=None,
        primaryMobileNumber="780-456-8934",
        secondaryMobileNumber=None,
    )
    c2.showComponents()

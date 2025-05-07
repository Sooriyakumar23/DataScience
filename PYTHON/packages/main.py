# Package is a Collection of Modules/Python files
# Package is used to breakdown the 1000 lines of code into different different python files so that it will be readable

from calculator import add # calculator -> module
from company.employee import first_name # company -> package, employee -> module
from company.labour.salary import give_my_salary # comapny, labour -> package, salary -> module

add(1,2)
first_name("Alice")
give_my_salary(15)
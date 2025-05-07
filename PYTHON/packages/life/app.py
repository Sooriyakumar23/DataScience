import sys
import os

sys.path.append(os.path.abspath("..")) # os.path.abspath("..")

from company.labour.salary import give_my_salary

give_my_salary(20)
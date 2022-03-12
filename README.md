# Payroll-Strategy

This repository contains all the scripts to solve a Payroll task considering different scenarios using unstructured data from a Text file. Strategy was the applied design pattern for this task due to none of the employees had any hierarchical relation. Classes and methods are well commented, nevertheless, these are some considerations used to develop this solution.

Assumptions - Payment may be monthly; therefore, days can be repeated for any given employee. - Maximum number of employees is None - Minimum number of employees is 5. - Payment does not include any particular discounts or increases due to insurance or bonuses. - Input data must be a .txt file - Time intervals must be of exact hours as usual.

**Data format for every employee must be:**

  1 Record: DAY&WorkingHoursInterval x N, N <= 4, & ∄
  Format → EmployeName = 1Record x M, M <= 30

**Possible scenarios**
  - Duplicated names of employees - Duplicated rows
  - Blank spaces
  - Repeated days (No more than 5 repetitions)
  - Different job intervals during the same day
  - Different salary ranges during the same job interval in the same day
  - Transition intervals between different salary ranges (Friday-Saturday, Sunday-Monday)

**Requirements:**

   - This solution does not require any external library or dependency.
   - All the job is built based on Python standard libraries

**Considerations:**

   Python version == 3.9.6
   To run the solution just follow the next steps: 
   
   1.- Clone this repository or
   2.- Download PayrollExcercise folder and payroll.txt file
   3.- - Note - [dataExtraction.py, dataStructurer.py, moneyMaker.py, Payroll] files must be included in the same folder 
   4.- Use the above criteria for UnitTest folder and scripts
   5.- Run Payroll.py file on your terminal/CMD: python Payroll.py
   6.- Input the text file address on your system, like: C:/Users/Felix/Desktop/Ioet/payroll.txt ,as example.
   7.- Have fun

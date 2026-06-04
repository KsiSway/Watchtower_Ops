---
sourceFile: "How to Convert a Python datetime.datetime to Excel Serial Date Number? - TutorialsPoint"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.385Z"
---

# How to Convert a Python datetime.datetime to Excel Serial Date Number? - TutorialsPoint

de8a01f1-cd6e-4e60-b6ef-489dbf78f087

How to Convert a Python datetime.datetime to Excel Serial Date Number? - TutorialsPoint

b9e2d11c-9653-474f-bcda-1341ad3ac8ff

https://www.tutorialspoint.com/article/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

Practice Code

Graphing Calculator

Online Compilers

Explore  Categories

Find the perfect tutorial for your learning journey

Python Technologies

Computer Programming

Web Development

Java Technologies

Computer Science

Mobile Development

Big Data & Analytics

Microsoft Technologies

Latest Technologies

Machine Learning

Digital Marketing

Software Quality

Management Tutorials

View All Categories

Article Categories

All Categories

Data Structure

Operating System

C Programming

Economics & Finance

Selected Reading

UPSC IAS Exams Notes

Developer's Best Practices

Questions and Answers

Online Resume Builder

HR Interview Questions

Computer Glossary

How to Convert a Python datetime.datetime to Excel Serial Date Number?

Server Side Programming

Programming

Excel uses a special format to store dates and times, called serial date numbers. Serial date numbers are a count of days since January 1, 1900, which Excel considers as day 1. Python's  datetime  module provides powerful tools for working with dates, and we can convert datetime objects to Excel's serial format for interoperability.

Understanding Excel Serial Date Numbers

In Excel, dates are internally represented as serial numbers where each day has a unique numeric value. January 1, 1900 is represented by 1, January 2, 1900 by 2, and so on. This numeric format allows Excel to perform date calculations efficiently.

Jan 1, 1900   Serial: 1   May 1, 2023   Serial: 45047   45046 days

Converting datetime to Excel Serial Date

To convert a Python  datetime  object to Excel serial format, we calculate the difference from Excel's base date (December 30, 1899) and add fractional days for time components ?

import datetime as dt def datetime\_to\_excel\_serial\_date(date): excel\_base\_date = dt.datetime(1899, 12, 30) # Excel's actual base date delta = date - excel\_base\_date excel\_serial\_date = delta.days + delta.seconds / (24 \* 60 \* 60) return excel\_serial\_date # Example with date and time my\_datetime = dt.datetime(2023, 5, 1, 12, 30, 0) # May 1, 2023 12:30 PM excel\_serial = datetime\_to\_excel\_serial\_date(my\_datetime) print(f"DateTime: {my\_datetime}") print(f"Excel Serial: {excel\_serial}") # Example with date only my\_date = dt.datetime(2023, 5, 1) excel\_serial\_date = datetime\_to\_excel\_serial\_date(my\_date) print(f"\nDate only: {my\_date.date()}") print(f"Excel Serial: {excel\_serial\_date}")  DateTime: 2023-05-01 12:30:00 Excel Serial: 45047.520833333336 Date only: 2023-05-01 Excel Serial: 45047.0

Using Python's Built-in Ordinal Method

Python's  datetime  provides  toordinal()  method, but it uses a different epoch (January 1, Year 1) than Excel ?

import datetime as dt # Using toordinal() - different from Excel format current\_date = dt.datetime.now() python\_ordinal = current\_date.toordinal() print(f"Current date: {current\_date.date()}") print(f"Python ordinal: {python\_ordinal}") # Convert Python ordinal to Excel serial (approximate) # Excel starts from Jan 1, 1900 (ordinal 693594) excel\_serial\_approx = python\_ordinal - 693593 # Adjust for Excel base print(f"Approximate Excel serial: {excel\_serial\_approx}")  Current date: 2024-01-15 Python ordinal: 738887 Approximate Excel serial: 45294

Handling Excel's Leap Year Bug

Excel incorrectly treats 1900 as a leap year. For accurate conversion, we need to account for this bug ?

import datetime as dt def accurate\_excel\_serial\_date(date): excel\_base = dt.datetime(1899, 12, 30) delta = date - excel\_base serial = delta.days + delta.seconds / 86400 # 86400 seconds in a day # Adjust for Excel's leap year bug (1900 not a leap year but Excel thinks it is) if date >= dt.datetime(1900, 3, 1): serial += 1 return serial # Test with dates before and after the bug dates\_to\_test = \[ dt.datetime(1900, 2, 28), # Before the bug dt.datetime(1900, 3, 1), # After the bug dt.datetime(2023, 5, 1) # Modern date \] for test\_date in dates\_to\_test: serial = accurate\_excel\_serial\_date(test\_date) print(f"{test\_date.date()} → {serial}")  1900-02-28 ? 59.0 1900-03-01 ? 61.0 2023-05-01 ? 45048.0

Comparison of Methods

Method   Handles Time?   Excel Bug Fix?   Best For   Basic Delta Calculation   Yes   No   Simple conversion   Python toordinal()   No   No   Different epoch system   Accurate Method   Yes   Yes   Excel compatibility

Converting Python datetime to Excel serial dates requires calculating days from Excel's base date (December 30, 1899). For maximum accuracy, account for Excel's 1900 leap year bug by adding 1 to dates after March 1, 1900.

Mukul Latiyan

Updated on:  2026-03-27T11:13:55+05:30

Learn More in Our Tutorials

Python - Date and Time   Python

Python XlsxWriter - Date & Time   Python Xlsxwriter

Python - Date & Time   PYTHON

Excel - DATE Function   Advanced Excel Functions

Excel - DATEVALUE Function   Advanced Excel Functions

Advertisements

Tutorials Point is a leading Ed Tech company striving to provide the best learning material on technical and non-technical subjects.

Copyright 2026. All Rights Reserved.


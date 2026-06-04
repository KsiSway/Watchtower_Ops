---
sourceFile: "How Do I Convert Excel Dates And Numbers Into Usable Python Types? - Python Code School"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.383Z"
---

# How Do I Convert Excel Dates And Numbers Into Usable Python Types? - Python Code School

52fb4778-32fe-4a61-a992-d54dacf633d5

How Do I Convert Excel Dates And Numbers Into Usable Python Types? - Python Code School

a98cda5d-22f6-4f0f-85b0-9a42f1790174

https://www.youtube.com/watch?v=BZkwROtpFQU

BZkwROtpFQU

Python Code School

how do I convert Excel dates and numbers into usable Python types imagine working with a spreadsheet full of dates and numbers but they are not in a format Python can understand it can be frustrating trying to analyze data when dates are just numbers today I will show you how to turn those Excel serial numbers and general numbers into Python types that you can work with easily excel stores dates as serial numbers counting days from December 30 1899 for example the number 150 corresponds to a specific date to make this usable in Python you need to add that number of days to the base date you can do this with the datetime module first set the base date as December 30 1899 then add the serial number as a time delta which is a duration of days this gives you a Python datetime object representing the date here's a simple function to do that it takes the serial number as input adds it to the base date and returns the date as a datetime object if your Excel file has times or datetime values with fractional days like 0.54 noon this method still works the fractional part is converted into hours minutes and seconds when you add the time delta if you're using pandas which is great for data analysis you can convert Excel date serial numbers into pandas datetime objects easily just add the serial number as a time delta to the date 1899 1230 using pandas this makes it simple to convert entire columns of dates when you read your Excel files into pandas dataf frames when you load an Excel file with libraries like open pixel or xlrard date cells might already come as serial numbers or strings you can apply the conversion functions to turn those into Python datetime objects for general numbers that are not dates python's built-in int or float types work perfectly after reading the data pandas also automatically detects numeric columns so you don't have to worry about converting them manually to sum it up first identify the serial numbers that representing dates in Excel then convert those serial numbers into Python datetime objects by adding the number of days to December 30 1899 use pandas or the datetime module for easy conversion and manipulation for other numbers just read them as Python numeric types for calculations these steps are essential when automating tasks with Excel files in Python making your data ready for analysis or reporting


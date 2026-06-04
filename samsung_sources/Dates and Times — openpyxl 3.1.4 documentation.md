---
sourceFile: "Dates and Times — openpyxl 3.1.4 documentation"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.311Z"
---

# Dates and Times — openpyxl 3.1.4 documentation

c0023b6c-e12c-4689-9b98-cf7d37cbd25e

Dates and Times — openpyxl 3.1.4 documentation

75144827-56ca-45aa-aafb-308e464db143

https://openpyxl.readthedocs.io/en/3.1/datetime.html

Dates and Times — openpyxl 3.1.4 documentation

https://openpyxl.readthedocs.io/en/3.1/genindex.html

https://openpyxl.readthedocs.io/en/3.1/py-modindex.html

https://openpyxl.readthedocs.io/en/3.1/simple\_formulae.html

https://openpyxl.readthedocs.io/en/3.1/comments.html

openpyxl 3.1.4 documentation

https://openpyxl.readthedocs.io/en/3.1/index.html

Dates and Times

https://openpyxl.readthedocs.io/en/3.1/datetime.html

Dates and Times

https://openpyxl.readthedocs.io/en/3.1/datetime.html#dates-and-times

Dates and times can be stored in two distinct ways in XLSX files: as an ISO 8601 formatted string or as a single number. openpyxl supports both representations and translates between them and Python's datetime module representations when reading from and writing to files. In either representation, the maximum date and time precision in XLSX files is millisecond precision.

XLSX files are not suitable for storing historic dates (before 1900), due to bugs in Excel that cannot be fixed without causing backward compatibility problems. To discourage users from trying anyway, Excel deliberately refuses to recognize and display such dates. Consequently, it is not advised to use openpyxl for such purposes either, especially when exchanging files with others.

https://openpyxl.readthedocs.io/en/3.1/datetime.html#timezones

The date and time representations in Excel do not support timezones, therefore openpyxl can only deal with naive datetime/time objects. Any timezone information attached to Python datetimes must be stripped off by the user before datetimes can be stored in XLSX files.

Using the ISO 8601 format

https://openpyxl.readthedocs.io/en/3.1/datetime.html#using-the-iso-8601-format

To make openpyxl store dates and times in the ISO 8601 format on writing your file, set the workbook's

>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> wb.iso\_dates = True

The benefit of using this format is that the meaning of the stored information is not subject to interpretation, as it is with the single number format

https://openpyxl.readthedocs.io/en/3.1/datetime.html#f1

The Office Open XML standard does not specify a supported subset of the ISO 8601 duration format for representing time interval durations. openpyxl therefore always uses the single number format for timedelta values when writing them to file.

The 1900 and 1904 date systems

https://openpyxl.readthedocs.io/en/3.1/datetime.html#the-1900-and-1904-date-systems

The 'date system' of an XLSX file determines how dates and times in the single number representation are interpreted. XLSX files always use one of two possible date systems:

In the 1900 date system (the default), the reference date (with number 1) is 1900-01-01.

In the 1904 date system, the reference date (with number 0) is 1904-01-01.

Complications arise not only from the different start numbers of the reference dates, but also from the fact that the 1900 date system has a built-in (but wrong) assumption that the year 1900 had been a leap year. Excel deliberately refuses to recognize and display dates before the reference date correctly, in order to discourage people from storing historical data.

#### More information on this issue is available from Microsoft:

https://docs.microsoft.com/en-us/office/troubleshoot/excel/1900-and-1904-date-system

https://docs.microsoft.com/en-us/office/troubleshoot/excel/1900-and-1904-date-system

https://docs.microsoft.com/en-us/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year

https://docs.microsoft.com/en-us/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year

In workbooks using the 1900 date system, openpyxl behaves the same as Excel when translating between the worksheets' date/time numbers and Python datetimes in January and February 1900. The only exception is 29 February 1900, which cannot be represented as a Python datetime object since it is not a valid date.

#### You can get the date system of a workbook like this:

>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> if wb.epoch == openpyxl.utils.datetime.CALENDAR\_WINDOWS\_1900:
...     print("This workbook is using the 1900 date system.")
...
This workbook is using the 1900 date system.

and set it like this:

>>> wb.epoch = openpyxl.utils.datetime.CALENDAR\_MAC\_1904

Handling timedelta values

https://openpyxl.readthedocs.io/en/3.1/datetime.html#handling-timedelta-values

Excel users can use number formats resembling

to display time interval durations, which openpyxl considers to be equivalent to timedeltas in Python. openpyxl recognizes these number formats when reading XLSX files and returns datetime.timedelta values for the corresponding cells.

When writing timedelta values from worksheet cells to file, openpyxl uses the

number format for these cells.

https://openpyxl.readthedocs.io/en/3.1/datetime.html#id1

For example, the serial 1 in an Excel worksheet can be interpreted as 00:00, as 24:00, as 1900-01-01, as 1440 (minutes), etc., depending solely on the formatting applied.

Simplify infrastructure with MongoDB Atlas, the leading modern database

https://server.ethicalads.io/proxy/click/10498/019e440e-9c28-7620-bb1b-14c70463ec3e/

Ads by EthicalAds

https://www.ethicalads.io/advertisers/?ref=ea-text

Table of Contents

https://openpyxl.readthedocs.io/en/3.1/index.html

Dates and Times

https://openpyxl.readthedocs.io/en/3.1/datetime.html

https://openpyxl.readthedocs.io/en/3.1/datetime.html#timezones

Using the ISO 8601 format

https://openpyxl.readthedocs.io/en/3.1/datetime.html#using-the-iso-8601-format

The 1900 and 1904 date systems

https://openpyxl.readthedocs.io/en/3.1/datetime.html#the-1900-and-1904-date-systems

Handling timedelta values

https://openpyxl.readthedocs.io/en/3.1/datetime.html#handling-timedelta-values

Previous topic

https://openpyxl.readthedocs.io/en/3.1/comments.html

Simple Formualae

https://openpyxl.readthedocs.io/en/3.1/simple\_formulae.html

Show Source

https://openpyxl.readthedocs.io/en/3.1/\_sources/datetime.rst.txt

Quick search

https://openpyxl.readthedocs.io/en/3.1/genindex.html

https://openpyxl.readthedocs.io/en/3.1/py-modindex.html

https://openpyxl.readthedocs.io/en/3.1/simple\_formulae.html

https://openpyxl.readthedocs.io/en/3.1/comments.html

openpyxl 3.1.4 documentation

https://openpyxl.readthedocs.io/en/3.1/index.html

Dates and Times

https://openpyxl.readthedocs.io/en/3.1/datetime.html

© Copyright 2010 - 2024, See AUTHORS. Created using

https://www.sphinx-doc.org/

https://openpyxl.readthedocs.io/en/latest/datetime.html

https://openpyxl.readthedocs.io/en/stable/datetime.html

https://openpyxl.readthedocs.io/en/3.1.3/datetime.html

https://openpyxl.readthedocs.io/en/3.1.2/datetime.html

https://openpyxl.readthedocs.io/en/3.1.1/datetime.html

https://openpyxl.readthedocs.io/en/3.1.0/datetime.html

https://openpyxl.readthedocs.io/en/3.0/datetime.html

https://openpyxl.readthedocs.io/en/2.6/datetime.html

https://openpyxl.readthedocs.io/en/2.5.14/datetime.html

https://openpyxl.readthedocs.io/en/2.5/datetime.html

https://openpyxl.readthedocs.io/en/2.4/datetime.html

On Read the Docs

Project Home

https://app.readthedocs.org/projects/openpyxl/?utm\_source=openpyxl&utm\_content=flyout

https://app.readthedocs.org/projects/openpyxl/builds/?utm\_source=openpyxl&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=openpyxl&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=openpyxl&utm\_content=flyout

No recent searches

to navigate

Search powered by


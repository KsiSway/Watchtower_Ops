---
sourceFile: "Technical Analysis of Temporal Data Interoperability: Converting Excel Date Serial Numbers in Python"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.521Z"
---

# Technical Analysis of Temporal Data Interoperability: Converting Excel Date Serial Numbers in Python

2f0dc516-31a1-405d-aaf0-f8c7ca75d377

Technical Analysis of Temporal Data Interoperability: Converting Excel Date Serial Numbers in Python

b1fc7f7c-8f9b-4347-82c3-d66fa02aa6a7

Technical Analysis of Temporal Data Interoperability: Converting Excel Date Serial Numbers in Python

The representation of chronological data within computational environments has historically been a source of significant friction, particularly when interfacing between high-level programming languages like Python and ubiquitous spreadsheet applications such as Microsoft Excel. At the heart of this friction is the "date serial number," a system that simplifies date-time calculations for spreadsheet users but introduces a layer of complexity for data engineers and analysts. Understanding the conversion of these serial numbers requires an exhaustive examination of historical software bugs, architectural differences between operating systems, and the numerical limitations of floating-point arithmetic.

The Historical Genesis of Spreadsheet Chronology

To comprehend why modern Python libraries must account for seemingly arbitrary offsets when converting Excel dates, one must look back to the early 1980s. The architectural decisions made during the development of Lotus 1-2-3, the second major spreadsheet program after VisiCalc, continue to dictate the behavior of modern data pipelines.\[1, 2\] The most pervasive anomaly is the "1900 Leap Year Bug." Under the rules of the Gregorian calendar, a year is a leap year if it is divisible by 4, except for years divisible by 100, which are only leap years if they are also divisible by 400. Consequently, the year 1900 was not a leap year.\[2, 3, 4\]

However, the developers of Lotus 1-2-3 intentionally—or perhaps through oversight in a resource-constrained environment—treated 1900 as a leap year.\[1, 4\] Contemporary accounts suggest this was likely an optimization to save memory and compute cycles.\[1, 2\] On the hardware of the era, where memory was limited to 640K, calculating the leap year condition could be simplified to checking if the last two bits of the year were zero, effectively ignoring the century exception.\[2\] When Microsoft developed Multiplan and later Excel, they faced a critical decision: correct the leap year error or maintain compatibility with Lotus 1-2-3.\[2, 4\] Microsoft chose the latter, reproducing the bug to ensure that worksheets migrated from Lotus would maintain consistent date calculations.\[1, 4, 5\]

This decision created a permanent rift in temporal data logic. Because Excel assumes February 29, 1900, exists, every serial date after February 28, 1900, is incremented by one.\[5, 6, 7\] If this behavior were corrected today, it would cause a cascading failure across millions of legacy workbooks, decreasing almost every date by one day and breaking functions such as

.\[1, 4\] For Python developers, this means that the "true" epoch for Excel's 1900 system is effectively December 30, 1899, rather than the documented January 1, 1900.\[2, 6, 8, 9\]

Computational Mechanics of Serial Date Structures

Excel stores dates and times as floating-point numbers, referred to as serial numbers.\[3, 10, 11\] The integer portion of the serial number represents the number of days elapsed since the epoch, while the fractional portion represents the time as a fraction of a 24-hour day.\[3, 6, 12\] This dual-nature representation allows for efficient sorting and mathematical operations, such as calculating the number of days between two dates through simple subtraction.\[12, 13\]

The mathematical representation of a timestamp in Excel can be articulated through the following relationship:

SerialValue = Days + \frac{Hours}{24} + \frac{Minutes}{1440} + \frac{Seconds}{86400} + \frac{Milliseconds}{86400000}

In this system, a value of 1.0 corresponds to January 1, 1900, at midnight.\[3, 10\] A value of 0.5 would represent 12:00 PM on the day before the epoch, which Excel's display engine often renders as the non-existent "January 0, 1900".\[6, 7, 14\] Python’s

module, however, adheres to the proleptic Gregorian calendar, which correctly identifies 1900 as a common year. This discrepancy is the primary driver behind the need for specialized conversion logic when reading data from Excel files.\[12, 15\]

Serial Number

Excel Display (1900 System)

(Gregorian)

Significance

1/0/1900 \[6, 7\]

1899-12-30 \[2, 8\]

The effective base for calculations.

1/1/1900 \[6, 10\]

1899-12-31 \[7, 16\]

Excel's "Day 1."

2/28/1900 \[14, 17\]

1900-02-27 \[17\]

Last day before divergence.

2/29/1900 \[1, 5, 15\]

N/A (Error) \[15\]

The non-existent leap day.

3/1/1900 \[7, 14\]

1900-03-01 \[7, 14\]

Point of synchronization.

5/1/2023 12:30 PM \[12\]

2023-05-01 12:30 PM \[12\]

Modern date-time example.

Architectural Divergence: The 1900 vs. 1904 Date Systems

A significant complication in temporal interoperability is the existence of two distinct date systems within Excel: the 1900 system and the 1904 system.\[3, 10\] The 1900 system is the default for Windows and modern versions of Excel for Mac (Excel 2011 and later).\[10\] The 1904 system was originally the default for Macintosh versions of Excel.\[3, 10, 18\]

The 1904 system was developed to resolve the 1900 leap year bug and to simplify calculations for early Mac developers by starting the epoch after the problematic year 1900.\[10, 15, 19\] In the 1904 system, January 1, 1904, is serial number 0.\[10, 15, 17\] This results in a persistent 1,462-day difference between the two systems.\[10\] This value corresponds to four years and one day, which includes the extra day from the 1904 leap year.\[10\]

When moving data between workbooks or platforms, the underlying serial number does not change, but the date it represents does, depending on the workbook's active date system.\[18\] If a user copies a date from a 1900-system workbook to a 1904-system workbook without conversion, the date will shift by approximately four years.\[10, 18\] For Python developers, identifying the

(0 for 1900, 1 for 1904) is critical to prevent significant data errors.\[17, 20, 21\]

Start Date (Serial 0 or 1)

Offset to Python Epoch

1900 System

Jan 1, 1900 (Serial 1) \[10, 15\]

-25,569 Days (to Unix) \[22\]

Windows, New Mac \[10\]

1904 System

Jan 1, 1904 (Serial 0) \[10, 15\]

-24,107 Days (to Unix) \[10, 22\]

Legacy Mac \[3, 10\]

Procedural Conversion with the Python Standard Library

For developers seeking to convert serial numbers without external dependencies, the

modules provide the necessary primitives. The standard approach involves defining a reference date (the epoch) and adding the serial number as an offset.\[8, 12, 23\]

The logic for a modern date (after March 1, 1900) generally uses December 30, 1899, as the anchor. This compensates for the fact that Excel's serial 1 is January 1, 1900, but its serial 60 is a day that does not exist in the Python

calendar.\[2, 5, 8, 23\] By using December 30, 1899, as the base:

ResultDate = DateTime(1899, 12, 30) + TimeDelta(days=SerialNumber)

This formula correctly maps serial 1 to December 31, 1899, in a proleptic sense, but because Excel is "ahead" by one day after the fake leap day, serial 61 correctly maps to March 1, 1900, in both systems.\[7, 14\] If the application requires handling the small window of dates in January and February 1900, the logic must be branched to account for the off-by-one discrepancy.\[12, 17\]

The conversion of the fractional portion is equally vital. Python's

accepts fractional days, but the internal normalization process converts these to days, seconds, and microseconds.\[24, 25, 26\] This normalization is crucial for maintaining mathematical uniqueness between different durations, ensuring that "2.5 hours" and "150 minutes" resolve to the same internal representation of 9,000 seconds.\[26\]

Vectorized Conversion and Precision in the Pandas Ecosystem

In large-scale data engineering, manual iteration through rows is computationally inefficient. The Pandas library offers a vectorized solution via the

to\_datetime

function, which can interpret a Series of serial numbers in a single operation.\[9, 23, 27\] By specifying

and a custom

, developers can transform raw numeric columns into robust

datetime64\[ns\]

objects.\[9, 27, 28\]

However, the transition to floating-point representation introduces the risk of temporal drift. Python, like most programming languages, implements the IEEE 754 standard for floating-point arithmetic, which approximates real numbers in binary.\[29, 30\] Certain decimal fractions, such as 0.1, have no exact representation in binary, leading to infinite repeating fractions.\[29, 30, 31\] When these approximations are scaled—for instance, converting a fractional day to nanoseconds for a Pandas index—the errors can accumulate.\[29, 32\]

A classic manifestation of this issue is when a serial number representing exactly 12:00:00 PM is converted to a timestamp showing 11:59:59.999971.\[1, 9\] To mitigate this, practitioners often round the result to the nearest minute or second using

.dt.round('1s')

.\[8, 30\] Furthermore, comparing timestamps for equality should avoid the

operator in favor of

math.isclose()

or checking if the absolute difference is within a predefined "epsilon" value, such as

.\[30, 31, 32\]

Logic Component

Configuration in Pandas

'1899-12-30'

Aligns with Excel's effective epoch for 1900 system. \[9\]

Defines the numeric input as days. \[27, 28\]

Error Handling

errors='coerce'

Converts invalid serials to

(Not a Time). \[27, 28, 33\]

dtype='datetime64\[ns\]'

Default Pandas resolution; subject to float error. \[27, 34\]

Deep Dive into Library-Specific Implementations

While Pandas provides the most utility for analysis, other libraries such as

offer specialized methods that are indispensable when dealing with specific Excel file formats or workbook properties.

xlrd and the Legacy Binary Format

library is the traditional choice for reading

(BIFF) files. It handles date conversion through the

module, specifically the

xldate\_as\_datetime

xldate\_as\_tuple

functions.\[17, 20, 35\] A primary advantage of

is its ability to read the

directly from the

object, allowing the code to automatically adapt to either the 1900 or 1904 systems.\[17, 20, 36\]

Crucially, in versions prior to 2.0.0,

would inspect the "number format" applied to a cell. If the format resembled a date, the cell's

would be set to 3 (

XL\_CELL\_DATE

), signaling to the developer that the float should be interpreted as a serial number.\[17, 20, 21\] Modern versions of

have restricted support to

only, requiring other libraries for

openpyxl and the OpenXML Standard

is the preferred interface. It manages "Excel date weirdness" by providing a

utility in the

openpyxl.utils.datetime

module.\[15, 37\] By default,

epoch for reading and the

function for writing serials back to the workbook.\[37\]

allows developers to set the

when writing files, which stores temporal data as ISO 8601 strings rather than serial numbers.\[15\] This is highly recommended for cross-platform data exchange, as it eliminates the ambiguity of the serial number's origin.\[15\] Furthermore,

recognizes time interval durations and can automatically return

objects for cells formatted with

pyxlsb and Binary Compressed Files

format is a binary container that offers faster loading and smaller file sizes for massive datasets. The

library is specifically designed for these files. Because the binary format stores dates as raw floats without the same type-hinting found in XML-based formats,

provides a dedicated

convert\_date

method.\[38\] Developers must manually apply this method to any float that represents a date, as the library does not always automatically differentiate between dates and standard numbers.\[38\]

xlsxwriter: Exporting Temporal Data

When the goal is to generate Excel files from Python,

provides fine-grained control over date formatting. It includes a

write\_datetime

method that accepts native Python

objects and handles the conversion to Excel serial numbers internally.\[11, 39\]

A critical feature of

is its handling of timezones. Since Excel does not natively support timezone-aware timestamps,

remove\_timezone

option in the

constructor.\[11\] If this option is set to

, the library will strip the

from datetime objects before writing them, preventing errors that occur when attempting to map UTC or localized offsets into Excel's naive serial system.\[11, 40\]

Primary Use Case

Key Conversion Method

Date System Detection

files. \[20, 36\]

xldate\_as\_datetime()

book.datemode

files. \[15\]

utils.datetime.from\_excel()

Generating new workbooks. \[11\]

write\_datetime()

remove\_timezone

files. \[38\]

convert\_date()

Manual application required. \[38\]

Cross-Platform Divergence and Interoperability

While Microsoft Excel is the dominant force in the spreadsheet market, the rise of Google Sheets and LibreOffice Calc has introduced new nuances to serial date handling. Both Google Sheets and LibreOffice have chosen to implement the Gregorian calendar correctly, meaning they do not recognize February 29, 1900, as a valid date.\[7, 13, 14\]

In these alternative applications, the "Day 0" is correctly identified as December 30, 1899.\[7, 14\] Consequently, a serial number of 1 in Google Sheets results in December 31, 1899, whereas in Excel it results in January 1, 1900.\[7\] This divergence persists for the first 60 days of the year 1900. By March 1, 1900 (serial number 61), the systems synchronize, as Excel's "extra day" has already occurred.\[7, 14\] For analysts working with early 20th-century historical records, this means that the platform from which the data was exported is as important as the serial number itself.\[7, 13, 16\]

Historical Data Challenges and Pre-1900 Logic

The spreadsheet serial number system was essentially designed for modern business use, which seldom involves dates before the 20th century. Excel is inherently incapable of handling dates before January 1, 1900.\[3, 15, 16\] Any attempt to enter a date like "July 4, 1776" into Excel results in the application treating it as a literal string rather than a serial number.\[13, 16\]

When these mixed-format workbooks are imported into Python via Pandas or

, the resulting data structures are often heterogeneous, containing a mix of floats and strings.\[16, 41\] For data engineers, this necessitates a "cleaning" phase where strings are parsed into

objects and serial numbers are converted using the 1899-12-30 epoch.\[41\] In cases where data integrity is paramount, some practitioners choose to replace all dates before 1900 with

(Not a Number) or

to avoid the risk of mixed-type columns causing downstream failures in analytical models.\[41, 42\]

Bridging Temporal Epochs: Unix, SQL, and Beyond

In many data architectures, Excel is merely one stop in a longer journey that involves SQL databases and Unix-based systems. Unix timestamps represent the number of seconds since January 1, 1970 (the Unix Epoch).\[43, 44\] Converting between Unix and Excel serials requires reconciling both the unit (seconds vs. days) and the offset between epochs.\[22, 45\]

The Unix epoch of January 1, 1970, corresponds to Excel serial number 25,569.\[22\] To convert a Unix timestamp (

) to an Excel serial (

) in Python, the formula is:

E = \frac{U}{86400} + 25569

If the Unix timestamp is in milliseconds, the divisor increases to

.\[22\] This relationship is also common in database systems like SQL Server or Access, which often use December 30, 1899, as their internal base date to remain compatible with the spreadsheet ecosystem.\[2, 45\] For developers, this shared lineage simplifies the process of moving data between Access MDB files and Python dataframes, as the same 1899-12-30 anchor remains valid.\[2, 45\]

Numerical Stability and the Risks of Fractional Arithmetic

The inherent limitations of floating-point representation in binary systems can lead to "temporal jitter"—small errors in the microsecond or nanosecond range that occur during the conversion process.\[9, 29\] This is not a bug in Python or Excel but a fundamental consequence of how fractional numbers are stored in a fixed number of bits.\[29, 30\]

objects use integer arithmetic for days, seconds, and microseconds, but the Excel serial number is a single float.\[12, 24\] When we divide seconds by 86,400 to get a fraction of a day, the resulting number might be slightly off. Conversely, when we multiply an Excel fraction by 86,400, we might get

#### To ensure stability in financial or scientific applications:

module for all intermediate arithmetic to maintain absolute precision.\[29, 30, 32\]

Always round to the expected precision of the source data (e.g., milliseconds for XLSX) immediately after conversion.\[8, 15\]

#### When performing comparisons, use a tolerance-based approach:

abs(time1 - time2) < timedelta(milliseconds=1)

Conclusions and Practical Synthesis

The conversion of date serial numbers in Python is a sophisticated task that requires more than a simple arithmetic operation. It demands an awareness of the 1900 leap year bug, an understanding of the 1,462-day shift between PC and legacy Mac workbooks, and a defensive strategy against floating-point inaccuracies.

For professional peers developing data pipelines, the following heuristics should be standard practice:

for vectorized, high-performance conversion of modern dates, leveraging the

origin='1899-12-30'

parameter to automatically correct for the 1900 bug.\[9, 27\]

to read the workbook's internal

property before processing, ensuring that 1904-system files do not introduce a four-year error.\[15, 20\]

When writing dates back to Excel, prefer

ISO 8601 strings

where supported, or use

xlsxwriter's

timezone-stripping options to avoid naive vs. aware datetime conflicts.\[11, 15\]

post-conversion to eliminate binary approximation noise, particularly when the resulting timestamps will be used for indexing or equality-based joins.\[8, 32\]

By integrating these strategies, developers can bridge the gap between the idiosyncratic temporal logic of legacy spreadsheets and the precise, standards-compliant environment of modern Python development. This ensures not only the accuracy of the conversion but the long-term reliability of the data analysis and reporting lifecycle.

--------------------------------------------------------------------------------

Excel incorrectly assumes that the year 1900 is a leap year | "Although it is technically possible to correct this behavior, the disadvantages of doing so outweigh the advantages." : r/technology - Reddit,

https://www.reddit.com/r/technology/comments/1sgy8hv/excel\_incorrectly\_assumes\_that\_the\_year\_1900\_is\_a/

https://www.reddit.com/r/technology/comments/1sgy8hv/excel\_incorrectly\_assumes\_that\_the\_year\_1900\_is\_a/

Why is 1899-12-30 the zero date in Access / SQL Server instead of 12/31? - Stack Overflow,

https://stackoverflow.com/questions/3963617/why-is-1899-12-30-the-zero-date-in-access-sql-server-instead-of-12-31

https://stackoverflow.com/questions/3963617/why-is-1899-12-30-the-zero-date-in-access-sql-server-instead-of-12-31

Year 1900 problem - Wikipedia,

https://en.wikipedia.org/wiki/Year\_1900\_problem

https://en.wikipedia.org/wiki/Year\_1900\_problem

Excel incorrectly assumes that the year 1900 is a leap year ...,

https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/wrongly-assumes-1900-is-leap-year

https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/wrongly-assumes-1900-is-leap-year

How to convert a python datetime.datetime to excel serial date number - Stack Overflow,

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

Excel calculates dates WRONG, so please be careful. : r/AskStatistics - Reddit,

https://www.reddit.com/r/AskStatistics/comments/7uk40z/excel\_calculates\_dates\_wrong\_so\_please\_be\_careful/

https://www.reddit.com/r/AskStatistics/comments/7uk40z/excel\_calculates\_dates\_wrong\_so\_please\_be\_careful/

Why does the same value produce different outputs when formatted as a date in Excel compared to Google Sheets? - Web Applications Stack Exchange,

https://webapps.stackexchange.com/questions/104081/why-does-the-same-value-produce-different-outputs-when-formatted-as-a-date-in-ex

https://webapps.stackexchange.com/questions/104081/why-does-the-same-value-produce-different-outputs-when-formatted-as-a-date-in-ex

convert Excel serial date to python datetime.datetime · GitHub - GitHub Gist,

https://gist.github.com/9959241

https://gist.github.com/9959241

Convert Excel style date with pandas - Stack Overflow,

https://stackoverflow.com/questions/38454403/convert-excel-style-date-with-pandas

https://stackoverflow.com/questions/38454403/convert-excel-style-date-with-pandas

Date systems in Excel - Microsoft Support,

https://support.microsoft.com/en-us/office/date-systems-in-excel-e7fe7167-48a9-4b96-bb53-5612a800b487

https://support.microsoft.com/en-us/office/date-systems-in-excel-e7fe7167-48a9-4b96-bb53-5612a800b487

Working with Dates and Time - XlsxWriter,

https://xlsxwriter.readthedocs.io/working\_with\_dates\_and\_time.html

https://xlsxwriter.readthedocs.io/working\_with\_dates\_and\_time.html

How to Convert a Python datetime.datetime to Excel Serial Date Number? - TutorialsPoint,

https://www.tutorialspoint.com/article/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

https://www.tutorialspoint.com/article/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

Dates as Data – Data Organization in Spreadsheets - Carpentry @ UCSB Library,

https://carpentry.library.ucsb.edu/2022-10-11-ucsb-spreadsheets/03-dates-as-data/

https://carpentry.library.ucsb.edu/2022-10-11-ucsb-spreadsheets/03-dates-as-data/

xlf :: Spreadsheet date comparisons - Excel at Finance,

https://excelatfinance.com/online2/xlf-spreadsheet-date-comparisons.php

https://excelatfinance.com/online2/xlf-spreadsheet-date-comparisons.php

Dates and Times — openpyxl 3.1.4 documentation,

https://openpyxl.readthedocs.io/en/3.1/datetime.html

https://openpyxl.readthedocs.io/en/3.1/datetime.html

Tidy data for librarians: Dates as data - Library Carpentry,

https://librarycarpentry.github.io/lc-spreadsheets/instructor/03-dates-as-data.html

https://librarycarpentry.github.io/lc-spreadsheets/instructor/03-dates-as-data.html

Dates in Excel spreadsheets — xlrd 2.0.1 documentation - Read the Docs,

https://xlrd.readthedocs.io/en/latest/dates.html

https://xlrd.readthedocs.io/en/latest/dates.html

Microsoft Excel Date Munging: 1900 vs. 1904 Date System - nuxx.net,

https://nuxx.net/blog/2011/09/21/microsoft-excel-date-munging-1900-vs-1904-date-system/

https://nuxx.net/blog/2011/09/21/microsoft-excel-date-munging-1900-vs-1904-date-system/

Apache POI 1904 date - Alan Dix,

https://alandix.com/code2/apache-poi-detect-1904-date-option/

https://alandix.com/code2/apache-poi-detect-1904-date-option/

xlrd.xldate\_as\_tuple()

- Stack Overflow,

https://stackoverflow.com/questions/3727916/how-to-use-xlrd-xldate-as-tuple

https://stackoverflow.com/questions/3727916/how-to-use-xlrd-xldate-as-tuple

How do I read a date in Excel format in Python? - Stack Overflow,

https://stackoverflow.com/questions/1108428/how-do-i-read-a-date-in-excel-format-in-python

https://stackoverflow.com/questions/1108428/how-do-i-read-a-date-in-excel-format-in-python

Converting unix time into date-time via excel - Stack Overflow,

https://stackoverflow.com/questions/46130132/converting-unix-time-into-date-time-via-excel

https://stackoverflow.com/questions/46130132/converting-unix-time-into-date-time-via-excel

How Do I Convert Excel Dates And Numbers Into Usable Python Types? - YouTube,

https://www.youtube.com/watch?v=BZkwROtpFQU

https://www.youtube.com/watch?v=BZkwROtpFQU

datetime — Basic date and time types — Python 3.14.5 documentation,

https://docs.python.org/3/library/datetime.html

https://docs.python.org/3/library/datetime.html

Python timedelta seconds vs total\_seconds - Stack Overflow,

https://stackoverflow.com/questions/51652952/python-timedelta-seconds-vs-total-seconds

https://stackoverflow.com/questions/51652952/python-timedelta-seconds-vs-total-seconds

Time deltas are not intuitive - Mostly Python,

https://www.mostlypython.com/time-deltas-are-not-intuitive/

https://www.mostlypython.com/time-deltas-are-not-intuitive/

pandas.to\_datetime — pandas 3.0.3 documentation - PyData |,

https://pandas.pydata.org/docs/reference/api/pandas.to\_datetime.html

https://pandas.pydata.org/docs/reference/api/pandas.to\_datetime.html

Pandas to\_datetime: Convert Strings, Timestamps, and Mixed Formats - Kanaries Docs,

https://docs.kanaries.net/topics/Pandas/pandas-to-datetime

https://docs.kanaries.net/topics/Pandas/pandas-to-datetime

Floating point error in Python - GeeksforGeeks,

https://www.geeksforgeeks.org/python/floating-point-error-in-python/

https://www.geeksforgeeks.org/python/floating-point-error-in-python/

Floating-Point Precision in Programming - DEV Community,

https://dev.to/dilanblog/understanding-floating-point-precision-in-programming-h7

https://dev.to/dilanblog/understanding-floating-point-precision-in-programming-h7

\[Python\] Adding floating point number causes precision issues for some numbers but not othera. - Reddit,

https://www.reddit.com/r/learnprogramming/comments/192tkp0/python\_adding\_floating\_point\_number\_causes/

https://www.reddit.com/r/learnprogramming/comments/192tkp0/python\_adding\_floating\_point\_number\_causes/

Understanding Floating-Point Precision Issues in Python: A Practical Guide - Medium,

https://medium.com/@goldengrisha/understanding-floating-point-precision-issues-in-python-a-practical-guide-5e17b2f14057

https://medium.com/@goldengrisha/understanding-floating-point-precision-issues-in-python-a-practical-guide-5e17b2f14057

Pandas.to\_datetime()-Python - GeeksforGeeks,

https://www.geeksforgeeks.org/pandas/python-pandas-to\_datetime/

https://www.geeksforgeeks.org/pandas/python-pandas-to\_datetime/

Exploring dates and times in Python - Bits of Analytics,

https://bitsofanalytics.org/posts/python-datetime/python\_datetime

https://bitsofanalytics.org/posts/python-datetime/python\_datetime

Convert excel serial date to datetime - Python - GeeksforGeeks,

https://www.geeksforgeeks.org/python/python-convert-excel-serial-date-to-datetime/

https://www.geeksforgeeks.org/python/python-convert-excel-serial-date-to-datetime/

API Reference — xlrd 2.0.1 documentation,

https://xlrd.readthedocs.io/en/latest/api.html

https://xlrd.readthedocs.io/en/latest/api.html

openpyxl.utils.datetime module — openpyxl 3.1.4 documentation,

https://openpyxl.readthedocs.io/en/3.1/api/openpyxl.utils.datetime.html

https://openpyxl.readthedocs.io/en/3.1/api/openpyxl.utils.datetime.html

pyxlsb · PyPI,

https://pypi.org/project/pyxlsb/

https://pypi.org/project/pyxlsb/

Example: Dates and Times in Excel - XlsxWriter,

https://xlsxwriter.readthedocs.io/example\_datetimes.html

https://xlsxwriter.readthedocs.io/example\_datetimes.html

Example: Pandas Excel output with datetimes - XlsxWriter,

https://xlsxwriter.readthedocs.io/example\_pandas\_datetime.html

https://xlsxwriter.readthedocs.io/example\_pandas\_datetime.html

python - How to handle "old" dates when transfering data to excel - Stack Overflow,

https://stackoverflow.com/questions/37047526/python-how-to-handle-old-dates-when-transfering-data-to-excel

https://stackoverflow.com/questions/37047526/python-how-to-handle-old-dates-when-transfering-data-to-excel

PYTHON Convert dates under 1900 (Negatives) to text date xlrd EXCEL - Stack Overflow,

https://stackoverflow.com/questions/46182724/python-convert-dates-under-1900-negatives-to-text-date-xlrd-excel

https://stackoverflow.com/questions/46182724/python-convert-dates-under-1900-negatives-to-text-date-xlrd-excel

Python program to convert unix timestamp string to readable date - GeeksforGeeks,

https://www.geeksforgeeks.org/python/python-program-to-convert-unix-timestamp-string-to-readable-date/

https://www.geeksforgeeks.org/python/python-program-to-convert-unix-timestamp-string-to-readable-date/

How to Convert Unix Timestamps to Readable Dates in Python - Statology,

https://www.statology.org/how-to-convert-unix-timestamps-to-readable-dates-in-python/

https://www.statology.org/how-to-convert-unix-timestamps-to-readable-dates-in-python/

Converting Unix timestamp to date format in an Excel spreadsheet,

https://knowledge.broadcom.com/external/article/24040/converting-unix-timestamp-to-date-format.html

https://knowledge.broadcom.com/external/article/24040/converting-unix-timestamp-to-date-format.html


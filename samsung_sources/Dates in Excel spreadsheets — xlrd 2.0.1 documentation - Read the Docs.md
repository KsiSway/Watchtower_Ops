---
sourceFile: "Dates in Excel spreadsheets — xlrd 2.0.1 documentation - Read the Docs"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.311Z"
---

# Dates in Excel spreadsheets — xlrd 2.0.1 documentation - Read the Docs

64d84836-24c3-42ee-b0a8-d8ab261787d9

Dates in Excel spreadsheets — xlrd 2.0.1 documentation - Read the Docs

dff6294c-34d6-42f2-9a48-096a4bc35915

https://xlrd.readthedocs.io/en/latest/dates.html

Dates in Excel spreadsheets — xlrd 2.0.1 documentation

https://xlrd.readthedocs.io/en/latest/index.html

Handling of Unicode

https://xlrd.readthedocs.io/en/latest/unicode.html

Dates in Excel spreadsheets

https://xlrd.readthedocs.io/en/latest/dates.html

Named references, constants, formulas, and macros

https://xlrd.readthedocs.io/en/latest/references.html

Formatting information in Excel Spreadsheets

https://xlrd.readthedocs.io/en/latest/formatting.html

Loading worksheets on demand

https://xlrd.readthedocs.io/en/latest/on\_demand.html

API Reference

https://xlrd.readthedocs.io/en/latest/api.html

Development

https://xlrd.readthedocs.io/en/latest/development.html

https://xlrd.readthedocs.io/en/latest/changes.html

Acknowledgements

https://xlrd.readthedocs.io/en/latest/acknowledgements.html

https://xlrd.readthedocs.io/en/latest/licenses.html

https://xlrd.readthedocs.io/en/latest/index.html

https://xlrd.readthedocs.io/en/latest/index.html

Dates in Excel spreadsheets

Edit on GitHub

https://github.com/python-excel/xlrd/blob/master/docs/dates.rst

Dates in Excel spreadsheets

https://xlrd.readthedocs.io/en/latest/dates.html#dates-in-excel-spreadsheets

In reality, there are no such things. What you have are floating point numbers and pious hope. There are several problems with Excel dates:

Dates are not stored as a separate data type; they are stored as floating point numbers and you have to rely on:

the “number format” applied to them in Excel and/or

knowing which cells are supposed to have dates in them. This module helps with the former by inspecting the format that has been applied to each number cell; if it appears to be a date format, the cell is classified as a date rather than a number. Feedback on this feature, especially from non-English-speaking locales, would be appreciated.

Excel for Windows stores dates by default as the number of days (or fraction thereof) since

1899-12-31T00:00:00

. Excel for Macintosh uses a default start date of

1904-01-01T00:00:00

. The date system can be changed in Excel on a per-workbook basis (for example: Tools -> Options -> Calculation, tick the “1904 date system” box). This is of course a bad idea if there are already dates in the workbook. There is no good reason to change it even if there are no dates in the workbook. Which date system is in use is recorded in the workbook. A workbook transported from Windows to Macintosh (or vice versa) will work correctly with the host Excel. When using this package's

xldate\_as\_tuple()

https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.xldate\_as\_tuple

function to convert numbers from a workbook, you must use the

attribute of the

object. If you guess, or make a judgement depending on where you believe the workbook was created, you run the risk of being 1462 days out of kilter. Reference:

https://support.microsoft.com/en-us/help/180162/xl-the-1900-date-system-vs.-the-1904-date-system

https://support.microsoft.com/en-us/help/180162/xl-the-1900-date-system-vs.-the-1904-date-system

The Excel implementation of the Windows-default 1900-based date system works on the incorrect premise that 1900 was a leap year. It interprets the number 60 as meaning

, which is not a valid date. Consequently, any number less than 61 is ambiguous. For example, is 59 the result of

entered directly, or is it

minus 2 days? The OpenOffice.org Calc program “corrects” the Microsoft problem; entering

causes the number 59 to be stored. Save as an XLS file, then open the file with Excel and you'll see

displayed. Reference:

https://support.microsoft.com/en-us/help/214326/excel-incorrectly-assumes-that-the-year-1900-is-a-leap-year

https://support.microsoft.com/en-us/help/214326/excel-incorrectly-assumes-that-the-year-1900-is-a-leap-year

The Macintosh-default 1904-based date system counts

as day 1 and

as day zero. Thus any number such that

(0.0 <= number < 1.0)

is ambiguous. Is 0.625 a time of day (

), independent of the calendar, or should it be interpreted as an instant on a particular day (

1904-01-01T15:00:00

)? The functions in

https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.xldate

take the view that such a number is a calendar-independent time of day (like Python's

datetime.time

https://docs.python.org/3/library/datetime.html#datetime.time

type) for both date systems. This is consistent with more recent Microsoft documentation. For example, the help file for Excel 2002, which says that the first day in the 1904 date system is

Usage of the Excel

function may leave strange dates in a spreadsheet. Quoting the help file in respect of the 1900 date system:

If year is between 0 (zero) and 1899 (inclusive),
Excel adds that value to 1900 to calculate the year.
For example, DATE(108,1,2) returns January 2, 2008 (1900+108).

This gimmick, semi-defensible only for arguments up to 99 and only in the pre-Y2K-awareness era, means that

DATE(1899, 12, 31)

is interpreted as

. For further information, please refer to the documentation for the functions in

https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.xldate

https://xlrd.readthedocs.io/en/latest/references.html

https://xlrd.readthedocs.io/en/latest/unicode.html

© Copyright 2005-2019 Stephen John Machin, Lingfo Pty Ltd. 2019-2021 Chris Withers Revision

http://sphinx-doc.org/

https://github.com/rtfd/sphinx\_rtd\_theme

provided by

Read the Docs

https://readthedocs.org/

https://xlrd.readthedocs.io/en/stable/dates.html

On Read the Docs

Project Home

https://app.readthedocs.org/projects/xlrd/?utm\_source=xlrd&utm\_content=flyout

https://app.readthedocs.org/projects/xlrd/builds/?utm\_source=xlrd&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=xlrd&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=xlrd&utm\_content=flyout

Simplify infrastructure with MongoDB Atlas, the leading modern database

https://server.ethicalads.io/proxy/click/10498/019e440e-9c28-7620-bb1b-14c70463ec3e/

Ads by EthicalAds

https://www.ethicalads.io/advertisers/?ref=ea-text

No recent searches

to navigate

Search powered by


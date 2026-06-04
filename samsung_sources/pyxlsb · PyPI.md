---
sourceFile: "pyxlsb · PyPI"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.595Z"
---

# pyxlsb · PyPI

a177878d-147f-4bfa-a312-d66ddbd555f5

pyxlsb · PyPI

ec5b18ba-2792-4221-b9fd-a055e8b9dddb

https://pypi.org/project/pyxlsb/

pyxlsb · PyPI

Skip to main content

https://pypi.org/project/pyxlsb/#content

Switch to mobile version

Warning Some features may not work without JavaScript. Please try enabling it if you encounter problems.

Search PyPI Search

https://pypi.org/help/

https://docs.pypi.org/

https://pypi.org/sponsors/

https://pypi.org/account/login/?next=https%3A%2F%2Fpypi.org%2Fproject%2Fpyxlsb%2F

https://pypi.org/account/register/

https://pypi.org/help/

https://docs.pypi.org/

https://pypi.org/sponsors/

https://pypi.org/account/login/?next=https%3A%2F%2Fpypi.org%2Fproject%2Fpyxlsb%2F

https://pypi.org/account/register/

Search PyPI Search

pyxlsb 1.0.10

pip install pyxlsb Copy PIP instructions

Latest version

https://pypi.org/project/pyxlsb/

Released: Oct 14, 2022

Excel 2007-2010 Binary Workbook (xlsb) parser

Project description

https://pypi.org/project/pyxlsb/#description

Release history

https://pypi.org/project/pyxlsb/#history

Download files

https://pypi.org/project/pyxlsb/#files

Verified details

These details have been verified by PyPI

Maintainers

https://pypi.org/user/wiill/

Unverified details

These details have not been verified by PyPI

Project links

https://github.com/willtrnr/pyxlsb

GNU Lesser General Public License v3 or later (LGPLv3+) (LGPLv3+)

William Turner

mailto:willtur.will@gmail.com

Classifiers

Development Status

5 - Production/Stable

https://pypi.org/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable

OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)

https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Lesser+General+Public+License+v3+or+later+%28LGPLv3%2B%29

Programming Language

Python :: 2

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+2

Python :: 2.7

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+2.7

Python :: 3

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3

Python :: 3.5

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.5

Python :: 3.6

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.6

Python :: 3.7

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.7

Python :: 3.8

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.8

Python :: 3.9

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.9

AWS is a Maintaining sponsor of the Python Software Foundation.

PSF Sponsor

https://www.python.org/psf/sponsorship/?ref=ethicalads-placement

Served ethically

https://www.ethicalads.io/sponsorship-platform/?ref=psf

Report project as malware

https://pypi.org/project/pyxlsb/submit-malware-report/

Project description

https://pypi.org/project/pyxlsb/#description

Project details

https://pypi.org/project/pyxlsb/#data

Release history

https://pypi.org/project/pyxlsb/#history

Download files

https://pypi.org/project/pyxlsb/#files

Project description

pyxlsb is an Excel 2007-2010 Binary Workbook (xlsb) parser for Python. The library is currently extremely limited, but functional enough for basic data extraction.

pip install pyxlsb

The module exposes an open\_workbook(name) method (similar to Xlrd and OpenPyXl) for opening XLSB files. The Workbook object representing the file is returned.

from pyxlsb import open\_workbook
with open\_workbook('Book1.xlsb') as wb:
    # Do stuff with wb

The Workbook object exposes a get\_sheet(idx) method for retrieving a Worksheet instance.

# Using the sheet index (1-based)
with wb.get\_sheet(1) as sheet:
    # Do stuff with sheet

# Using the sheet name
with wb.get\_sheet('Sheet1') as sheet:
    # Do stuff with sheet

Tip: A sheets property containing the sheet names is available on the Workbook instance.

The rows() method will hand out an iterator to read the worksheet rows.

# You can use .rows(sparse=True) to skip empty rows
for row in sheet.rows():
    print(row)
# \[Cell(r=0, c=0, v='TEXT'), Cell(r=0, c=1, v=42.1337)\]

Do note that dates will appear as floats. You must use the convert\_date(date) method from the pyxlsb module to turn them into datetime instances.

from pyxlsb import convert\_date
print(convert\_date(41235.45578))
# datetime.datetime(2012, 11, 22, 10, 56, 19)

Project details

Verified details

These details have been verified by PyPI

Maintainers

https://pypi.org/user/wiill/

Unverified details

These details have not been verified by PyPI

Project links

https://github.com/willtrnr/pyxlsb

GNU Lesser General Public License v3 or later (LGPLv3+) (LGPLv3+)

William Turner

mailto:willtur.will@gmail.com

Classifiers

Development Status

5 - Production/Stable

https://pypi.org/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable

OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)

https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Lesser+General+Public+License+v3+or+later+%28LGPLv3%2B%29

Programming Language

Python :: 2

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+2

Python :: 2.7

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+2.7

Python :: 3

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3

Python :: 3.5

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.5

Python :: 3.6

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.6

Python :: 3.7

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.7

Python :: 3.8

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.8

Python :: 3.9

https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.9

Release history

Release notifications

https://pypi.org/help/#project-release-notifications

https://pypi.org/rss/project/pyxlsb/releases.xml

#### This version

1.0.10 Oct 14, 2022

https://pypi.org/project/pyxlsb/1.0.10/

1.0.9 Nov 4, 2021

https://pypi.org/project/pyxlsb/1.0.9/

1.0.8 Jan 17, 2021

https://pypi.org/project/pyxlsb/1.0.8/

1.0.7 Dec 14, 2020

https://pypi.org/project/pyxlsb/1.0.7/

1.0.6 Jan 2, 2020

https://pypi.org/project/pyxlsb/1.0.6/

1.0.5 May 7, 2019

https://pypi.org/project/pyxlsb/1.0.5/

1.0.4 Oct 31, 2018

https://pypi.org/project/pyxlsb/1.0.4/

1.0.3 Nov 23, 2017

https://pypi.org/project/pyxlsb/1.0.3/

1.0.2 Nov 21, 2017

https://pypi.org/project/pyxlsb/1.0.2/

1.0.1 Sep 27, 2017

https://pypi.org/project/pyxlsb/1.0.1/

Download files

Download the file for your platform. If you're not sure which to choose, learn more about

installing packages

https://packaging.python.org/tutorials/installing-packages/

Source Distribution

pyxlsb-1.0.10.tar.gz

https://files.pythonhosted.org/packages/3f/13/eebaeb7a40b062d1c6f7f91d09e73d30a69e33e4baa7cbe4b7658548b1cd/pyxlsb-1.0.10.tar.gz

view details

https://pypi.org/project/pyxlsb/#pyxlsb-1.0.10.tar.gz

Uploaded Oct 14, 2022

Built Distribution

Filter files by name, interpreter, ABI, and platform.

If you're not sure about the file name format, learn more about

wheel file names

https://packaging.python.org/en/latest/specifications/binary-distribution-format/

The dropdown lists show the available interpreters, ABIs, and platforms.

Enable javascript to be able to filter the list of wheel files.

Copy a direct link to the current filters

https://pypi.org/project/pyxlsb/#files

https://pypi.org/project/pyxlsb/#files

Showing 1 of 1 file.

Interpreter

Interpreter

pyxlsb-1.0.10-py2.py3-none-any.whl

https://files.pythonhosted.org/packages/7e/92/345823838ae367c59b63e03aef9c331f485370f9df6d049256a61a28f06d/pyxlsb-1.0.10-py2.py3-none-any.whl

view details

https://pypi.org/project/pyxlsb/#pyxlsb-1.0.10-py2.py3-none-any.whl

Uploaded Oct 14, 2022

File details

Details for the file

pyxlsb-1.0.10.tar.gz

File metadata

#### Download URL:

pyxlsb-1.0.10.tar.gz

https://files.pythonhosted.org/packages/3f/13/eebaeb7a40b062d1c6f7f91d09e73d30a69e33e4baa7cbe4b7658548b1cd/pyxlsb-1.0.10.tar.gz

Upload date: Oct 14, 2022

Size: 22.4 kB

Tags: Source

Uploaded using Trusted Publishing? No

Uploaded via: twine/3.6.0 importlib\_metadata/4.8.1 pkginfo/1.8.3 requests/2.28.1 requests-toolbelt/0.9.1 tqdm/4.64.0 CPython/3.10.5

File hashes

Hashes for pyxlsb-1.0.10.tar.gz

Hash digest

8062d1ea8626d3f1980e8b1cfe91a4483747449242ecb61013bc2df85435f685

e5d1117c2c5fffc9fdc872f0b7ea18a1

BLAKE2b-256

3f13eebaeb7a40b062d1c6f7f91d09e73d30a69e33e4baa7cbe4b7658548b1cd

See more details on using hashes here.

https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode

File details

Details for the file

pyxlsb-1.0.10-py2.py3-none-any.whl

File metadata

#### Download URL:

pyxlsb-1.0.10-py2.py3-none-any.whl

https://files.pythonhosted.org/packages/7e/92/345823838ae367c59b63e03aef9c331f485370f9df6d049256a61a28f06d/pyxlsb-1.0.10-py2.py3-none-any.whl

Upload date: Oct 14, 2022

Size: 23.8 kB

Tags: Python 2, Python 3

Uploaded using Trusted Publishing? No

Uploaded via: twine/3.6.0 importlib\_metadata/4.8.1 pkginfo/1.8.3 requests/2.28.1 requests-toolbelt/0.9.1 tqdm/4.64.0 CPython/3.10.5

File hashes

Hashes for pyxlsb-1.0.10-py2.py3-none-any.whl

Hash digest

87c122a9a622e35ca5e741d2e541201d28af00fb46bec492cfa9586890b120b4

5002b1a44372e94d719284cbc9ec10b7

BLAKE2b-256

7e92345823838ae367c59b63e03aef9c331f485370f9df6d049256a61a28f06d

See more details on using hashes here.

https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode

Installing packages

https://packaging.python.org/tutorials/installing-packages/

Uploading packages

https://packaging.python.org/tutorials/packaging-projects/

https://packaging.python.org/

Project name retention

https://www.python.org/dev/peps/pep-0541/

https://pypi.org/help/

https://blog.pypi.org/

Infrastructure dashboard

https://dtdg.co/pypi

https://pypi.org/stats/

Logos & trademarks

https://pypi.org/trademarks/

Our sponsors

https://pypi.org/sponsors/

Contributing to PyPI

Bugs and feedback

https://pypi.org/help/#feedback

Contribute on GitHub

https://github.com/pypi/warehouse

Translate PyPI

https://hosted.weblate.org/projects/pypa/warehouse/

Sponsor PyPI

https://pypi.org/sponsors/

Development credits

https://github.com/pypi/warehouse/graphs/contributors

Terms of Service

https://policies.python.org/pypi.org/Terms-of-Service/

Report security issue

https://pypi.org/security/

Code of conduct

https://policies.python.org/python.org/code-of-conduct/

Privacy Notice

https://policies.python.org/pypi.org/Privacy-Notice/

Acceptable Use Policy

https://policies.python.org/pypi.org/Acceptable-Use-Policy/

All Systems Operational

https://status.python.org/

Developed and maintained by the Python community, for the Python community.

Donate today!

https://donate.pypi.org/

"PyPI", "Python Package Index", and the blocks logos are registered

https://pypi.org/trademarks/

Python Software Foundation

https://www.python.org/psf-landing

Python Software Foundation

https://www.python.org/psf-landing/

https://pypi.org/sitemap/

Deployed from

https://github.com/pypi/warehouse/commit/dec24d31e87c725ceab02a0ab3fdafae61845aee

Switch to desktop version

português (Brasil)

Supported by

AWS Cloud computing and Security Sponsor

https://aws.amazon.com/

Datadog Monitoring

https://www.datadoghq.com/

Depot Continuous Integration

https://depot.dev/

https://www.fastly.com/

Google Download Analytics

https://careers.google.com/

Pingdom Monitoring

https://www.pingdom.com/

Sentry Error logging

https://sentry.io/for/python/?utm\_source=pypi&utm\_medium=paid-community&utm\_campaign=python-na-evergreen&utm\_content=static-ad-pypi-sponsor-learnmore

StatusPage Status page

https://statuspage.io/


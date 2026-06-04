---
sourceFile: "How to convert a python datetime.datetime to excel serial date number - Stack Overflow"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.390Z"
---

# How to convert a python datetime.datetime to excel serial date number - Stack Overflow

497627f9-b775-4aa7-b774-39bb61905653

How to convert a python datetime.datetime to excel serial date number - Stack Overflow

29a72194-c59d-4f71-925f-608682506562

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

How to convert a python datetime.datetime to excel serial date number - Stack Overflow

By clicking “Sign up”, you agree to our

terms of service

https://stackoverflow.com/legal/terms-of-service/public

and acknowledge you have read our

privacy policy

https://stackoverflow.com/legal/privacy-policy

Sign up with Google

Sign up with GitHub

Already have an account?

https://stackoverflow.com/users/login

Skip to main content

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#content

1. \[Home\](https://stackoverflow.com/)
2. \[Questions\](https://stackoverflow.com/questions)
3. \[AI Assist\](https://stackoverflow.com/ai-assist)
4. \[Tags\](https://stackoverflow.com/tags)
5.
6. \[Challenges\](https://stackoverflow.com/beta/challenges)
7. \[Chat\](https://chat.stackoverflow.com/?tab=explore)
8. \[Articles\](https://stackoverflow.blog/contributed?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=so-blog&utm\_content=experiment-articles)
9. \[Users\](https://stackoverflow.com/users)
10.
11. \[Companies\](https://stackoverflow.com/jobs/companies?so\_medium=stackoverflow&so\_source=SiteNav)
12. \[Collectives\](javascript:void(0))
13. Communities for your favorite technologies. \[Explore all Collectives\](https://stackoverflow.com/collectives-all)

Stack Internal Stack Overflow for Teams is now called

Stack Internal

. Bring the best of human thought and AI automation together at your work.

Try for free

https://stackoverflowteams.com/teams/create/free/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=side-bar&utm\_content=explore-teams

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=side-bar&utm\_content=explore-teams

Stack Internal

javascript:void(0)

Bring the best of human thought and AI automation together at your work.

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=side-bar&utm\_content=explore-teams-compact

Collectives™ on Stack Overflow

Find centralized, trusted content and collaborate around the technologies you use most.

Learn more about Collectives

https://stackoverflow.com/collectives

Stack Internal

Knowledge at work

Bring the best of human thought and AI automation together at your work.

Explore Stack Internal

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=side-bar&utm\_content=explore-teams-compact-popover

https://stackoverflow.com/

https://stackoverflow.co/

https://stackoverflow.co/internal/

Stack Internal Implement a knowledge platform layer to power your enterprise and AI tools.

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=stack-overflow-for-teams

Stack Data Licensing Get access to top-class technical expertise with trusted & attributed content.

https://stackoverflow.co/data-licensing/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=overflow-api

Stack Ads Connect your brand to the world's most trusted technologist communities.

https://stackoverflow.co/advertising/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=stack-overflow-advertising

Releases Keep up-to-date on features we add to Stack Overflow and Stack Internal.

https://stackoverflow.blog/releases/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=releases

About the company

https://stackoverflow.co/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=about-the-company

Visit the blog

https://stackoverflow.blog/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=top-nav&utm\_content=blog

Tour Start here for a quick overview of the site

https://stackoverflow.com/tour

Help Center Detailed answers to any questions you might have

https://stackoverflow.com/help

Meta Discuss the workings and policies of this site

https://meta.stackoverflow.com/

About Us Learn more about Stack Overflow the company, and our products

https://stackoverflow.co/

current community

https://stackoverflow.com/

Stack Overflow

https://stackoverflow.com/

https://stackoverflow.com/help

https://chat.stackoverflow.com/?tab=explore

Meta Stack Overflow

https://meta.stackoverflow.com/

your communities

https://stackoverflow.com/users/signup?ssrc=site\_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f9574793%2fhow-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

https://stackoverflow.com/users/login?ssrc=site\_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f9574793%2fhow-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

to customize your list.

more stack exchange communities

https://stackexchange.com/sites

company blog

https://stackoverflow.blog/

https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f9574793%2fhow-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f9574793%2fhow-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

How to convert a python datetime.datetime to excel serial date number

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

Ask Question

https://stackoverflow.com/questions/ask

Asked 14 years, 2 months ago

8 months ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number?lastactivity

Viewed 76k times

This question shows research effort; it is useful and clear

This question does not show any research effort; it is unclear or not useful

Save this question.

https://stackoverflow.com/posts/9574793/timeline

Show activity on this post.

I need to convert dates into Excel serial numbers for a data munging script I am writing. By playing with dates in my OpenOffice Calc workbook, I was able to deduce that '1-Jan 1899 00:00:00' maps to the number zero.

I wrote the following function to convert from a python datetime object into an Excel serial number:

def excel\_date(date1):
    temp=dt.datetime.strptime('18990101', '%Y%m%d')
    delta=date1-temp
    total\_seconds = delta.days \* 86400 + delta.seconds
    return total\_seconds

However, when I try some sample dates, the numbers are different from those I get when I format the date as a number in Excel (well OpenOffice Calc). For example, testing '2009-03-20' gives 3478032000 in Python, whilst excel renders the serial number as 39892.

What is wrong with the formula above?

\*Note: I am using Python 2.6.3, so do not have access to datetime.total\_seconds()

https://stackoverflow.com/questions/tagged/python

https://stackoverflow.com/questions/tagged/excel

https://stackoverflow.com/questions/tagged/datetime

data-munging

https://stackoverflow.com/questions/tagged/data-munging

https://stackoverflow.com/q/9574793

Short permalink to this question

Improve this question

https://stackoverflow.com/posts/9574793/edit

Follow this question to receive notifications

edited Jan 28, 2019 at 19:42

https://stackoverflow.com/posts/9574793/revisions

https://stackoverflow.com/users/9209546/jpp

166k 37 37 gold badges 303 303 silver badges 365 365 bronze badges

asked Mar 5, 2012 at 22:08

Homunculus Reticulli

https://stackoverflow.com/users/962891/homunculus-reticulli

69.2k 87 87 gold badges 234 234 silver badges 366 366 bronze badges

Add a comment

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

7 Answers 7

Reset to default

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number?answertab=scoredesc#tab-top

Highest score (default)

Trending (recent votes count more)

Date modified (newest first)

Date created (oldest first)

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/9574948/timeline

Show activity on this post.

It appears that the Excel "serial date" format is actually the number of

since 1900-01-00, with a fractional component that's a fraction of a day, based on

http://www.cpearson.com/excel/datetime.htm

http://www.cpearson.com/excel/datetime.htm

. (I guess that date should actually be considered 1899-12-31, since there's no such thing as a 0th day of a month)

#### So, it seems like it should be:

def excel\_date(date1):
    temp = dt.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!
    delta = date1 - temp
    return float(delta.days) + (float(delta.seconds) / 86400)

https://stackoverflow.com/a/9574948

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/9574948/edit

Follow this answer to receive notifications

edited May 8, 2018 at 21:48

https://stackoverflow.com/posts/9574948/revisions

https://stackoverflow.com/users/-1/community

1 1 1 silver badge

answered Mar 5, 2012 at 22:22

https://stackoverflow.com/users/1226284/akgood

1,117 8 8 silver badges 4 4 bronze badges

Sign up to request clarification or add additional context in comments.

Add a comment

Homunculus Reticulli

Homunculus Reticulli

https://stackoverflow.com/users/962891/homunculus-reticulli

Over a year ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#comment12140622\_9574948

+1 for the link. It seems Excel is using the wierd date of 1900-01-00, since dates calculated by the function above is out by one day (according to Excel).

2012-03-05T22:30:52.907Z+00:00

https://stackoverflow.com/users/416467/kindall

Over a year ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#comment12140748\_9574948

joelonsoftware.com/items/2006/06/16.html

http://www.joelonsoftware.com/items/2006/06/16.html

. Basically, it's because Excel wanted to be compatible with Lotus 1-2-3 on dates.

2012-03-05T22:37:58.397Z+00:00

https://stackoverflow.com/users/566942/saroele

Over a year ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#comment12642155\_9574948

I tried your function, but I have to change

temp = dt.datetime(1899, 12, 30)

in order to get correct results.

2012-03-28T13:09:52.57Z+00:00

https://stackoverflow.com/users/3488237/rugby82

Over a year ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#comment48874018\_9574948

change "temp = dt.datetime(1899, 12, 30)" with "temp = datetime.datetime(1899, 12, 31)"

2015-05-22T09:28:39.293Z+00:00

https://stackoverflow.com/users/3011444/cdarlint

Over a year ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#comment49502311\_9574948

a cell of number 60 in excel, press Ctrl+Shift+3 would convert into 1900/02/29, which is not exists in any calendar. This is where the weird one more day comes from.

2015-06-09T03:28:44.477Z+00:00

Add a comment | Show 4 more comments

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/24410858/timeline

Show activity on this post.

While this is not exactly relevant to the excel serial date format, this was the top hit for exporting python date time to Excel. What I have found particularly useful and simple is to just export using strftime.

import datetime
current\_datetime = datetime.datetime.now()
current\_datetime.strftime('%x %X')

This will output in the following format '06/25/14 09:59:29' which is accepted by Excel as a valid date/time and allows for sorting in Excel.

https://stackoverflow.com/a/24410858

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/24410858/edit

Follow this answer to receive notifications

answered Jun 25, 2014 at 14:03

https://stackoverflow.com/users/975915/jazzywhit

411 4 4 silver badges 8 8 bronze badges

Add a comment

https://stackoverflow.com/users/287325/newyuppie

Over a year ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#comment41978162\_24410858

this works perfectly and is more elegant I feel, if you are willing to go to Excel and have the extra step to convert to serial over there

2014-11-01T15:36:43.297Z+00:00

steve-gregory

steve-gregory

https://stackoverflow.com/users/697151/steve-gregory

Over a year ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#comment60272562\_24410858

This is the best answer, hands down. Simple. Pythonic. And easy to remember (%e-x-cel)! :)

2016-03-31T05:38:36.12Z+00:00

Yuya Takashina

Yuya Takashina

https://stackoverflow.com/users/6907832/yuya-takashina

Over a year ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#comment122637622\_24410858

As JazyWhit says, be careful that this won't work when one exactly wants to convert a datetime to excel date number. This is off topic and is not a best answer for this question.

2021-09-30T01:06:42.633Z+00:00

https://stackoverflow.com/users/8182118/masklinn

Over a year ago

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number#comment132863785\_24410858

Except it's wrong because

is a locale-sensitive representation of the date, so whether it works depends on the excel locale and the python locale matching. The selected answer works for all cases but dates in January and February 1900.

2023-01-31T10:06:53.447Z+00:00

Add a comment

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/47478659/timeline

Show activity on this post.

if the problem is that we want DATEVALUE() excel serial number for dates, the toordinal() function can be used. Python serial numbers start from Jan1 of year 1 whereas excel starts from 1 Jan 1900 so apply an offset. Also see excel 1900 leap year bug (

https://support.microsoft.com/en-us/help/214326/excel-incorrectly-assumes-that-the-year-1900-is-a-leap-year

https://support.microsoft.com/en-us/help/214326/excel-incorrectly-assumes-that-the-year-1900-is-a-leap-year

def convert\_date\_to\_excel\_ordinal(day, month, year) :

    offset = 693594
    current = date(year,month,day)
    n = current.toordinal()
    return (n - offset)

https://stackoverflow.com/a/47478659

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/47478659/edit

Follow this answer to receive notifications

answered Nov 24, 2017 at 18:47

https://stackoverflow.com/users/262376/rjha94

4,328 3 3 gold badges 33 33 silver badges 37 37 bronze badges

Add a comment

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/54409168/timeline

Show activity on this post.

With the 3rd party

xlrd.xldate

https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.xldate

module, you can supply a tuple structured as

(year, month, day, hour, minute, second)

and, if necessary, calculate a day fraction from any microseconds component:

from datetime import datetime
from xlrd import xldate
from operator import attrgetter

def excel\_date(input\_date):
    components = ('year', 'month', 'day', 'hour', 'minute', 'second')
    frac = input\_date.microsecond / (86400 \* 10\*\*6)  # divide by microseconds in one day
    return xldate.xldate\_from\_datetime\_tuple(attrgetter(\*components)(input\_date), 0) + frac

res = excel\_date(datetime(1900, 3, 1, 12, 0, 0, 5\*10\*\*5))
# 61.50000578703704

https://stackoverflow.com/a/54409168

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/54409168/edit

Follow this answer to receive notifications

answered Jan 28, 2019 at 19:42

https://stackoverflow.com/users/9209546/jpp

166k 37 37 gold badges 303 303 silver badges 365 365 bronze badges

Add a comment

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/59751081/timeline

Show activity on this post.

According to @akgood's

https://stackoverflow.com/a/9574948/12525445

, when the datetime is before 1/0/1900, the return value is wrong, the corrected return expression may be:

def excel\_date(date1):
    temp = dt.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!
    delta = date1 - temp
    return float(delta.days) + (-1.0 if delta.days < 0 else 1.0)\*(delta.seconds)) / 86400

https://stackoverflow.com/a/59751081

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/59751081/edit

Follow this answer to receive notifications

edited Jan 16, 2020 at 3:03

https://stackoverflow.com/posts/59751081/revisions

answered Jan 15, 2020 at 12:04

https://stackoverflow.com/users/12525445/f-one

23 5 5 bronze badges

Add a comment

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/64976595/timeline

Show activity on this post.

This worked when I tested using the

csv package

https://docs.python.org/3/library/csv.html

to create a spreadsheet:

from datetime import datetime

def excel\_date(date1):
    return date1.strftime('%x %-I:%M:%S %p')

now = datetime.now()
current\_datetime=now.strftime('%x %-I:%M:%S %p')
time\_data.append(excel\_date(datetime.now()))
...

https://stackoverflow.com/a/64976595

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/64976595/edit

Follow this answer to receive notifications

answered Nov 23, 2020 at 21:18

Michael Behrens

https://stackoverflow.com/users/11972755/michael-behrens

1,189 13 13 silver badges 9 9 bronze badges

Add a comment

This answer is useful

This answer is not useful

Save this answer.

Loading when this answer was accepted…

https://stackoverflow.com/posts/79759288/timeline

Show activity on this post.

#### In case anybody needs a pandas solution to this:

import pandas as pd
from datetime import datetime

df = pd.DataFrame(\["2025-05-15", "2025-09-08", ""\], columns=\["date\_column"\])
df\["date\_column"\] = pd.to\_datetime(df\["date\_column"\], format="%Y-%m-%d", errors="coerce")

(df\["date\_column"\] - datetime(1899, 12, 30)).dt.days

>>> 
0    45792.0
1    45908.0
2        NaN
Name: date\_column, dtype: float64

https://stackoverflow.com/a/79759288

Short permalink to this answer

Improve this answer

https://stackoverflow.com/posts/79759288/edit

Follow this answer to receive notifications

answered Sep 8, 2025 at 19:52

Francisco Nicolai Manaut

https://stackoverflow.com/users/10963973/francisco-nicolai-manaut

136 2 2 silver badges 4 4 bronze badges

Add a comment

Your Answer

Thanks for contributing an answer to Stack Overflow!

Please be sure to

answer the question

. Provide details and share your research!

Asking for help, clarification, or responding to other answers.

Making statements based on opinion; back them up with references or personal experience.

To learn more, see our

tips on writing great answers

https://stackoverflow.com/help/how-to-answer

Draft saved

Draft discarded

https://stackoverflow.com/users/login?ssrc=question\_page&returnurl=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F9574793%2Fhow-to-convert-a-python-datetime-datetime-to-excel-serial-date-number%23new-answer

Sign up using Google

Sign up using Email and Password

Post as a guest

Required, but never shown

Post as a guest

Required, but never shown

Post Your Answer Discard

By clicking “Post Your Answer”, you agree to our

terms of service

https://stackoverflow.com/legal/terms-of-service/public

and acknowledge you have read our

privacy policy

https://stackoverflow.com/legal/privacy-policy

Start asking to get answers

Find the answer to your question by asking.

Ask question

https://stackoverflow.com/questions/ask

Explore related questions

https://stackoverflow.com/questions/tagged/python

https://stackoverflow.com/questions/tagged/excel

https://stackoverflow.com/questions/tagged/datetime

data-munging

https://stackoverflow.com/questions/tagged/data-munging

See similar questions with these tags.

The Overflow Blog

Your fridge could be a threat to national security

https://stackoverflow.blog/2026/05/19/your-fridge-could-be-a-threat-to-national-security/

Pack your agentic stack in Slack

https://stackoverflow.blog/2026/05/20/pack-your-agentic-stack-in-slack/

Featured on Meta

(Almost) One year of Challenges

https://meta.stackexchange.com/questions/418261/almost-one-year-of-challenges

Policy: Generative AI (e.g., ChatGPT) is banned

https://meta.stackoverflow.com/questions/421831/policy-generative-ai-e-g-chatgpt-is-banned

https://stackoverflow.com/questions/38454403/convert-excel-style-date-with-pandas

Convert Excel style date with pandas

https://stackoverflow.com/questions/38454403/convert-excel-style-date-with-pandas?noredirect=1

https://stackoverflow.com/questions/29387137/how-to-convert-a-given-ordinal-number-from-excel-to-a-date

How to convert a given ordinal number (from Excel) to a date

https://stackoverflow.com/questions/29387137/how-to-convert-a-given-ordinal-number-from-excel-to-a-date?noredirect=1

https://stackoverflow.com/questions/47325204/python-xlsxwriter-wont-align-dates

python xlsxwriter won't align dates

https://stackoverflow.com/questions/47325204/python-xlsxwriter-wont-align-dates?noredirect=1

https://stackoverflow.com/questions/70536563/convert-pandas-datetime-column-to-excel-serial-date

Convert pandas datetime column to Excel serial date

https://stackoverflow.com/questions/70536563/convert-pandas-datetime-column-to-excel-serial-date?noredirect=1

https://stackoverflow.com/questions/14498816/how-to-convert-from-python-date-to-excel-date-using-xlrd-attribute-xlrd-xldate

How to convert from Python date to Excel date using xlrd (attribute xlrd.xldate\_from\_date\_tuple does not exist)

https://stackoverflow.com/questions/14498816/how-to-convert-from-python-date-to-excel-date-using-xlrd-attribute-xlrd-xldate?noredirect=1

https://stackoverflow.com/questions/59744239/how-to-get-the-excel-datetime-as-a-float-number-rather-than-a-datetime-datetime

How to get the excel datetime as a FLOAT number rather than a 'datetime.datetime' in xlwings?

https://stackoverflow.com/questions/59744239/how-to-get-the-excel-datetime-as-a-float-number-rather-than-a-datetime-datetime?noredirect=1

https://stackoverflow.com/questions/43682977/xlwings-early-dates-1900s

xlwings - early dates (<=1900's)

https://stackoverflow.com/questions/43682977/xlwings-early-dates-1900s?noredirect=1

https://stackoverflow.com/questions/38940665/converting-a-list-of-datetime-objects-to-a-list-of-number-of-days-since-a-certai

Converting a list of datetime objects to a list of number of days since a certain date

https://stackoverflow.com/questions/38940665/converting-a-list-of-datetime-objects-to-a-list-of-number-of-days-since-a-certai?noredirect=1

https://stackoverflow.com/questions/62496075/how-to-convert-dataframe-dates-into-floating-point-numbers

How to convert dataframe dates into floating point numbers?

https://stackoverflow.com/questions/62496075/how-to-convert-dataframe-dates-into-floating-point-numbers?noredirect=1

https://stackoverflow.com/questions/65655568/converting-vba-script-to-python-script

Converting VBA script to Python Script

https://stackoverflow.com/questions/65655568/converting-vba-script-to-python-script?noredirect=1

See more linked questions

https://stackoverflow.com/questions/linked/9574793

https://stackoverflow.com/questions/1108428/how-do-i-read-a-date-in-excel-format-in-python

How do I read a date in Excel format in Python?

https://stackoverflow.com/questions/1108428/how-do-i-read-a-date-in-excel-format-in-python

https://stackoverflow.com/questions/26010455/convert-xldate-to-python-datetime

convert xldate to python datetime

https://stackoverflow.com/questions/26010455/convert-xldate-to-python-datetime

https://stackoverflow.com/questions/28750905/converting-a-datetime-object

converting a datetime object

https://stackoverflow.com/questions/28750905/converting-a-datetime-object

https://stackoverflow.com/questions/45183293/convert-date-string-in-excel-to-date-object-in-python

Convert date string in excel to date object in python

https://stackoverflow.com/questions/45183293/convert-date-string-in-excel-to-date-object-in-python

https://stackoverflow.com/questions/49601597/python-datetime-to-excel-serial-number

python datetime to excel serial number

https://stackoverflow.com/questions/49601597/python-datetime-to-excel-serial-number

https://stackoverflow.com/questions/50472037/using-datetime-in-python-and-how-to-import-from-excel

Using datetime in Python and how to import from Excel

https://stackoverflow.com/questions/50472037/using-datetime-in-python-and-how-to-import-from-excel

https://stackoverflow.com/questions/63963635/how-to-convert-a-column-with-excel-serial-dates-and-regular-dates-to-a-pandas-da

How to convert a column with Excel Serial Dates and regular dates to a pandas datetime?

https://stackoverflow.com/questions/63963635/how-to-convert-a-column-with-excel-serial-dates-and-regular-dates-to-a-pandas-da

https://stackoverflow.com/questions/70536563/convert-pandas-datetime-column-to-excel-serial-date

Convert pandas datetime column to Excel serial date

https://stackoverflow.com/questions/70536563/convert-pandas-datetime-column-to-excel-serial-date

https://stackoverflow.com/questions/71246581/convert-number-in-excel-time-format-to-string-equivalent-in-python

Convert number in Excel time format to string equivalent in python

https://stackoverflow.com/questions/71246581/convert-number-in-excel-time-format-to-string-equivalent-in-python

https://stackoverflow.com/questions/71407196/python-datetime-to-excel-serial-date-conversion

Python datetime to Excel serial date conversion

https://stackoverflow.com/questions/71407196/python-datetime-to-excel-serial-date-conversion

Hot Network Questions

https://stackexchange.com/questions?tab=hot

What is the antecedent of "which" in this sentence from an EFL textbook?

https://ell.stackexchange.com/questions/374888/what-is-the-antecedent-of-which-in-this-sentence-from-an-efl-textbook

English is Evil

https://puzzling.stackexchange.com/questions/138107/english-is-evil

How can I privately insure against bank going bankrupt?

https://money.stackexchange.com/questions/169603/how-can-i-privately-insure-against-bank-going-bankrupt

Understanding the APEM toggle switch lever positions and connections

https://electronics.stackexchange.com/questions/769105/understanding-the-apem-toggle-switch-lever-positions-and-connections

How real are Loki's illusions?

https://scifi.stackexchange.com/questions/304509/how-real-are-loki-s-illusions

Need advice on new foundation tolerances

https://diy.stackexchange.com/questions/330569/need-advice-on-new-foundation-tolerances

Idealization of latches

https://electronics.stackexchange.com/questions/769116/idealization-of-latches

Why should we care what's "real"?

https://philosophy.stackexchange.com/questions/138511/why-should-we-care-whats-real

How can I create a horizontal line from the end of a section's text to the right margin in multicol environment?

https://tex.stackexchange.com/questions/762913/how-can-i-create-a-horizontal-line-from-the-end-of-a-sections-text-to-the-right

In John 10:18, does ἐξουσίαν imply that Christ had the power to resurrect himself, or the legal right to gain resurrection from God?

https://hermeneutics.stackexchange.com/questions/116500/in-john-1018-does-%e1%bc%90%ce%be%ce%bf%cf%85%cf%83%ce%af%ce%b1%ce%bd-imply-that-christ-had-the-power-to-resurrect-himsel

How to adapt apt\_repository in ansible in Ubuntu 26.04

https://askubuntu.com/questions/1566955/how-to-adapt-apt-repository-in-ansible-in-ubuntu-26-04

Are molecular orbitals a linear or a nonlinear combination of atomic orbitals?

https://chemistry.stackexchange.com/questions/195537/are-molecular-orbitals-a-linear-or-a-nonlinear-combination-of-atomic-orbitals

Why does DiracDelta make the difference between RealAbs and Abs?

https://mathematica.stackexchange.com/questions/319440/why-does-diracdelta-make-the-difference-between-realabs-and-abs

What book is this?

https://puzzling.stackexchange.com/questions/138158/what-book-is-this

Canadian off-cycle Phd application

https://academia.stackexchange.com/questions/226750/canadian-off-cycle-phd-application

Sum of powers of polynomial roots

https://codegolf.stackexchange.com/questions/288244/sum-of-powers-of-polynomial-roots

How can I realistically simulate a push-pull SMPS and design a compensator?

https://electronics.stackexchange.com/questions/769037/how-can-i-realistically-simulate-a-push-pull-smps-and-design-a-compensator

Lualatex error when adding accent package with oldStandard math package and unicode-math

https://tex.stackexchange.com/questions/762903/lualatex-error-when-adding-accent-package-with-oldstandard-math-package-and-unic

How can I overlap a uv thats the symmetrical side of another (without mirror modifier or symmetrize)

https://blender.stackexchange.com/questions/346778/how-can-i-overlap-a-uv-thats-the-symmetrical-side-of-another-without-mirror-mod

Former PI gave unexpectedly negative reference after 3 years of positive feedback, how should I handle this with a prospective PhD supervisor?

https://academia.stackexchange.com/questions/226723/former-pi-gave-unexpectedly-negative-reference-after-3-years-of-positive-feedbac

Increase DC-coupled signal by a factor of 2 with common components

https://electronics.stackexchange.com/questions/769060/increase-dc-coupled-signal-by-a-factor-of-2-with-common-components

How easy/safe is it to lower the nut on a classical guitar?

https://music.stackexchange.com/questions/143696/how-easy-safe-is-it-to-lower-the-nut-on-a-classical-guitar

Running external Python script from QGIS action

https://gis.stackexchange.com/questions/500798/running-external-python-script-from-qgis-action

Is there a reason that French uses "how's it going" but Italian and Spanish use "how's it staying"?

https://linguistics.stackexchange.com/questions/51713/is-there-a-reason-that-french-uses-hows-it-going-but-italian-and-spanish-use

more hot questions

https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

Question feed

https://stackoverflow.com/feeds/question/9574793

Subscribe to RSS

Question feed

To subscribe to this RSS feed, copy and paste this URL into your RSS reader.

https://stackoverflow.com/feeds/question/9574793

Hang on, you can't upvote just yet.

You'll need to complete a few actions and gain 15 reputation points before being able to upvote.

indicates when questions and answers are useful.

What's reputation and how do I get it?

https://stackoverflow.com/help/whats-reputation

Instead, you can save this post to reference later.

Save this post for later Not now

https://stackoverflow.com/

Stack Overflow

https://stackoverflow.com/

https://stackoverflow.com/questions

https://stackoverflow.com/help

https://chat.stackoverflow.com/?tab=explore

https://stackoverflow.co/

Stack Internal

https://stackoverflow.co/internal/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=footer&utm\_content=teams

Stack Data Licensing

https://stackoverflow.co/data-licensing/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=footer&utm\_content=data-licensing

https://stackoverflow.co/advertising/?utm\_medium=referral&utm\_source=stackoverflow-community&utm\_campaign=footer&utm\_content=advertising

https://stackoverflow.co/

https://stackoverflow.co/

https://stackoverflow.co/company/press/

https://stackoverflow.co/company/work-here/

https://stackoverflow.com/legal

Privacy Policy

https://stackoverflow.com/legal/privacy-policy

Terms of Service

https://stackoverflow.com/legal/terms-of-service/public

https://stackoverflow.com/contact

Your Privacy Choices

Cookie Policy

https://policies.stackoverflow.co/stack-overflow/cookie-policy

Stack Exchange Network

https://stackexchange.com/

https://stackexchange.com/sites#technology

Culture & recreation

https://stackexchange.com/sites#culturerecreation

Life & arts

https://stackexchange.com/sites#lifearts

https://stackexchange.com/sites#science

Professional

https://stackexchange.com/sites#professional

https://stackexchange.com/sites#business

https://api.stackexchange.com/

https://data.stackexchange.com/

https://stackoverflow.blog?blb=1

https://www.facebook.com/officialstackoverflow/

https://twitter.com/stackoverflow

https://linkedin.com/company/stack-overflow

https://www.instagram.com/thestackoverflow

Site design / logo © 2026 Stack Exchange Inc; user contributions licensed under

https://stackoverflow.com/help/licensing

. rev 2026.5.18.43150

By continuing to use this website, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our

Cookie Policy

https://policies.stackoverflow.co/stack-overflow/cookie-policy/

. By exiting this window, default cookies will be accepted. To reject cookies, select an option from below.

Necessary cookies only

Customize settings

Report this ad


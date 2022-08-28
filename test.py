import datetime
'''d = datetime.date.today()
# delta = datetime.timedelta(10)
# d += delta
# >>>d = d + 10天
love_date = datetime.date(2020,12,9)
delta = datetime.timedelta(days = 365)
annual = love_date + delta

for i in range(1,100):
    annual_day = annual + (delta*i)
    print(annual_day)

print(annual)
'''

love_datte = datetime.date(2020,12,9)
d_todayy = datetime.date.today()

for i in range(2,5):
    d_year = 2020
    d_year += i
    annual_dayy = datetime.date(d_year, 12, 9)
    if d_todayy.year == annual_dayy.year:
        # print('today is:',d_todayy)
        # print(annual_dayy)
        annual_day = (annual_dayy - d_todayy).days
        annual_year = i
        # print('距离',annual_year,'周年纪念还有',annual_day,'天')
        break
'''
love_date = datetime.date(2020,12,9)
d_today = datetime.date(2032,12,10)

for i in range(2,100):
    d_year = 2020
    d_year += i
    annual_day = datetime.date(d_year, 12, 9)
    if d_today.year == annual_day.year:
        print('today is:',d_today)
        print(annual_day)
        print('今年是',i,'周年纪念')
        break
'''
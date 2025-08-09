import datetime
import sys
from datetime import date, timedelta


def get_last_day_of_month(year, month):
    if month == 12:
        next_month_first = datetime.datetime(year + 1, 1, 1)
    else:
        next_month_first = datetime.datetime(year, month + 1, 1)
    
    return (next_month_first - timedelta(days=1)).day


def display_calendar(year, month):
    
    print(f"     {month}月 {year}")
    weekday_names = ['月', '火', '水', '木', '金', '土', '日']
    print(' '.join(weekday_names))

    first_date = date(year, month, 1)
    first_weekday = first_date.weekday()
    for _ in range(first_weekday):
        print("   ", end='')

    last_day = get_last_day_of_month(year, month)
    
    for day in range(1, last_day + 1):
        print(f"{day:2d} ", end='')
        
        if (first_weekday + day - 1) % 7 == 6:
            print()
    
    if (first_weekday + last_day - 1) % 7 != 6:
        print()


year = datetime.datetime.now().year
month = datetime.datetime.now().month


if len(sys.argv) == 1:
    pass
    
elif len(sys.argv) == 3 and sys.argv[1] == "-m":
    try:
        month = int(sys.argv[2])
        
        if month < 1 or month > 12:
            print(f"{month} is neither a month number (1..12) nor a name")
            sys.exit(1)
            
    except ValueError:
        print(f"{sys.argv[2]} is neither a month number (1..12) nor a name")
        sys.exit(1)


display_calendar(year, month)



from datetime import datetime, timedelta

date1 = input("Send date 1 (YYYY-MM-DD): ")
date_1 = datetime.strptime(date1,"%Y-%m-%d")

date2 = input("Send date 2 (YYYY-MM-DD): ")
date_2 = datetime.strptime(date2,"%Y-%m-%d")

second = date_2 - date_1
print(second.total_seconds())



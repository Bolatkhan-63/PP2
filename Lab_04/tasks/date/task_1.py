from datetime import datetime, timedelta

current_time = datetime.today()

new_date = current_time - timedelta(days=5)

print("Today: ",current_time.strftime("%x"))
print("Before 5 day: ",new_date.strftime("%x"))
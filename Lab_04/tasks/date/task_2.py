from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday: ",yesterday.strftime("%x"),"\n","Today: ",today.strftime("%x"),"\n", "Tomorrow: ",tomorrow.strftime("%x"))
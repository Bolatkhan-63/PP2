import time

start_time = time.time()
time.sleep(90)
elapsed_time = time.time() - start_time

print(elapsed_time)

seconds = int(elapsed_time % 60)
minutes = int((elapsed_time // 60) % 60)

print(seconds)
print(minutes)
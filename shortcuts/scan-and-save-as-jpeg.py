# this will scan a page from the scanner with simple-scan (document scanner)
# and save it as %H-%M-%S.jpg file
# Hotkey: bind this to an empty Function key (for example F2)
# Window Filter: simple-scan.Simple-scan

# we need time for sleep
import time
# first we get current time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H-%M-%S")
# new document - so previous scanned pages get removed
keyboard.send_keys("<ctrl>+n")
# scan page
keyboard.send_keys("<ctrl>+1")
# wait till scan is finished
time.sleep(10)
# save scan
keyboard.send_keys("<ctrl>+s")
# select the whole filename
keyboard.send_keys("<ctrl>+a")
# enter filename using time with extension jpg
keyboard.send_keys("%s.jpg" %current_time)
# hit save button
keyboard.send_key('<enter>')

import threading

e = threading.Event()
e.set()
e.clear()

e.wait()
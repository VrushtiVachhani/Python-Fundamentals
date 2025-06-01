import threading
import time

# Function that will run in multiple threads
def print_numbers():
    for i in range(5):
        print(f"Thread {threading.current_thread().name}: {i}")
        time.sleep(1)  # Simulate work

# Creating threads
thread1 = threading.Thread(target=print_numbers, name="T1")
thread2 = threading.Thread(target=print_numbers, name="T2")

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print("Multithreading Done!")



# Two threads (T1 and T2) run concurrently and print numbers.
# Threads share the same memory space and run interleaved, not truly parallel due to GIL.
# time.sleep(1) simulates a delay, allowing us to see concurrency in action.
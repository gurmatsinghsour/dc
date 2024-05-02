import threading
import time

# Function for each thread to execute
def communicate(id, message, lock):
    with lock:
        print(f"Thread {id} sends message: {message}")
        time.sleep(2)  # Simulate some work being done
        print(f"Thread {id} received message: {message}\n")

# Create a list of messages to communicate
messages = ["Hello", "Bonjour", "Hola", "Ciao", "Namaste"]

# Create a lock
lock = threading.Lock()

# Create threads for each message
threads = []
for idx, msg in enumerate(messages):
    thread = threading.Thread(target=communicate, args=(idx, msg, lock))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All communication complete!")


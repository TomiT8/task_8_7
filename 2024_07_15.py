# todo
#   Viacvláknové programovanie (Multithreading)

"""
import threading

def iterate_print(iter):
    for item in iter:
        print(item)

if __name__ == "__main__":
    # creating threads
    t1 = threading.Thread(target=iterate_print, args=(range(5),))
    t2 = threading.Thread(target=iterate_print, args=("Python",))

    # starting threads
    t1.start()
    t2.start()

    # waiting until both threads have finished executing before executing further code
    t1.join()
    t2.join()

    print("Done!")
"""

# todo
#   task 1
#   # Napis program, ktory vytvori 10 threadov a spusti ich.
#   Funkcia priradena threadu bude vypisovat aktualny nazov threadu cez
#   threading.current_thread().name

import threading

def thread_function():
    print(f"Aktuálny názov threadu: Thread - {threading.current_thread().name}.")

if __name__ == "__main__":
    threads = [threading.Thread(target=thread_function, name=f"{x}") for x in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
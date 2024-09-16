import threading


list_num = [2, 4, 5, -9, 1, 15, 9, 0, 3, 1]
max_num = max(list_num)
min_num = min(list_num)


def writer(x, event_for_wait, event_for_set):
    for i in range(5):
        event_for_wait.wait()
        event_for_wait.clear()
        print(x, end=" / ")
        event_for_set.set()


event_1 = threading.Event()
event_2 = threading.Event()

thread_1 = threading.Thread(target=writer, args=(max_num, event_1, event_2))
thread_2 = threading.Thread(target=writer, args=(min_num, event_2, event_1))

thread_1.start()
thread_2.start()

event_1.set()

thread_1.join()
thread_2.join()

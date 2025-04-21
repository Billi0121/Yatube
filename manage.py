import time

def sleep_one_sec():
    print('Перерыв 1 секунда')
    time.sleep(2)
    return 'Возвращаемое значение'
        

def sleep_two_sec():
    time.sleep(2)

def time_of_function(func):
    def wrapper():
        start_time = time.time()
        result = func()
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции: {execution_time} с.')
        return result
    return wrapper



# measured_sleep_one_sec = time_of_function(sleep_one_sec)
# print(measured_sleep_one_sec())

# measured_sleep_two_sec = time_of_function(sleep_two_sec)
# measured_sleep_two_sec()
sleep_on_sec()
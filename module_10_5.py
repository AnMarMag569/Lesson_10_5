import time
from multiprocessing import Pool

def read_info(filename):

    all_data = []
    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line.strip())
            line = file.readline()

filenames = [f"file {i}.txt" for i in range(1,5)]

if __name__ == "__main__":

    start_time = time.time()
    for filename in filenames:
        read_info(filename)
        end_time = time.time()
        print(f"Линейное выполнение: {end_time - start_time} секунд")

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессное выполнение: {end_time - start_time} секунд")
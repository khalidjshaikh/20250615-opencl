#!/usr/bin/env python3
# python count to 1 billion 8 threads

# 666 million operations per second

import multiprocessing

def count_range(start, end):
    count = 0
    for i in range(start, end):
        count += 1
    return count

if __name__ == '__main__':
    total_count = int(5e9) 
    # 12 seconds for 8 billion ( 1e9 * 8 ). 
    # 55 seconds for 40 billion ( 5e9 * 8 ).

    # 30 seconds for 1 trillion on GPU OpenCL 8-bit
    # 50 seconds for 1 trillion on GPU OpenCL 32-bit
    num_processes = 8
    chunk_size = total_count // num_processes

    processes = []
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else total_count
        process = multiprocessing.Process(target=count_range, args=(start, end))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Counted to {total_count} using {num_processes} processes.")
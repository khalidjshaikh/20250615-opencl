#!/usr/bin/env python3
# run a counter in opencl example python

import pyopencl as cl
import numpy as np

# OpenCL kernel code (string)
kernel_code = """
__kernel void counter_kernel(__global unsigned int* counter) {
    // Atomically increment the counter
    atomic_inc(counter);
}
"""

# 1. Initialize PyOpenCL
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

# 2. Build the OpenCL program from the source code
program = cl.Program(context, kernel_code).build()

# 3. Create a buffer in device memory to hold the counter
counter_buf = cl.Buffer(context, cl.mem_flags.READ_WRITE, size=np.uint32().itemsize)

# 4. Initialize the counter buffer on the device to 0
cl.enqueue_fill_buffer(queue, counter_buf, np.uint32(0), offset=0, size=np.uint32().itemsize)

# 5. Get the kernel object from the program
counter_kernel = program.counter_kernel

# 6. Execute the kernel
# The kernel is launched with a certain number of work-items
# Each work-item will execute the kernel code and increment the counter


for i in range(0, 100):
    cl.enqueue_fill_buffer(queue, counter_buf, np.uint32(0), offset=0, size=np.uint32().itemsize)

    num_work_items = int(2e9)
    counter_kernel(queue, (num_work_items,), None, counter_buf)

    # 7. Read the counter value back from the device to the host
    counter_value = np.empty(1, dtype=np.uint32)
    # print(counter_value)
    cl.enqueue_copy(queue, counter_value, counter_buf).wait() # Wait for the copy to complete
    # print(counter_buf)

    # 8. Print the result
    print("Final counter value:", counter_value[0])

# 9. Release OpenCL resources (optional, but good practice)
# counter_buf.release()
# program.release()
# queue.release()
# context.release()

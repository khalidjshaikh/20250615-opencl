#!/usr/bin/env python3
# opencl counter unsigned int 64 example python

# 20 billion per second at 32 bit

import pyopencl as cl
import numpy as np

# Create a context and command queue
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

# Define the counter buffer (64-bit unsigned integer)
counter_np = np.zeros(1, dtype=np.uint64) 
counter_g = cl.Buffer(ctx, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=counter_np)

# OpenCL kernel code (replace with your kernel from step 1)
prg = cl.Program(ctx, """
__kernel void counter_kernel(__global unsigned int * counter) {
    atomic_inc(counter); 
}
""").build()

kernel = prg.counter_kernel 

# # Enqueue the kernel
# cl.enqueue_nd_range_kernel(queue, kernel, (100,), None, counter_g) 
# cl.enqueue_nd_range_kernel(queue, kernel, counter_np.shape, None)

for i in range(0, int(1e3)):
    kernel(queue, (int(1e9),), None, counter_g)
    # Read the counter value back
    cl.enqueue_copy(queue, counter_np, counter_g).wait() # Wait for the copy to complete

print(f"Counter value: {counter_np[0]}")

# 100e9 % 2**32 = 1215752192
# Counter value: 1215752192

# 1000e9 % 2**32 = 3567587328
# Counter value: 3567587328

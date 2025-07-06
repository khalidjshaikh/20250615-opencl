#!/usr/bin/env python3
# simplest opencl program example python two cores

import pyopencl as cl
import numpy as np

# 1. Data Preparation
a = np.array([1, 2, 3, 4], dtype=np.int32)
b = np.array([5, 6, 7, 8], dtype=np.int32)
result = np.zeros_like(a)

# 2. OpenCL Setup
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)
mf = cl.mem_flags

# 3. Memory Buffers
a_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
b_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
result_buf = cl.Buffer(ctx, mf.WRITE_ONLY, result.nbytes)

# 4. Kernel Code (as a string)
kernel_code = """
__kernel void add_arrays(__global const int *a, __global const int *b, __global int *result) {
    int gid = get_global_id(0);
    result[gid] = a[gid] + b[gid];
}
"""

# 5. Compile and Build Kernel
program = cl.Program(ctx, kernel_code).build()

# 6. Execute Kernel
global_size = a.shape
program.add_arrays(queue, global_size, None, a_buf, b_buf, result_buf)

# 7. Read Results Back
cl.enqueue_copy(queue, result, result_buf)

# 8. Print Results
print("Input A:", a)
print("Input B:", b)
print("Result:", result)
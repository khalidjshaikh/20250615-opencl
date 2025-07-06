#!/usr/bin/env python3
# simplest opencl program example python

import pyopencl as cl
import numpy as np

# 1. Create a context
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

# 2. Define the OpenCL kernel as a string
kernel_code = """
__kernel void square_array(__global const float *input, __global float *output) {
    int i = get_global_id(0);
    output[i] = input[i] * input[i];
}
"""

# 3. Create program from the kernel code
program = cl.Program(ctx, kernel_code).build()

# 4. Create input and output arrays
size = 10
input_array = np.arange(size, dtype=np.float32)
output_array = np.empty_like(input_array)

# 5. Create buffers
mf = cl.mem_flags
input_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=input_array)
output_buf = cl.Buffer(ctx, mf.WRITE_ONLY, output_array.nbytes)

# 6. Execute the kernel
kernel = program.square_array
kernel.set_arg(0, input_buf)
kernel.set_arg(1, output_buf)

cl.enqueue_nd_range_kernel(queue, kernel, input_array.shape, None)

# 7. Read the results
cl.enqueue_copy(queue, output_array, output_buf)

# Print results
print("Input array:", input_array)
print("Output array:", output_array)
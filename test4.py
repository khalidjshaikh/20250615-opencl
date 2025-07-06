#!/usr/bin/env python3
# opencl print a buffer example python

import pyopencl as cl
import numpy as np

# 1. Setup OpenCL context and queue
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

# 2. Create a sample numpy array
data = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# 3. Create an OpenCL buffer from the numpy array
mf = cl.mem_flags
buffer = cl.Buffer(ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=data)

# 4. Create another numpy array to store the result
result = np.empty_like(data)
print(result)

# 5. Copy data from the OpenCL buffer to the result array
cl.enqueue_copy(queue, result, buffer).wait()

# 6. Print the result array
print("Data from OpenCL buffer:", result)
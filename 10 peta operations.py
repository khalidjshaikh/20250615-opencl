#!/usr/bin/env python3
# simplest opencl program example python

# $env:PYOPENCL_CTX='0'

# 10 peta operation per second
# no memory access, internal kernel variable gid

# Processor	13th Gen Intel(R) Core(TM) i3-1315U, 1200 Mhz, 6 Core(s), 8 Logical Processor(s)
# https://www.intel.com/content/www/us/en/products/sku/233459/intel-core-i31315u-processor-10m-cache-up-to-4-50-ghz-with-ipu/specifications.html
# GPU 1.25GHz
# EUs 64

import pyopencl as cl
import numpy as np
from numpy import *

# 1. Data Preparation
# a = np.arange(0, 5, dtype=np.int32)
a = np.arange(0,1e8, dtype=np.int32)
# a = ones(int(1e2))
b = np.array([5, 6, 7, 8], dtype=np.int32)
result = np.zeros_like(a)

# 2. OpenCL Setup
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
ctx = context = cl.Context([device])
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
    //result[gid] = a[gid] + b[gid];
    //result[gid] = gid;
    
    short i;  // 16-bit
    short j;
    short k;
    for(i=0; i<(short)(1e4); i++)
      for(j=0; j<(short)(1e4); j++);
    //    for(k=0; k<1; k++);
    
    // int i;  // 32-bit
    // for(i=0; i<1e4; i++);

    //long i; // 64-bit
    //for(i=0; i<1e9; i++);
      
    //result[gid] = a[gid]; // assign memory
    result[gid] = gid + i; 
    //result[gid] = gid + i*j;
}
"""

# 5. Compile and Build Kernel
program = cl.Program(ctx, kernel_code).build()

# 6. Execute Kernel
global_size = a.shape

# Loop 1 peta op on GPU
for i in range(int(1e1)): # 1e0 1e1 1e2
  program.add_arrays(queue, global_size, None, a_buf, b_buf, result_buf)
  # 7. Read Results Back
  cl.enqueue_copy(queue, result, result_buf)


# 8. Print Results
print("Input A:", a)
print("Input B:", b)
print("Result:", result)
print(a.shape, b.shape, result.shape)
print(f"{a.shape[0]:e}")
print(f"{result.shape[0]:e}")

macOS 15.5 M1

export PYOPENCL_CTX=''

python3 py\ version.py 
Python version:
3.13.5 (main, Jun 11 2025, 15:36:57) [Clang 17.0.0 (clang-1700.0.13.3)]
Version info:
sys.version_info(major=3, minor=13, micro=5, releaselevel='final', serial=0)

python3 pyopencl\ version.py # if broken remove pyenv use system macos python
PyOpenCL version: 2025.2.4

python3 square\ 10\ numbers.py 
Choosing only available device: <pyopencl.Device 'Apple M1' on 'Apple' at 0x1027f00>
Input array: [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
Output array: [ 0.  1.  4.  9. 16. 25. 36. 49. 64. 81.]

python3 opencl\ buffer\ 1d.py 
Choosing only available device: <pyopencl.Device 'Apple M1' on 'Apple' at 0x1027f00>
[0 0 0 0 0]
Data from OpenCL buffer: [1 2 3 4 5]

python3 add\ arrays\ 1d.py 
Choosing only available device: <pyopencl.Device 'Apple M1' on 'Apple' at 0x1027f00>
Input A: [1 2 3 4]
Input B: [5 6 7 8]
Result: [ 6  8 10 12]

time python3 count\ to\ 1\ trillion.py 
Choosing only available device: <pyopencl.Device 'Apple M1' on 'Apple' at 0x1027f00>
Counter value: 1

real	0m27.182s
user	0m0.494s
sys	0m0.408s

node
Welcome to Node.js v24.3.0.
Type ".help" for more information.
> 1e12/27 * 1e-9
37.037037037037045


---

python3 Chess.py 
g1h3
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R

---

capitalization is intentionally incorrect

scalar - single number
vector - 1d - list - array 
buffer - scalar 1d 2d 3d 4d ...

scalar - data type
  uint8
  uint16
  uint32
  uint64
  int8
  int16
  int32
  int64
  fp8
  fp16
  fp32
  fp64

8  - 1 byte   - 8 bits 
16 - 2 bytes  - 16 bits
32 - 4 bytes  - 32 bits 
64 - 8 bytes  - 64 bits

bit - either 0 or 1

metrics prefixes
https://en.wikipedia.org/wiki/Metric_prefix

kilo 10^3
mega 10^6
giga 10^9
tera 10^12
peta 10^15

milli 10^-3
micro 10^-6
nano  10^-9
pico  10^-12
femto 10^-15

byte KB MB GB
KB/s MB/s GB/s
kbps Mbps Gbps

6G 1Tbps
AI5 2 peta ops
RTX 5090 3.352 peta flops (fp4)

---

1GHz 1 billion 1e9

64 EUs

1 peta  = 100 million * 10 million
10 peta = 100 million * 100 million
1 exa is 100 (on CPU) * 10 peta

100 million 1e8 memory UINT32 (400MB) global size
100 million 1e8 loop - 45 operations + 9 (in systolic array but not scalar GPU with data type)

systolic array
54 operations
  45 operations
    27 multiplications (9 * 3)
    18 additions (9 * 2)
  9 operations
    9 additions

1 clock cycle
memory look up table - both take space
transistor based functional logic - both take space

DRAM bit is stored using one transistor and one capacitor
A 32-bit adder, built using ripple-carry architecture, requires 896 transistors

LOAD/STORE or MOV - memory
ALU - multiply or add - functional logic

1.25GHz5

10 peta with GPU with memory access
4.5GHz * 8 cores billion per second if CPU

scalar
1D array
2D matrix AI software
3D n^3
    i=0; i<n; i++
      j=0; j<n; j++
        k=0; k<n; k++

NPU TPU
AI accelerator
inference processor

AI
machine learning
neural networks
computer vision
robotics
algorithms

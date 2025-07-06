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
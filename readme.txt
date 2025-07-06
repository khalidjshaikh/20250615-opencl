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

scalar - single number
vector - 1d - list - array
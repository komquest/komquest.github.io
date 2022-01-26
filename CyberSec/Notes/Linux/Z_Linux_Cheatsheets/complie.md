## Complie Simple c and c++ files for Windows on Linux! (Windows on Linux)

https://arrayfire.com/cross-compile-to-windows-from-linux/

```
sudo apt-get install mingw-w64
 
# C
i686-w64-mingw32-gcc hello.c -o hello32.exe      # 32-bit
x86_64-w64-mingw32-gcc hello.c -o hello64.exe    # 64-bit
 
# C++
i686-w64-mingw32-g++ hello.cc -o hello32.exe     # 32-bit
x86_64-w64-mingw32-g++ hello.cc -o hello64.exe   # 64-bit
```


## Another way to compile c files! (Linux on Linux)

## Make sure you install the correct libs!:
https://www.geeksforgeeks.org/compile-32-bit-program-64-bit-gcc-c-c/

```
gcc -m32 -o output32 hello.c (32 bit)
gcc -m64 -o output hello.c (64 bit)
```
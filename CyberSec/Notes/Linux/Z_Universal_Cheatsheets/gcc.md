## Compile a simple c program

```
gcc ex.c -o ex
```

## Compile a simple c program statically:

```
gcc -static ex.c -o ex
```

## Compile 32 bit program on 64 bit machine:

```
gcc -m32 ex.c -o ex
```

## mtune, don't know if this works correclty

```
gcc  -static -m32 -mtune=i686 21420.c -o cc
```

## Getting crazy with some pthreads!!!

```
gcc 40616.c -m32 -static -pthread -o dc3
```

## Compiling tips if you have libs in strange places

https://homepages.inf.ed.ac.uk/imurray2/compnotes/library_linking.txt
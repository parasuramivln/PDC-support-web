ltrace intercepts and records dynamic library calls which are called by an executed process and the signals received by that process. It can also intercept and print the system calls executed by the program.
ltrace was originally authored by Juan Cespedes.

## How to use

ltrace is a debugging utility in Linux, used to display the calls a
userspace application makes to shared libraries. It does this by
hooking into the dynamic loading system, allowing it to insert shims
which display the parameters which the applications uses when making
the call, and the return value which the library call reports. ltrace
can also trace Linux system calls. Because it uses the dynamic library
hooking mechanism, ltrace cannot trace calls to libraries which are
statically linked directly to the target binary. Since 0.7.3, ltrace
can also trace calls to libraries which are loaded using dlopen().

# To use ltrace on Tegner, type

```
module load ltrace

```

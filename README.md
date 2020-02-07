# MVA Topological Data Analysis

Topological data analysis (TDA) is the use of topology to analyze (potentially high-dimensional) datasets in a way that exploits topological features and invariants.


![](images/distmat_pers_alpha_dim1.png)

![](images/persistence_landscape_MC.png)

## Gudhi install

It can be easily installed when using Anaconda by
```bash
conda install -c conda-forge gudhi
```
This will also make the Gudhi headers and libraries available on your system at `$CONDA_PREFIX/{include,lib}` for writing custom C++ modules.


## TTK/Paraview installation on a system with Anaconda

At time of writing my machine runs the latest Ubuntu 19.10 (eoan) with several Python environments managed by conda and the base conda environment active at all times.

### Conda-managed dependencies

The installation instructions on the TTK website have the user install dependencies through `apt`, including Python packages and or other packages that depend on Python.
If you manage Python and other dependencies through Anaconda that might not be desirable. For example, on my system, conda manages:
* Python
* Eigen
* Boost
* QT5
* Graphviz

which I do *not* want to reinstall through `apt` because that would also reinstall a ton of deps I already have under Anaconda. It also creates confusion for the C/C++ linker (for instance link against something in `/usr/lib` while runtime looks at `/path/to/conda/lib`).

TTK and Paraview use CMake to look for the dependencies on your system and generate a build. By default it will look at system paths first, so you need to set it to look through your Anaconda paths first. The easiest way to do that is to set the CMAKE_PREFIX_PATH environment variable before invoking CMake:
```bash
export CMAKE_PREFIX_PATH=$CONDA_PREFIX
cmake-gui ../ # or cmake ../
```

Then you can check where CMake finds the headers and libraries to see if everything is consistent.


The tutorial says to update the CMake flags `CMAKE_C_FLAGS=-luuid` and `CMAKE_CXX_FLAGS=-luuid` on Linux Mint (>19). That is also the case on Ubuntu 19+.

**Remark** Some libraries such as `zfp` can be installed through conda:
```bash
conda install -c conda-forge zfpy
```
so you don't need to compile it yourself.

The Paraview install still needs to be patched with TTK though so  installing it through conda won't suffice!


For the TTK installation, the NumPy headers might be found at `/usr/include`, which is a mistake due to how CMake's `find_path` function works, so be sure to change them to the headers in your conda env!


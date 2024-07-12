# Evaluation and Comparison of Boosted ML Models in Behavior-Based Malware Detection
**Choa, de Veyra, Escalona, Fortiz**

This is a repository for the Thesis **"Evaluation and Comparison of Boosted ML Models in Behavior-Based Malware Detection"**.

It contains the Jupyter notebook files and datasets used for the development of the study.

## Tested on:
1. Windows (Recommended)
2. Linux (Debian-based)

## Pre-requisite Software:
1. [Python 3.11.x](https://www.python.org/downloads/release/python-3115/)
2. [Anaconda/Conda](https://www.anaconda.com/download)

Kindly install these before proceeding to the next step.

## Dependency/Library Installation:
1. Once the two software is installed open `Anaconda Prompt`**as administrator** in your computer and navigate to the local copy of the repository in your computer.
2. Once navigated, type `install.bat` for Windows or `install.sh` for Linux. The script will begin the installation of the necessary libraries for your Conda environment.
3. Once completed, you can now begin exploring the thesis project files.

## How to run:
1. Open `Anaconda Prompt`
2. Navigate to the location of the GitHub repository on your computer.
3. Type `jupyter notebook`
4. To terminate `jupyter`, simply `Ctrl+C` on the Anaconda Prompt.

## Tips for running on Linux:
1. Install Anaconda as shown [here](https://docs.anaconda.com/free/anaconda/install/linux/).
2. Once completed, run Anaconda Terminal (assuming `conda config --set auto_activate_base False`
) by typing `soure <PATH_TO_ANACONDA>/bin/activate`

## CUDA Toolkit
Make sure you have installed the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) in your machine to ensure that GPU (CUDA-specific) is supported. Do note that this may replace (downgrade) your GPU driver.

## LightGBM GPU Support
- Download the latest [GCC](https://winlibs.com/#download-release)
- Download the latest [CMake](https://cmake.org/download/)
- Download the [Boost v1.56.0 ](https://sourceforge.net/projects/boost/files/boost/1.56.0/)
- Follow the [guide](https://lightgbm.readthedocs.io/en/latest/GPU-Windows.html)
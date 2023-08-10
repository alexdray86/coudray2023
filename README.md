Code necessary to reproduce figures of the manuscript

## Deconvolution of ex-vivo drug screening data and bulk tissue expression predicts the abundance and viability of cancer cell subpopulations

## Setup 

Here can be found the code to reproduce figures from the manuscript. In the present README, we will explain the main steps to be able to run the codes. First of all, all notebook are in R language (requires R\>v4.0), and were ran with the IRkernel for jupyter notebook. Libraries needed to run each notebook are present in the first cell of each notebook, and should be installed before running the notebook. \\

### Python environment necessary for running TAPE and Scaden deconvolution methods
In case the user wants to run the panel of deconvolution method to predict cell type abundance, which includes Scaden and TAPE, a python environnment will need to be set up. The R notebook will run a bash script, which will load the python environment with required libraries, and then launch the python script with TAPE and Scaden methods. To



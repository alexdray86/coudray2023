Code necessary to reproduce figures of the manuscript

## Deconvolution of ex-vivo drug screening data and bulk tissue expression predicts the abundance and viability of cancer cell subpopulations

## Setup 

Here can be found the code to reproduce figures from the manuscript. In the present README, we will explain the main steps to be able to run the code. First of all, all notebook are in R language (requires R\>v4.0), and were ran with the IRkernel for jupyter notebook. Libraries needed to run each notebook are listed in the first cell of each notebook, and should be installed before running the notebook. Libraries can be installed directly inside the notebooks, and we provide an extra cell with installation commands.\\

## Data: IMPORTANT 

All the data required are stored in a Google Drive, publicly available with the following link: 

https://drive.google.com/drive/folders/1ev2uiHhoID1nWbutPxPRFkgJUCWLBVYQ?usp=sharing

The file data.zip can be unziped and the folder data/ should be placed at the root of this folder. 

The data/ folder contains all the raw data of single-cell datasets, but also pre-processed data (e.g. deconovution results), allowing to perform the analysis without necessarily re-running all deconvolution methods. 

## Python environment necessary for running TAPE and Scaden deconvolution methods
In case the user wants to run the panel of deconvolution method to predict cell type abundance, which includes Scaden and TAPE, a python environnment will need to be set up. The file requirements_tape_scaden.txt allows to install and the dependencies in a python environment easily with the following commands: 

First, create a new python environment with:\\
`python3 -m venv tape\_scaden\_env`

Load the python environment:\\
`source tape\_scaden\_env/bin/activate`

Then, install all the libraries listed in file requirements_tape_scaden.txt:\\
`python3 -m pip install -r requirements_tape_scaden.txt`

This is how we implemented it: the R notebook will run a bash script, which will, first, i) load the python environment with required libraries, and then, ii) launch the python script with TAPE and Scaden methods. The python script then write all results in a CSV file that is read by the R script. This way, TAPE and Scaden deconvolution can be run directly from the R notebook and the results directly loaded.

LAST IMPORTANT POINT: Tape / Scaden method produces figures during the run, that makes the script to stop until the figure popping up are closed by the user. This can be avoid by commenting the source code at the following locations:

XXX

## Description of the different Notebooks

We provide notebooks for each Figures, named after figure numbers. Hereafter, we summarize the content of each notebook so that users can go and check the code of specific parts of the manuscript:

### Fig2_deconvolution_invitro.ipynb



### Fig3_aml_3cohorts.ipynb

### Fig3_analysis.ipynb

### Fig3_deconvolution_panel.ipynb

### Fig3_preproc.ipynb

### Fig3_simulation.ipynb

### Fig4_expression_deconvolution.ipynb

### Fig5_CLIFF_highres_invitro.ipynb

### Fig6_CLIFF_highres_beataml.ipynb

### Fig6_CLIFF_highres_simulation.ipynb

### Fig7_CLIFF-SC.ipynb


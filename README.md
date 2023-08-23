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

First, create a new python environment with:

`python3 -m venv tape_scaden_env`

Load the python environment:

`source tape_scaden_env/bin/activate`

Then, install all the libraries listed in file requirements_tape_scaden.txt:

`python3 -m pip install -r requirements_tape_scaden.txt`

This is how we implemented it: the R notebook will run a bash script, which will, first, i) load the python environment with required libraries, and then, ii) launch the python script with TAPE and Scaden methods. The python script then write all results in a CSV file that is read by the R script. This way, TAPE and Scaden deconvolution can be run directly from the R notebook and the results directly loaded.

LAST IMPORTANT POINT: Tape / Scaden method produces figures during the run, that makes the script to stop until the figure popping up are closed by the user. This can be avoid by commenting the source code at the following locations:

XXX

## Description of the different Notebooks

We provide notebooks for each Figures, named after figure numbers. Hereafter, we summarize the content of each notebook so that users can go and check the code of specific parts of the manuscript:

### Fig2_invitro_experiment.ipynb

Figures related to the in-vitro experiment developed in our research group. Cell line mixed were produced after cell counting and recording of cell line fraction, and sequenced immediatly after with standard bulk RNA sequencing. In this notebook we use a panel of deconvolution methods to deconovlute cell line fractions using a single-cell RNA-seq reference made from a mix of the same four cell lines. 

### Fig3_1_preproc_integration.ipynb

In this notebook we present the integration pipeline for pairs of single-cell datasets. We first subset cells and genes, and then use Seurat integration pipeline to integrate two datasets. Utlimately, cell subtype labels are transfered from one dataset to the other. We then generate pseudo-bulks with ground truth cell subtype proportions, and save the resulting datasets into RDS objects to be used in `Fig3_2_deconvolution_panel.ipynb` notebook for deconvolution of cell subtype proportions. 

### Fig3_2_deconvolution_panel.ipynb

Uses processed dataset from `Fig3_1_preproc_integration.ipynb` notebook to launch our panel of deconvolution methods in a cross-dataset context. the results are then saved and analysed in next notebook, `Fig3_3_analysis.ipynb`. 

### Fig3_3_analysis.ipynb

Results from deconvolution are compared with ground truth cell subtype proportions based on four metrics. Boxplots and ranking plots are generated for each of the 12 analysis we performed.

### Fig3_4_amlCohorts.ipynb

Here we run CLIMB deconvolution on 3 cohorts of AML patients, and show the results as a heatmap. Further comparison between CLIMB deconvolution output and van galen signature scores, and LSC17 signature, is performed. 

### Fig4_expression_deconvolution.ipynb

In this notebook we perform deconvolution of cell subtype expression based on the in-vitro experiment (where our ground truth comes from bulk RNA-seq), and in a simulated context (based on Van Galen > Naldini cross-dataset deconvolution, for which we have ground truth cell subtype expression). Then, we performed an over-expression of 20 genes in HSC-like cell subtype, based on Van Galen > Naldini analysis, thus inducing over-expression in pseudo-bulk made from Naldini samples.
 
### Fig5_CLIFF_highres_invitro.ipynb
### Fig6_CLIFF_highres_beataml.ipynb
### Fig6_CLIFF_highres_simulation.ipynb
### Fig7_CLIFF-SC.ipynb


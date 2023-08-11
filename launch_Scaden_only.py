import numpy as np
import pandas as pd
import sys
from TAPE import Deconvolution
from TAPE.deconvolution import ScadenDeconvolution

sc_mat_file = sys.argv[1]
pbulk_file = sys.argv[2]
gene_len_file = sys.argv[3]
out_dir = sys.argv[4]

# Load scRNA-seq reference data 
print('load scrna-seq reference data')
sc_ref = pd.read_csv(sc_mat_file, index_col=0)

# Launch Scaden 
print('launch Scaden deconvolution')
sc_ref = pd.read_csv(sc_mat_file, index_col=0)
scaden_out = out_dir + '/scaden_prop.csv'
Pred = ScadenDeconvolution(sc_ref, pbulk_file, sep=',', batch_size=128, epochs=128)
Pred.to_csv(scaden_out)

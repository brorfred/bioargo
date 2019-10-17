import os

import numpy as np

BIOARGO_VARLIST = ["chl_smooth",  "aou", "doxy", "bbp700_corr_smooth", 
                   "S", "T", "chl_spikes", "c1phase", "c2phase",
                   "sigma_theta0", "o2prcntsat", "bbp532_corr_smooth",
                   "Kd", "ocr", "bbp_slope_smooth", "bbp532_corr_smooth",
                   "S", "T", "bbp700_corr", "bbp532_corr"]
   
def read_variable(float_no="lovbio014b", datadir="./", varname="chl_smooth"):
    """read variable from bioargo .dat file
    Read data from a bioargo data file.

    Arguments
    ---------
    float_no: str
        Name of float
    varname: str
        Variable to read (will be included in file name)
    datadir: str
        Dir to look for datafiles

    Output
    ------
    time: Array-like
        Vector with julian dates
    depths: Array-like
        Vector with depths for observations (m)
    values: Array-like
        Vector with observed values
    """
    if not varname in BIOARGO_VARLIST:
        raise NameError("varname not valid")
    filename = f"{datadir}/{float_no}_xyz_{varname}.dat"
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}'' doesn't exist")
    time,depth,vals = np.loadtxt(filename, unpack=True, usecols=(0,1,2))
    time = time-366  #conversion between octave and python date
    return time,depth,vals

def read_mld(float_no="lovbio014b", datadir="./", mldtype="mld"):
    """Read mld from bioargo .dat file"""
    filename = f"{datadir}/{float_no}_mld.dat"
    mdict = {}
    time, mdict["mld"], mdict["010"], mdict["005"], mdict["001"] = np.loadtxt(filename, unpack=True, usecols=(0,1,2,3,4))
    time = time-366
    return time,mdict[mldtype]

"""
    elif 'ocr' in fn:
#        vmin_grg = 0.97 # for metbio002b
#        vmax_grg = 1.0  # for metbio002b
        x, y, z380, z412, z490, zpar = np.loadtxt(din + fn, unpack=True, usecols=(0,1,2, 3, 4, 5))
        x = x-366
        wv = 'par'
        z = eval('z'+wv)
        vmin_grg = -2.0#np.percentile(z, 5)# 0.95
        vmax_grg = 1.5#np.percentile(z, 95)# 1.2
        cmap = mpl.cm.RdYlBu_r
        ymax = 250
        title_grg = '$\log10[E_d($'+str(wv)+'$)]$ [$\mu$W cm$^{-2}$ nm$^{-1}$]'
        if wv=='par':
            title_grg = '$\log10[E_d($'+str(wv)+'$)]$ [$\mu$W cm$^{-2}$]'

    elif kdr:  # this needs to be above the Kd part
#        vmin_grg = 0.97 # for metbio002b
#        vmax_grg = 1.0  # for metbio002b
        x, y, Kd380, Kd412, Kd490, Kdpar = np.loadtxt(din + fn, unpack=True, usecols=(0,1,2, 3, 4, 5))
        x = x-366
        wv = '380'
        z = eval('Kd'+wv+'/Kd490')
        vmin_grg = -0.0#np.percentile(z, 5)# 0.95
        vmax_grg = 2.25#np.percentile(z, 95)# 1.2
        cmap = mpl.cm.jet
        ymax = 250
        title_grg = '$K_d(' + str(wv) + '):K_d(490)$  [-]'
        wv = wv+'_Kd490'
        if wv[0:3]=='412':
            vmin_grg = 0.75#np.percentile(z, 5)# 0.95
            vmax_grg = 1.50#np.percentile(z, 95)# 1.2

    elif 'Kd' in fn:
#        vmin_grg = 0.97 # for metbio002b
#        vmax_grg = 1.0  # for metbio002b
        x, y, Kd380, Kd412, Kd490, Kdpar = np.loadtxt(din + fn, unpack=True, usecols=(0,1,2, 3, 4, 5))
        x = x-366
        wv = '412'
        z = eval('Kd'+wv)
        vmin_grg = -0.0#np.percentile(z, 5)# 0.95
        vmax_grg = 0.1#np.percentile(z, 95)# 1.2
        cmap = mpl.cm.RdYlBu_r
        ymax = 250
        title_grg = '$K_d($' + str(wv) + '$)$  [m$^{-1}$]'
#        if wv=='490':
#            vmin_grg = 0.02#np.percentile(z, 5)# 0.95
#            vmax_grg = 0.05#np.percentile(z, 95)# 1.2
"""
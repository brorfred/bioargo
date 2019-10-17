
import numpy as np
import scipy.interpolate
import matplotlib as mpl

import cmocean

def get_colordict(fn, vals, wv=None):
    cmap = mpl.cm.jet
    vmin,vmax = np.percentile(vals, [5,95])
    if 'chl_smooth' in fn:
        vmin,vmax = np.percentile(vals, [2,98])
        title_grg = '$\log_{10}$(chl) [mg m$^{-3}$]'
        cmap = cmocean.cm.tempo_r
    elif 'chl_spikes' in fn:
        vmin,vmax = np.percentile(vals, [75,95])
        title_grg = '$\log_{10}$(chl_spikes) [mg m$^{-3}$]'
    elif 'slope_smooth' in fn:
        vmin,vmax = np.percentile(vals, [5,95])
        title_grg = 'b$_{bp}(532)$:b$_{bp}(700)$'
        cmap = mpl.cm.RdYlBu
    elif 'ocr' in fn:
        vmin,vmax= -2.0,1.5
        cmap = mpl.cm.RdYlBu_r
        if wv=='par':
            title_grg = '$\log10[E_d($'+str(wv)+'$)]$ [$\mu$W cm$^{-2}$]'
        else:
            title_grg = '$\log10[E_d($'+str(wv)+'$)]$ [$\mu$W cm$^{-2}$ nm$^{-1}$]'
    elif "kdr" in fn:
        if wv=='412':
            vmin,vmax = -0.0,225
        else:
            vmin,vmax = 0.75,1.5
        title_grg = '$K_d(' + str(wv) + '):K_d(490)$  [-]'
        cmap = mpl.cm.jet
    elif 'Kd' in fn:
        vmin,vmax = 0,0.1
        cmap = mpl.cm.RdYlBu_r
        title_grg = '$K_d($' + str(wv) + '$)$  [m$^{-1}$]'
    elif 'bbp532_corr_smooth' in fn:
        vmin,vmax = np.percentile(vals, [15,95])
        title_grg = '$\log_{10}$(b$_{bp}(532)$) [m$^{-1}$]'
        cmap = mpl.cm.hot
    elif 'bbp700_corr_smooth' in fn:
        vmin,vmax = -2.88, np.percentile(z, 95)
        title_grg = '$\log_{10}$(b$_{bp}(700)$) [m$^{-1}$]'
        cmap = mpl.cm.magma
    elif 'bbp532_corr' in fn:
        vmin,vmax = -3.1, -2.7
        title_grg = '$\log_{10}$(b$_{bp}(532)$) [m$^{-1}$]'
        cmap = mpl.cm.hot
    elif 'bbp700_corr' in fn:
        vmin,vmax = np.percentile(vals, [35,95])
        title_grg = '$\log_{10}$(b$_{bp}(700)$) [m$^{-1}$]'
        cmap = mpl.cm.magma
    elif 'doxy' in fn:
        vmin,vmax = np.percentile(vals, [1,55])
        title_grg = 'Dissolved oxygen [$\mu$mol kg$^{-1}$]'
        cmap = cmocean.cm.ice
    elif 'o2prcntsat' in fn:
        vmin,vmax = np.percentile(vals, [5,95])
        title_grg = 'Oxygen saturation [$\%$]'
        cmap = mpl.cm.jet
    elif 'aou' in fn:
        vmin,vmax = np.percentile(vals, [35,98])
        title_grg = 'Apparent Oxygen Utilisation [$\mu$mol kg$^{-1}$]'
        cmap = cmocean.cm.matter_r
    elif 'c1phase' in fn:
        vmin,vmax = np.percentile(vals, [5,95])
        title_grg = 'C1PHASE'
        cmap = mpl.cm.jet
    elif 'c2phase' in fn:
        vmin,vmax = np.percentile(vals, [5,95])
        title_grg = 'C2PHASE'
        cmap = mpl.cm.jet
    elif 'T' in fn:
        vmin,vmax = np.percentile(vals, [5,95])
        title_grg = 'T [$^{\circ}$C]'
        cmap = cmocean.cm.thermal
    elif 'S' in fn:
        vmin,vmax = 34.3,34.75
        title_grg = 'S [psu]'
        cmap = cmocean.cm.haline
    elif fn[-14:-4]=='oxygen_sat':
        vmin,vmax = 0,100
        title_grg = 'Oxygen Saturation [%]'
    elif fn[-7:-4]=='no3':
        vmin,vmax = 0,100
        title_grg = 'Nitrate [uM]'
    elif 'sigma_theta0' in fn:
        vmin,vmax = np.percentile(vals, [5,95])
        title_grg = '$\sigma_{0}$ [kg m$^{-3}$]'
    elif fn[len(float_no)+1+5:len(float_no)+1+17]=='POC_bbpcorr_':
        vmin,vmax = [0,3]
        title_grg = '$\log_{10}$(POC) [mg m$^{-3}$]'
    return dict(vmin=vmin, vmax=vmax, title=title_grg, cmap=cmap)
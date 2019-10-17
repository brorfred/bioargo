
import numpy as np
import scipy.interpolate
import matplotlib as mpl
from matplotlib import pyplot as plt

import cmocean
import seaborn as sns

def nice_dateaxis(fig=None, ax=None):
    fig = plt.gcf() if fig is None else fig
    ax = plt.gca() if ax is None else ax
    fig.autofmt_xdate() 
    ax.xaxis_date() 

def colorbar(vmin, vmax, cmap):
    ax1 = plt.gcf().add_axes([0.90, 0.25, 0.025, 0.65])
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm, orientation='vertical')
    imaxes = plt.gca()
    plt.axes(cb1.ax)
    plt.yticks(fontsize=14)
    plt.axes(imaxes)

def time_depth(time, depths, vals, ymax=500, vmin=None, vmax=None, cmap=None, title=""):
    """Plot a depth slice of an argo float"""
    plt.close("all")
    plt.figure(1,(16,6))
    #plt.gcf().set_size_inches(16, 6)
    sc = plt.scatter(time, depths, s=64, c=vals, marker='o', edgecolors='none', 
                     vmin=vmin, vmax=vmax, cmap=cmap)
    plt.ylim(0, ymax)
    plt.gca().invert_yaxis()
    plt.ylabel('Depth [m]')
    plt.title(title)
    nice_dateaxis()

def mld(time, depths):
    """Plot mld on a depth slice of an argo float"""
    return plt.plot(time, depths, 'w-', lw=2)

def contour_sigma_theta0(ax=None, st0min=26.5, st0max = 27.):
    """add contours of Sigma Theta0"""
    ax = plt.gca if ax is None else ax
    fnin = float_no + '_xyz_sigma_theta0.dat'
    xst0,yst0,st0 = np.loadtxt(din + fnin, unpack=True, usecols=(0,1,2))
    xst0 = xst0-366;  #conversion between octave and python date
    # Set up a regular grid of interpolation points
    xi, yi = np.linspace(xst0.min(), xst0.max(), 100), np.linspace(yst0.min(), yst0.max(), 100)
    xi, yi = np.meshgrid(xi, yi)
    #    # Interpolate; there's also method='cubic' for 2-D data such as here
    zi = scipy.interpolate.griddata((xst0, yst0), st0, (xi, yi), method='linear')
    CS = ax.contour(xi, yi, zi, linspace(st0min, st0max, num=5), colors='w', linewidths=1)
    paxlt.clabel(CS, inline=1, fontsize=20, colors='w')

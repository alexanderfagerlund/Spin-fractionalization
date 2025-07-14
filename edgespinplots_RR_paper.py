# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 08:59:07 2024

@author: 46730
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv
import sys
from matplotlib.gridspec import GridSpec
#import sympy as sp
from mpl_toolkits.axes_grid1 import make_axes_locatable



mpl.rcParams['text.usetex'] = True
params = {
    'image.origin': 'lower',
    'image.interpolation': 'nearest',
    'image.cmap': 'gray',
    'axes.grid': False,
    'savefig.dpi': 800,  # to adjust notebook inline plot size
    'axes.labelsize': 10, # fontsize for x and y labels (was 10)
    'axes.titlesize': 10,
    #'font.size': 16, # was 10
    'legend.fontsize': 10, # was 10
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'text.usetex': True,
    #'figure.figsize': [3.39, 2.10],
    "font.family": "serif",   # Set font family to serif (matches APS default)
    "font.serif": ["Times New Roman"],  # Choose the serif font (Times New Roman is typical for APS)
    "text.latex.preamble": r"\usepackage{amsmath}",
}
mpl.rcParams.update(params)

mpl.rc('text.latex', preamble=r'\usepackage{dsfont}')


fs=10

je1 = np.loadtxt('jeList1v3.csv', delimiter=',')
jeSigma1 = np.loadtxt('jeListsigma1v3.csv', delimiter=',')
jeSigma2 = np.loadtxt('jeListsigma2v3.csv', delimiter=',')
jePsi1mod=np.loadtxt('jeListpsi1v3.csv', delimiter=',')
jePsi2mod=np.loadtxt('jeListpsi2v3.csv', delimiter=',')
jeEpsmod=np.loadtxt('jeListepsv3.csv', delimiter=',')

jb1 = np.loadtxt('jb1List.csv', delimiter=',')
jbSigma1 = np.loadtxt('jbSigma1List.csv', delimiter=',')
jbSigma2 = np.loadtxt('jbSigma2List.csv', delimiter=',')
jbPsi1mod=np.loadtxt('jbPsi1List.csv', delimiter=',')
jbPsi2mod=np.loadtxt('jbPsi2List.csv', delimiter=',')
jbEpsmod=np.loadtxt('jbEpsilonList.csv', delimiter=',')


fig_width = 3+3/8  # inches (standard APS journal column width)
fig_height = 3.4  # inches (adjust as necessary)

# Set up the figure
fig = plt.figure(figsize=(fig_width, fig_height))
#fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)
gs = GridSpec(nrows=2, ncols=2, figure=fig, height_ratios=[1,1])  # 2:1 ratio for upper to lower rows


x_values_je1, y_values_je1 = zip(*je1)
x_values_jeSigma1, y_values_jeSigma1 = zip(*jeSigma1)
x_values_jeSigma2, y_values_jeSigma2 = zip(*jeSigma2)
x_values_jePsi1mod, y_values_jePsi1mod = zip(*jePsi1mod)
x_values_jePsi2mod, y_values_jePsi2mod = zip(*jePsi2mod)
x_values_jeEpsmod, y_values_jeEpsmod = zip(*jeEpsmod)

x_values_jb1, y_values_jb1 = zip(*jb1)
x_values_jbSigma1, y_values_jbSigma1 = zip(*jbSigma1)
x_values_jbSigma2, y_values_jbSigma2 = zip(*jbSigma2)
x_values_jbPsi1, y_values_jbPsi1 = zip(*jbPsi1mod)
x_values_jbPsi2, y_values_jbPsi2 = zip(*jbPsi2mod)
x_values_jbEps, y_values_jbEps = zip(*jbEpsmod)


#y_values_jePsi1mod=[s % 1 for s in y_values_jePsi1mod]
#y_values_jePsi2mod=[s % 1 for s in y_values_jePsi2mod]
#y_values_jeEpsmod=[s % 1 for s in y_values_jeEpsmod]

sp=0.1
lw=1
lwdash=0.7

ax11 = fig.add_subplot(gs[0, 1])  # First row, each column
ax11.set_xlim(115, 145)  # Set the x-axis range from 2 to 8
ax11.set_ylim(-2, 0.2)  # Set the y-axis range from 3 to 7
ax11.set_aspect('auto')
ax11.set_yticks((-1.5,-1.0,-0.5,0))
label11 = (r'$-1.5$',r'$-1.0$',r'$-0.5$',r'$0.0$')
#plt.ylabel(r'$J_{e}$',fontsize=fs,labelpad=-20,rotation=0,loc='top')
ax11.set_yticklabels(label11, minor=False,ha='right')
ax11.get_xaxis().set_visible(False)
ax11.yaxis.tick_right()
ax11.yaxis.set_tick_params(pad=23)

tick_labels = ax11.get_yticklabels()
custom_padding=[-0.02,-0.02,-0.02,-0.02]

# Update tick labels with proper horizontal alignment
for i, label in enumerate(tick_labels):
    label.set_position((label.get_position()[0]+ custom_padding[i], label.get_position()[1] ))

#ax11.set_yticks(np.arange(-1, 0.6, 0.5))
ax11.axhline(y=-1/5, color='blue', linestyle='--',linewidth=lwdash)
ax11.axhline(y=-2/5, color='red', linestyle='--',linewidth=lwdash)
ax11.axhline(y=-3/5, color='black', linestyle='--',linewidth=lwdash)
ax11.plot(x_values_jeSigma1, y_values_jeSigma1, linestyle='-', color='blue', label=r'$\sigma_1$',linewidth=lw)
ax11.plot(x_values_jeSigma2, y_values_jeSigma2, linestyle='-', color='red', label=r'$\sigma_2$',linewidth=lw)
ax11.plot(x_values_je1, y_values_je1, linestyle='-', color='black', label=r'$\mathds{1}$',linewidth=lw)
ax11.text(0.045, 0.95, "c)", transform=ax11.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='left', color='black')
#plt.xlabel(r'$X_0$',fontsize=fs)

hp=0.5

#plt.ylabel(r'$J_{e}$', fontsize=fs)
ax11.set_title(r'Edge - $J_e$', fontsize=fs)
#ax11.set_title('Some spins')
#legend=ax11.legend( loc=(0.04,0.04),labelspacing=sp,handlelength=1,handletextpad=hp, columnspacing=1.0, frameon=False)
#for label in legend.get_texts():
#    label.set_verticalalignment('bottom')

#label.set_verticalalignment('baseline')

ax12 = fig.add_subplot(gs[1, 1])  # First row, each column
ax12.set_xlim(115, 145)  # Set the x-axis range from 2 to 8
ax12.set_ylim(-7.5, 0.3)  # Set the y-axis range from 3 to 7
ax12.set_aspect('auto')
ax12.set_yticks((-7,-5,-3,-1))
ax12.set_xticks((120,130,140))
#plt.ylabel(r'$J_{e}$',fontsize=fs,labelpad=-20,rotation=0,loc='top')
label12 = (r'$-7.0$',r'$-5.0$',r'$-3.0$',r'$-1.0$')
ax12.set_yticklabels(label12, minor=False,ha='right')
ax12.get_xaxis().set_visible(True)
plt.xlabel(r'$X_0$',fontsize=fs,labelpad=2)
ax12.yaxis.tick_right()
ax12.yaxis.set_tick_params(pad=23)
ax12.axhline(y=-1.8, color='green', linestyle='--',linewidth=lwdash)
ax12.axhline(y=-4.0, color='orangered', linestyle='--',linewidth=lwdash)
ax12.axhline(y=-2.2, color='purple', linestyle='--',linewidth=lwdash)
ax12.plot(x_values_jePsi1mod, y_values_jePsi1mod, linestyle='-', color='green', label=r'$\psi_1$',linewidth=lw)
ax12.plot(x_values_jeEpsmod, y_values_jeEpsmod, linestyle='-', color='purple', label=r'$\epsilon$',linewidth=lw)
ax12.plot(x_values_jePsi2mod, y_values_jePsi2mod, linestyle='-', color='orangered', label=r'$\psi_2$',linewidth=lw)
#ax12.axhline(y=-1.8, color='red', linestyle='--',label=r'$J_{e} = 0$')
#ax12.axhline(y=-4, color='blue', linestyle='--',label=r'$J_{e} = 0$')
#ax12.axhline(y=-2.2, color='green', linestyle='--',label=r'$J_{e} = 0$')
ax12.text(0.045, 0.95, "d)", transform=ax12.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='left', color='black')
#plt.xlabel(r'$X_0$',fontsize=fs)
#plt.ylabel(r'$J_{e}$', fontsize=fs)
#ax12.set_title(r'$J_e$', fontsize=fs)
#ax11.set_title('Some spins')
tick_labels = ax12.get_yticklabels()
custom_padding=[-0.02,-0.02,-0.02,-0.02]

# Update tick labels with proper horizontal alignment
for i, label in enumerate(tick_labels):
    label.set_position((label.get_position()[0]+ custom_padding[i], label.get_position()[1] ))

#legend=ax12.legend( loc=(0.02,0.02),labelspacing=sp,handlelength=1,handletextpad=hp, columnspacing=1.0, frameon=False)
#for label in legend.get_texts():
#    label.set_verticalalignment('bottom')

ax21 = fig.add_subplot(gs[0, 0])  # First row, each column
ax21.set_xlim(0, 30)  # Set the x-axis range from 2 to 8
ax21.set_ylim(-0.1, 1.4)  # Set the y-axis range from 3 to 7
ax21.set_aspect('auto')
ax21.get_xaxis().set_visible(False)
ax21.set_yticks((0.0,0.3,0.6,0.9,1.2))
#plt.ylabel(r'$J_{qp}$',fontsize=fs,labelpad=0,rotation=0,loc='top')
#ax21.yaxis.set_label_position('right')
ax21.axhline(y=1/5, color='blue', linestyle='--',linewidth=lwdash)
ax21.axhline(y=2/5, color='red', linestyle='--',linewidth=lwdash)
ax21.axhline(y=3/5, color='black', linestyle='--',linewidth=lwdash)
ax21.plot(x_values_jbSigma1, y_values_jbSigma1,  linestyle='-', color='blue', label=r'$\sigma_1$',linewidth=lw)
ax21.plot(x_values_jbSigma2, y_values_jbSigma2,  linestyle='-', color='red', label=r'$\sigma_2$',linewidth=lw)
ax21.plot(x_values_jb1, y_values_jb1,  linestyle='-', color='black', label=r'$\mathds{1}$',linewidth=lw)
ax21.text(0.045, 0.95, "a)", transform=ax21.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='left', color='black')
ax21.set_yticklabels((r'$0.0$',r'$0.3$',r'$0.6$',r'$0.9$',r'$1.2$'))
ax21.yaxis.tick_left()
ax21.yaxis.set_tick_params(pad=9)

tick_labels = ax21.get_yticklabels()
custom_padding=[0.08,0.08,0.08,0.08,0.08]

# Update tick labels with proper horizontal alignment
for i, label in enumerate(tick_labels):
    label.set_position((label.get_position()[0]+ custom_padding[i], label.get_position()[1] ))

#ax21.axhline(y=1/5, color='black', linestyle='--',label=r'$J_{e} = 0$')
#ax21.axhline(y=2/5, color='black', linestyle='--',label=r'$J_{e} = 0$')
#ax21.axhline(y=3/5, color='black', linestyle='--',label=r'$J_{e} = 0$')
#plt.xlabel(r'$X_0$',fontsize=fs)
#plt.ylabel(r'$J_{e}$', fontsize=fs)
#ax21.set_title(r'$1$', fontsize=fs)

ax21.set_title(r'Bulk - $J_{qp}$')
legend=ax21.legend( loc=(0.5,0.57),labelspacing=sp,handlelength=1,handletextpad=hp, columnspacing=1.0, frameon=False)
for label in legend.get_texts():
    label.set_verticalalignment('bottom')
label.set_verticalalignment('baseline')

ax22 = fig.add_subplot(gs[1, 0])  # First row, each column
ax22.set_xlim(0, 30)  # Set the x-axis range from 2 to 8
ax22.set_ylim(-1.6, 1.4)  # Set the y-axis range from 3 to 7
ax22.set_yticks((-1.5,-0.9,-0.3,0.3,0.9))
label22 = (r'$-1.5$',r'$-0.9$',r'$-0.3$',r'$0.3$',r'$0.9$')
ax22.set_yticklabels(label22, minor=False,ha='right')
ax22.yaxis.set_tick_params(pad=9)

tick_labels = ax22.get_yticklabels()
custom_padding=[0.08,0.08,0.08,0.08,0.08]

# Update tick labels with proper horizontal alignment
for i, label in enumerate(tick_labels):
    label.set_position((label.get_position()[0]+ custom_padding[i], label.get_position()[1] ))


#ax22.set_aspect(asp-2.8)
ax22.get_xaxis().set_visible(True)
plt.xlabel(r'$R$',fontsize=fs,labelpad=2)
#plt.ylabel(r'$J_{qp}$',fontsize=fs,labelpad=0,rotation=0,loc='top')
#ax22.yaxis.set_label_position('right')
ax22.set_xticks((0,15,30))
ax22.axhline(y=-1/5, color='green', linestyle='--',linewidth=lwdash)
ax22.axhline(y=0, color='orangered', linestyle='--',linewidth=lwdash)
ax22.axhline(y=1/5, color='purple', linestyle='--',linewidth=lwdash)
ax22.text(0.045, 0.95, "b)", transform=ax22.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='left', color='black')
ax22.plot(x_values_jbPsi1, y_values_jbPsi1,  linestyle='-', color='green', label=r'$\psi_1$',linewidth=lw)
ax22.plot(x_values_jbEps, y_values_jbEps,  linestyle='-', color='purple', label=r'$\epsilon$',linewidth=lw)
ax22.plot(x_values_jbPsi2, y_values_jbPsi2,  linestyle='-', color='orangered', label=r'$\psi_2$',linewidth=lw)
#ax22.axhline(y=-1/5, color='black', linestyle='--',label=r'$J_{e} = 3/5$')
#ax22.axhline(y=0, color='black', linestyle='--',label=r'$J_{e} = 3/5$')
#ax22.axhline(y=1/5, color='black', linestyle='--',label=r'$J_{e} = 3/5$')
#plt.xlabel(r'$X_0$',fontsize=fs)
#plt.ylabel(r'$J_{e}$', fontsize=fs)
#ax22.set_title(r'$\psi_1$', fontsize=fs)
#ax11.set_title('Some spins')
legend=ax22.legend( loc=(0.5,0.015),labelspacing=sp,handlelength=1,handletextpad=hp, columnspacing=1.0, frameon=False)

# Adjust vertical alignment of the legend text
for label in legend.get_texts():
    label.set_verticalalignment('bottom')

# Adjust layout for better spacing
dpival=600
plt.tight_layout(w_pad=0.65,h_pad=0.0)
plt.savefig("edge_spin_fig_2.pdf", format="pdf", pad_inches=0.1,dpi=dpival,bbox_inches='tight')
# Show the grid of plots
plt.show()

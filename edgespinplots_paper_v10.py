import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv
import sys
import random
from matplotlib.gridspec import GridSpec
import sympy as sp
from mpl_toolkits.axes_grid1 import make_axes_locatable

dpival=600

params = {
    'image.origin': 'lower',
    'image.interpolation': 'nearest',
    'image.cmap': 'gray',
    'axes.grid': False,
    'savefig.dpi': dpival,  # to adjust notebook inline plot size
    'axes.labelsize': 11, # fontsize for x and y labels (was 10)
    'axes.titlesize': 11,
    #'font.size': 16, # was 10
    'legend.fontsize': 11, # was 10
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'text.usetex': True,
    #'figure.figsize': [3.39, 2.10],
    "font.family": "serif",   # Set font family to serif (matches APS default)
    "font.serif": ["Times New Roman"],  # Choose the serif font (Times New Roman is typical for APS)
    "text.latex.preamble": r"\usepackage{amsmath}",
}
mpl.rcParams.update(params)


n0 = np.loadtxt('nzero.csv', delimiter=',')
nqh = np.loadtxt('nqh.csv', delimiter=',')
#je=np.loadtxt('jelistNormdelta=0point02.csv',delimiter=',')
je=np.loadtxt('jelistNormdelta=0point02Novernu.csv',delimiter=',')
#je = np.loadtxt('jelist.csv', delimiter=',')
#jb = np.loadtxt('jblist.csv', delimiter=',')    
#jb = np.loadtxt('jblistdelta=0point1.csv', delimiter=',') 
jb = np.loadtxt('jblistdelta=0point02.csv', delimiter=',')   

lx=22;
nu=1/3;
c = 2*np.pi/nu;
tmin0 = 0 #2*np.pi/lx*(len(n0) - 1)/2;

def rho0(t,x):
    dens0=0.0;
    for m in range(0,len(n0)-1):
        dens0 += c*np.exp((0+1j)*x*(m - m)*2*np.pi/lx)*np.exp(-1/2* ((t + tmin0) - 2*np.pi*m/lx)**2 - 1/2*((t + tmin0) - 2*np.pi*m/lx)**2)*n0[m]/(lx*np.sqrt(np.pi))
    return np.real(dens0)

def rhoqh(t,x):
    densqh=0.0;
    for m in range(0,len(nqh)-1):
        for n in range(0,len(nqh[m])-1):
            densqh += c*np.exp((0+1j)*x*(m - n)*2*np.pi/lx)*np.exp(-1/2 *((t + tmin0) - 2*np.pi*m/lx)**2 - 1/2*((t + tmin0) - 2*np.pi*n/lx)**2)*nqh[m][n]/(lx*np.sqrt(np.pi))
    return np.real(densqh)

def rhodiff(t,x):
    return rhoqh(t,x)-rho0(t,x)

# Step 1: Create a grid of x and y values
xvec = np.linspace(-lx/2, lx/2, 220)    

cen=298.5*2*np.pi/lx



# Define the t ranges for each region
#tvec1 = np.linspace(-2, 6, 80)  # First region t values: earlier (-86,-80,3)
#tvec2 = np.linspace(cen-5, cen+5, 100)    # Second region t values
#tvec3 = np.linspace(2*cen-6, 2*cen+2, 80)   # Third region t values (80,86,3)

# Create mesh grids for each region
#T1, X1 = np.meshgrid(tvec1, xvec)
#T2, X2 = np.meshgrid(tvec2, xvec)
#T3, X3 = np.meshgrid(tvec3, xvec)

# Evaluate the function rho0(t, x) on each grid
#Z1no = rho0(T1, X1)
#Z2no = rho0(T2, X2)
#Z3no = rho0(T3, X3)

# Evaluate the function rhoqh(t, x) on each grid
#Z1qh = rhoqh(T1, X1)
#Z2qh = rhoqh(T2, X2)
#Z3qh = rhoqh(T3, X3)

#data_size=(13,11)

# Evaluate the function rhoqh(t, x) on each grid
#Z1diff = rhodiff(T1, X1)
#Z2diff = rhodiff(T2, X2)
#Z3diff = rhodiff(T3, X3)

# Concatenate the regions horizontally to form a combined heatmap
#Z_combined_no = np.hstack([Z1no, Z2no, Z3no])
#Z_combined_qh = np.hstack([Z1qh, Z2qh, Z3qh])
#Z_combined_diff = np.hstack([Z1diff, Z2diff, Z3diff])


#np.savetxt('Z_0.txt', Z_combined_no)
#np.savetxt('Z_qh.txt', Z_combined_qh)
#np.savetxt('Z_diff.txt', Z_combined_diff)


Z_combined_no = np.loadtxt('Z_0.txt')
Z_combined_qh = np.loadtxt('Z_qh.txt')
Z_combined_diff = np.loadtxt('Z_diff.txt')

# Define the number of rows and columns
nrows, ncols = 3, 9  # 2 rows, 3 columns (first row for heatmaps, second for regular plots)

# Create a figure with a custom gridspec layout, adjusting column width ratios and height ratios
fig_width = 3.375  # inches (standard APS journal column width)
fig_height = 3.1  # inches (adjust as necessary)

# Set up the figure
fig = plt.figure(figsize=(fig_width, fig_height))
fig.dpi=dpival
#fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)
gs = GridSpec(nrows, ncols, figure=fig, height_ratios=[1.1,0.7,1.5],width_ratios=[0.0,1,1,1,1,-0.30,1,1.304,0.1])  # 2:1 ratio for upper to lower rows
extent = [-13, 13, -11, 11]
#for spine in fig.spines.values():
#    spine.set_visible(False)
#fig.supxlabel('')  # If there are any super xlabel
#fig.supylabel('')  # If there are any super ylabel
# Generate random data for the heatmaps (replace with your own data)

fs=11;

minval=-1
maxval=max((max(Z_combined_qh[0]),max(Z_combined_no[0])))

ax1 = fig.add_subplot(gs[0, 1:3])  # First row, each column
ax1.set_xlim(-13,13)  # Set the x-axis range from 2 to 8
ax1.set_ylim(-lx/2, lx/2)  # Set the y-axis range from 3 to 7
#ax1.set_title(r'$\rho_0$', fontsize=fs)
ax1.text(0.50, 0.95, r'$\rho_0$', transform=ax1.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='center', color='black')
ax1.set_aspect('auto')

x1 = (-11,-7,-2.5+0.24859935485879703,2.5+0.24859935485879703,7+0.49719870971759406,12+0.49719870971759406)
y1 = (-10,-5,0,5,10)
label1 = (r'$0$',r'$4$',r'$83$',r'$88$',r'$167$',r'$172$')
ax1.set_xticks(x1)
ax1.set_xticklabels(label1, minor=False)
ax1.set_yticks(y1)
ax1.axvline(x=5, color='red', linestyle='--', linewidth=2)
ax1.axvline(x=-5, color='red', linestyle='--', linewidth=2)
plt.xlabel(r'$x$',fontsize=fs,labelpad=0)
plt.ylabel(r'$y$',labelpad=-6,fontsize=fs)
ax1.text(0.05, 0.95, "a)", transform=ax1.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='left', color='black')
img1 = ax1.imshow(Z_combined_no, vmin=minval, vmax=maxval, cmap='inferno', interpolation='nearest',extent=extent)
#divider1 = make_axes_locatable(ax1)
#cax1 = divider1.append_axes("right", size="5%", pad=0.1)

#ticklabs1 = cax1.get_yticklabels()
#cax1.set_yticklabels(ticklabs1,ha='right')
#cax1.yaxis.set_tick_params(pad=35)

#for lab in cax1.get_yticklabels():
#    lab.set_horizontalalignment('right')
#    lab.set_x(3.5)
#fig.colorbar(img1, cax=cax1)

ax2 = fig.add_subplot(gs[0, 3:5])  # First row, each column
ax2.set_xlim(-13, 13)  # Set the x-axis range from 2 to 8
ax2.set_ylim(-lx/2, lx/2)  # Set the y-axis range from 3 to 7
#ax2.set_title(r'$\rho_1$', fontsize=fs)
ax2.set_yticks(y1)
ax2.get_yaxis().set_visible(False)
plt.xlabel(r'$x$',fontsize=fs,labelpad=0)
#plt.ylabel(r'$y$',labelpad=-10,fontsize=fs)
#initial_pos = ax2.get_position()
#initial_width = initial_pos.width
#initial_height = initial_pos.height
#initial_aspect_ratio = initial_width / initial_height
#print(f"Initial aspect ratio: {initial_aspect_ratio:.3f}")
#ax2.set_aspect(initial_aspect_ratio)
ax2.text(0.50, 0.95, r'$\rho_1$', transform=ax2.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='center', color='black')
ax2.text(0.05, 0.95, "b)", transform=ax2.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='left', color='black')
img2 = ax2.imshow(Z_combined_qh, vmin=minval, vmax=maxval, cmap='inferno', interpolation='nearest',extent=extent)
#cax2 = fig.add_axes([ax2.get_position().x1+0.025,
#                    ax2.get_position().y0+0.01,
#                    0.015,
#                    ax2.get_position().height+0.01])
#divider2 = make_axes_locatable(ax2)
#cax2 = divider2.append_axes("right", size="5%", pad=0.1)
#ticklabs2 = cax2.get_yticklabels()
#cax2.set_yticklabels(ticklabs2,ha='right')
#cax2.yaxis.set_tick_params(pad=35)
#fig.colorbar(img2, cax=cax2)
#new_pos = ax2.get_position()  # This gives the new position after colorbar is added
#new_width = new_pos.width
#new_height = new_pos.height
#new_aspect_ratio = new_width / new_height
#print(f"New aspect ratio (after colorbar): {new_aspect_ratio:.3f}")
ax2.set_xticks(x1)
ax2.set_xticklabels(label1, minor=False)
ax2.axvline(x=5, color='red', linestyle='--', linewidth=2)
ax2.axvline(x=-5, color='red', linestyle='--', linewidth=2)




ax3 = fig.add_subplot(gs[0, 5:8])  # First row, each column
ax3.set_xlim(-13,13)  # Set the x-axis range from 2 to 8
ax3.set_ylim(-lx/2, lx/2)  # Set the y-axis range from 3 to 7
#ax3.set_title(r'$\delta\rho=\rho_1-\rho_0$', fontsize=fs)
ax3.text(0.50, 0.95, r'$\delta\rho$', transform=ax3.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='center', color='black')
ax3.set_yticks(y1)
ax3.get_yaxis().set_visible(False)
plt.xlabel(r'$x$',fontsize=fs,labelpad=0)
#plt.ylabel(r'$z_2$', labelpad=50,fontsize=fs)
#ax3.set_aspect(0.696)
ax3.text(0.05, 0.95, "c)", transform=ax3.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='left', color='black')
img3 = ax3.imshow(Z_combined_diff, vmin=minval, vmax=maxval, cmap='inferno', interpolation='nearest',extent=extent)
divider3 = make_axes_locatable(ax3)
cax3 = divider3.append_axes("right", size="5%", pad=0.1)
#im_ratio = Z_combined_diff.shape[0]/Z_combined_diff.shape[1] 
#fig.colorbar(img3,fraction=0.046*im_ratio, pad=0.04)
ax3.set_xticks(x1)
ax3.set_xticklabels(label1, minor=False)
ax3.axvline(x=5, color='red', linestyle='--', linewidth=2)
ax3.axvline(x=-5, color='red', linestyle='--', linewidth=2)
ticklabs3 = cax3.get_yticklabels()
cax3.set_yticklabels(ticklabs3,ha='right')
cax3.yaxis.set_tick_params(pad=25)
#cax3 = fig.add_axes([0.96, 0.53, 0.01, 0.415])
fig.colorbar(img3, cax=cax3,ticks=[-1,-0.5,0,0.5,1])
#plt.subplots_adjust(wspace=-5.0,hspace=5.0)
#plt.subplots_adjust(wspace=-10.0,hspace=15.0)

for ax in [ax1, ax2, ax3]:
    for label in ax.get_xticklabels():
        label.set_verticalalignment('center')  # Align all labels vertically at the center
        label.set_horizontalalignment('center')  # Align all labels horizontally at the center
        label.set_y(-0.05)
        

current_position = ax3.get_position()

# Modify the position of ax3 (e.g., move it slightly to the left and reduce its width)
new_position = [current_position.x0 + 2, current_position.y0, current_position.width, current_position.height]

# Set the new position for ax3
ax3.set_position(new_position)

# Generate regular plots for the second row (with space between them)
jbdata=jb
# Unpack the list of tuples into x and y values
x_values_jb, y_values_jb = zip(*jbdata)
ax4 = fig.add_subplot(gs[2, 1:4])  # Second row, each column
ax4.set_aspect(46) #22.2 at 0.8
ax4.set_ylim(-0.08, 0.65)  # x-axis range from 0 to 5
ax4.set_yticks(np.arange(0.0, 0.7, 0.2))  # Add ticks from -1 to 1 with a step of 0.2
# Create a line plot connecting the points with lines
ax4.plot(x_values_jb, y_values_jb,  linestyle='-', color='red', label=r'$J_{qp}(R)$',linewidth=1.5)
plt.axhline(y=1/3, color='black', linestyle='--', dashes=(2.5, 3), label=r'$J_{qp} = 1/3$',linewidth=1.5)
plt.xlabel(r'$R$',fontsize=fs)
ax4.text(0.03, 0.94, "d)", transform=ax4.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='left', color='black')
#plt.ylabel(r'$J_{qh}$', fontsize=fs)
#plt.title(r'$J_{qh}$', fontsize=fs)
ax4.legend(loc=4,fontsize=fs)

jedata=je
# Unpack the list of tuples into x and y values
x_values_je, y_values_je = zip(*jedata)
ax5 = fig.add_subplot(gs[2, 4:8])  # Second row, each column
#ax5.set_aspect(30.9)
ax5.set_aspect(29.77)
#ax5.set_xlim(44, 101)  # x-axis range from 0 to 5
# Create a line plot connecting the points with lines
#ax5.set_yticks(np.arange(-0.6, 0.4, 0.2))  # Add ticks from -1 to 1 with a step of 0.2
#ax5.set_yticks((-1.2,-1.0,-0.8,-0.6,-0.4,-0.2, 0))
#ax5.set_yticklabels((r'$-1.2$',r'$-1.0$',r'$-0.8$',r'$-0.6$',r'$-0.4$',r'$-0.2$',r'$0.0$'),ha='right')
ax5.set_yticks((-1.2,-1.0,-0.8,-0.6,-0.4,-0.2, 0.0))
ax5.set_yticklabels((r'$-1.2$',r'$-1.0$',r'$-0.8$',r'$-0.6$',r'$-0.4$',r'$-0.2$',r'$0.0$'),ha='right')
ax5.plot(x_values_je, y_values_je,  linestyle='-', color='red', label=r'$J_{e}(X_0)$',linewidth=1.5)
ax5.yaxis.tick_right()
ax5.yaxis.set_tick_params(pad=25)
plt.axhline(y=-1/3, color='black', linestyle='--', dashes=(2.5, 3),label=r'$J_{e} = -1/3$',linewidth=1.5)
plt.xlabel(r'$X_0$',fontsize=fs)
ax5.text(0.03, 0.94, "e)", transform=ax5.transAxes, fontsize=fs, verticalalignment='top', horizontalalignment='left', color='black')
#plt.ylabel(r'$J_{e}$', fontsize=fs)
#plt.title(r'$J_{e}$', fontsize=fs)
ax5.legend( loc=3,fontsize=fs,labelspacing=0.57)

for label in ax5.get_yticklabels():
    label.set_verticalalignment('center')  # Align all labels vertically at the center
    label.set_horizontalalignment('right')  # Align all labels horizontally at the center

tick_labels = ax5.get_yticklabels()
custom_padding=[0.005,0.005,0.005,0.005,0.005,0.005,0.005]

# Update tick labels with proper horizontal alignment
for i, label in enumerate(tick_labels):
    label.set_position((label.get_position()[0]+ custom_padding[i], label.get_position()[1] ))

tick_labels = cax3.get_yticklabels()
custom_padding=[0.007,0.007,0.007,0.007,0.007]

# Update tick labels with proper horizontal alignment
for i, label in enumerate(tick_labels):
    label.set_position((label.get_position()[0]+ custom_padding[i], label.get_position()[1] ))

plt.subplots_adjust(wspace=-70.0,hspace=5)

# Adjust layout for better spacing
plt.tight_layout(pad=-4.5)

fig.set_size_inches(3.375,2.5)

plt.savefig("edge_spin_fig_1.pdf", format="pdf", pad_inches=0.2,dpi=dpival,bbox_inches='tight')

# Show the grid of plots
plt.gcf().set_dpi(dpival)
plt.show()


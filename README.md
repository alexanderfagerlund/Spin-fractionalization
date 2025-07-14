# Spin fractionalization

Supporting data for the paper "Spin fractionalization at the edge of quantum Hall fluids induced by bulk quasiparticles". Arxiv link: https://arxiv.org/abs/2412.14879

# Explanation of files:

## Files for Fig. 1:

nzero.csv: occupation numbers for system without any quasihole.

nqh.csv: matrix of <c_m^{\dagger}c_n> values for system with a quasihole.

jelistNormdelta=0point02Novernu.csv: edge spin values computed using Mathematica.

jblistdelta=0point02.csv: bulk spin values computed using Mathematica.

edgespinplots_paper_v10.py: used to plot the density and spin data in Fig. 1, using the .csv files above. 

## Files for Fig. 2:

jeList1v3.csv: edge spin data for the Laughlin quasihole.

jeListsigma1v3.csv: edge spin data for the sigma_1 quasihole.

jeListsigma2v3.csv: edge spin data for the sigma_2 quasihole.

jeListpsi1v3.csv: edge spin data for the psi_1 quasihole.

jeListpsi2v3.csv: edge spin data for the psi_2 quasihole.

jeListepsv3.csv: edge spin data for the epsilon quasihole.

jb1List.csv: bulk spin data for the Laughlin quasihole.

jbSigma1List.csv: bulk spin data for the sigma_1 quasihole.

jbSigma2List.csv: bulk spin data for the sigma_2 quasihole.

jbPsi1List.csv: bulk spin data for the psi_1 quasihole.

jbPsi2List.csv: bulk spin data for the psi_2 quasihole.

jbEpsilonList.csv: bulk spin data for the epsilon quasihole.

edgespinplots_RR_paper.py: used to plot the spin data in Fig. 2, using the .csv files above.

## Files for computing the data used above:

### Programs for computation: 

edgeSpinPlot.nb: used to compute bulk and edge spins for Fig. 1.

Datagen_edgespin_paper.nb: used to compute edge spins for Fig. 2.

The program for computing the bulk spins in Fig. 2 is available upon reasonable request.

### MPS data used in the above programs:

laughlin-corrmat-noqhs-lx=22-m=3-Ne=200-cutoff=16.wl: correlation matrix for Laughlin fluid without quasiholes.

laughlin-corrmat-lx=22-m=3-Ne=200-qhtype=1-cutoff=16.wl: correlation matrix for Laughlin fluid with a quasihole.

corrmat-noqhs-lx=22-m=1-Ne=120-cutoff=12.wl: correlation matrix for RR fluid with 120 electrons, without quasiholes.

corrmat-noqhs-lx=22-m=1-Ne=298-cutoff=12.wl: correlation matrix for RR fluid with 298 electrons, without quasiholes.

corrmat-noqhs-lx=22-m=1-Ne=299-cutoff=12.wl: correlation matrix for RR fluid with 299 electrons, without quasiholes.

corrmat-lx=22-m=1-Ne=300-qhtype=1_2_0-cutoff=12.wdx: correlation matrix for the sigma_1 quasihole.

corrmat-lx=22-m=1-Ne=300-qhtype=2_-2_0-cutoff=12.wdx: correlation matrix for the sigma_2 quasihole.

corrmat-lx=22-m=1-Ne=300-qhtype=3_0_0-cutoff=12.wdx: correlation matrix for the Laughlin quasihole.

corrmat-lx=22-m=1-Ne=299-qhtype=2_4_0-cutoff=12.wdx: correlation matrix for the psi_1 quasihole.

corrmat-lx=22-m=1-Ne=299-qhtype=3_0_2-cutoff=12.wdx: correlation matrix for the epsilon quasihole.

corrmat-lx=22-m=1-Ne=298-qhtype=4_-4_0-cutoff=12.wdx: correlation matrix for the psi_2 quasihole.

### Bulk spin data for RR fluid:

spin-1drev-lx=22-m=1-Ne=300-qhtype=1_2_0-cutoff=12.wl: bulk spin for sigma_1 quasihole.

spin-1drev-lx=22-m=1-Ne=300-qhtype=2_-2_0-cutoff=12.wl: bulk spin for sigma_2 quasihole.

spin-1drev-lx=22-m=1-Ne=300-qhtype=3_0_0-cutoff=12.wl: bulk spin for Laughlin quasihole.

spin-1drev-lx=22-m=1-Ne=300-qhtype=2_4_0-cutoff=12.wl: bulk spin for psi_1 quasihole.

spin-1drev-lx=22-m=1-Ne=300-qhtype=3_0_2-cutoff=12.wl: bulk spin for epsilon quasihole.

spin-1drev-lx=22-m=1-Ne=300-qhtype=4_-4_0-cutoff=12.wl: bulk spin for psi_2 quasihole.

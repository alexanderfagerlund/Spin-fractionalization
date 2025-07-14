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

### Computation programs: 

edgeSpinPlot.nb: used to compute bulk and edge spins for Fig. 1.

Datagen_edgespin_paper.nb: used to compute edge spins for Fig. 2.

q-j-vs-tau-modified-2.nb: used to compute bulk spins for Fig. 2.

### MPS data used in the above programs:



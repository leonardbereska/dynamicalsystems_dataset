# Dynamical systems datasets
Datasets and generation code for Lotka-Volterra, Gray-Scott and Navier-Stokes equations.

This repository contains generated data from three dynamical systems:
- Navier-Stokes (NV)
- Gray-Scott (GS)
- Lotka-Volterra (LV)
 
The code for generation is taken (and adapted) from https://github.com/yuan-yin/LEADS based on the paper:
Yin, Yuan, Ibrahim Ayed, Emmanuel de Bézenac, Nicolas Baskiotis, and Patrick Gallinari. “LEADS: Learning Dynamical Systems That Generalize Across Environments.” ArXiv:2106.04546 [Cs, Stat], June 8, 2021. http://arxiv.org/abs/2106.04546.
 

For each dynamical system, we sample different 'environments', namely, different parameter values.
By default, we sample 100 trajectories of length (number of time steps) 20 for each environment (parameter setting).


The Navier-Stokes system has 32 x 32 spatial dimensions, and by default 4 environments.
The Gray-Scott system has 32 x 32 spatial dimensions with 2 dimensions at each coordinate. The second coordinate seems to be just one minus the first coordinate (e.g. first coordinate 0.95 and second 0.05). By default, GS has 3 environments.
The Lotka-Volterra system has 2 dimensions, and by default 10 environments. 

In summary, 100 trajectories, 20 time steps each, 4/3/10 (NS/GS/LV) environments, with 32x32/32x32x2/2 dimensions (NS/GS/LV):
- Navier-Stokes dataset: `ns.pt`: `torch.Size([100, 4, 1, 20, 32, 32])`
- Gray-Scott dataset: `gs.pt`: `torch.Size([100, 3, 2, 20, 32, 32])`
- Lotka-Volterra dataset: `lv.pt`: `torch.Size([100, 10, 2, 20])`

The datasets can be loaded from pytorch files via, e.g., `tc.load('ns.pt')`.
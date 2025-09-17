

# TMCM-CdCl3-Piezoelectricity

>This repository contains all calculations, data, and model files related to the study of the piezoelectric properties of TMCM-CdCl₃, as described in [arXiv:2507.15687]. It includes first-principles (DFT) calculations, molecular dynamics simulations, and machine learning models.

## Folder Structure

- **database/**
	- Raw data for training and testing.
	- **dipole_model/**: Data for the dipole moment model, including `input.json` (input parameters) and `train.zip` (training data).
	- **force_model/**: Data for the force field model, including `input.json` (input parameters) and `database.zip` (database file).

- **model/**
	- Trained machine learning model files.
	- `dipole_model.pb`: Dipole moment prediction model.
	- `force_model.pb`: Force field prediction model.

- **DFT/**
	- Files and scripts for first-principles (DFT) calculations.
	- `INPUT.scf`: Input file for DFT calculations.
	- `pos2stru.py`: Script for structure conversion.

- **LAMMPS/**
	- Files for LAMMPS molecular dynamics simulations.
	- `01-eq.lammps`: Script of NPT simulation.
	- `02-apply-strain.lammps`: Script for applying strain.
	- `03-calculate-P.lammps`: Script for calculating polarization use machine learning potential.
	- `calc_d15.ipynb`: Jupyter notebook for d15 piezoelectric coefficient calculation.

## Wiki

We have also made a public wiki that explains how to calculate the piezoelectric tensor at finite temperature:
https://liutheorylab.github.io/Tutorial/MD_piezoelectric_tensor/

## Other Notices

To calculate the bond vector for TMCM molecules, we developed a custom LAMMPS plugin, which is open source at:
https://github.com/MoseyQAQ/ferrodispcalc

This package provides:
1. Fast neighbor list construction.
2. Calculation of polarization or displacement for ferroelectrics (supports LAMMPS plugin for real-time access in LAMMPS).
3. Post-processing tools, e.g., plotting dipole orientation in real space.

## Citation

```
@article{li2025giant,
  title={Giant Reversible Piezoelectricity from Symmetry-Governed Stochastic Dipole Hopping},
  author={Li, Denan and Ni, Haofei and Zhang, Yi and Liu, Shi},
  journal={arXiv preprint arXiv:2507.15687},
  year={2025}
}
```
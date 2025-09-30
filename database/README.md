# Details about the training database

(a) __Phases of TMCM-CdCl<sub>3</sub>  included in the training set:__ Our training set was designed to capture the key physical characteristic of TMCM-CdCl<sub>3</sub>, the pronounced rotational flexibility of the TMCM<sup>+</sup> molecular cations. To this end, in addition to including the well-defined ferroelectric phase (space group $Cc$), the database is primarily composed of configurations sampled from extensive finite-temperature MD simulations conducted at temperatures up to 450 K, representing snapshots of a dynamically disordered system under various thermodynamic conditions. By training on this diverse ensemble of structures, the DP model effectively learns the potential energy surface associated with the rotational degrees of freedom of the cations. 

(b) All training configurations were generated using the 84-atom primitive unit cell of the ferroelectric phase, which already has relatively large dimensions ($a \approx 9$ Å$, $b \approx 17$ Å, $c \approx 7$ Å). 

(c) __The sampled temperature and pressure conditions:__ Most configurations were sampled from MD simulations performed over a broad range of thermodynamic conditions, including temperatures of 200, 250, 300, 350, 400, and 450~K, and pressures of $-3$, $-2$, 0, 2, and 5~kbar.

(d) __The distribution of configurations across different structural motifs:__ The orientation of the TMCM<sup>+</sup> cations is the most critical structural motif in the system. To demonstrate the diversity of our training set, we analyzed the distribution of the N--Cl bond vector orientation, as shown in the figure below. The distributions of the polar angle $\theta$ and azimuthal angle $\phi$ confirm that the training set spans the full 180-degree range for $\theta$ and 360-degree for $\phi$. This broad angular coverage allows the DP model to accurately capture the full 3D rotational energy surface of the molecular cations.

<div align="center">
<img src="https://github.com/MoseyQAQ/TMCM-CdCl3-Piezoelectricity/blob/main/database/angle_distribution.png?raw=true" alt="Angle distribution" width="800">
</div>

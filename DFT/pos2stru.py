from ase.io import read, write 
import sys

input_file = 'POSCAR'
output_file = 'STRU'

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
elif len(sys.argv) == 2:
    input_file = sys.argv[1]
else:
    print("Usage: pos2stru.py POSCAR STRU")
    exit(1)

pp = {
    "Cd": "Cd_ONCV_PBE-1.0.upf",
    "Cl": "Cl_ONCV_PBE-1.0.upf",
    "N": "N_ONCV_PBE-1.0.upf",
    "C" : "C_ONCV_PBE-1.0.upf",
    "H" : "H_ONCV_PBE-1.0.upf",
}

basis = {
    "Cd": "Cd_gga_10au_100Ry_4s2p2d1f.orb",
    "Cl": "Cl_gga_10au_100Ry_2s2p1d.orb",
    "N": "N_gga_10au_100Ry_2s2p1d.orb",
    "C" : "C_gga_10au_100Ry_2s2p1d.orb",
    "H" : "H_gga_10au_100Ry_2s1p.orb",
}

atoms = read(input_file, format='vasp')
write(output_file,
      atoms,
      format='abacus',
      pp=pp,
      basis=basis)

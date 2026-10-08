import math

# Human A2A Adenosine Receptor (PDB: 4EIY) binding pocket key residues and coordinates
# Coordinates extracted from experimental 4EIY crystal structure (orthosteric pocket)
POCKET_RESIDUES = {
    "PHE168": {"atom": "CZ", "x": -1.25, "y": 23.40, "z": 8.12, "type": "aromatic_ring"},
    "ASN253": {"atom": "ND2", "x": -4.10, "y": 21.80, "z": 6.50, "type": "hbond_donor"},
    "GLU169": {"atom": "OE1", "x": -2.80, "y": 25.10, "z": 9.30, "type": "hbond_acceptor"},
    "LEU249": {"atom": "CD1", "x": -5.30, "y": 24.00, "z": 5.20, "type": "hydrophobic"},
    "ILE274": {"atom": "CD1", "x": -0.80, "y": 20.50, "z": 7.40, "type": "hydrophobic"},
    "TRP246": {"atom": "CH2", "x": -6.20, "y": 21.00, "z": 7.80, "type": "aromatic_ring"},
}

# Ligand test compounds
# SMILES, molecular weight, H-bond donors/acceptors, and experimental/theoretical affinity
COMPOUNDS = {
    "Caffeine (Coffee)": {
        "formula": "C8H10N4O2",
        "mw": 194.19,
        "rings": ["xanthine_core"],
        "hbond_donors": 0,
        "hbond_acceptors": 4, # 2 carbonyl O, 2 imidazole/pyrimidine N
        "logP": -0.07,
        "desc": "Non-selective adenosine receptor antagonist. Lacks ribose sugar."
    },
    "Theophylline (Tea)": {
        "formula": "C7H8N4O2",
        "mw": 180.16,
        "rings": ["xanthine_core"],
        "hbond_donors": 1, # N7-H donor
        "hbond_acceptors": 3,
        "logP": -0.02,
        "desc": "Natural xanthine found in tea leaves. Stronger bronchodilator than caffeine."
    },
    "Theobromine (Chocolate)": {
        "formula": "C7H8N4O2",
        "mw": 180.16,
        "rings": ["xanthine_core"],
        "hbond_donors": 1, # N1-H donor
        "hbond_acceptors": 3,
        "logP": -0.78,
        "desc": "Primary alkaloid in cocoa beans. Weaker central nervous system stimulant."
    },
    "ZM241385 (Synthetic Antagonist in 4EIY)": {
        "formula": "C16H18N8O2",
        "mw": 354.37,
        "rings": ["triazolotriazine", "phenol"],
        "hbond_donors": 3,
        "hbond_acceptors": 5,
        "logP": 1.25,
        "desc": "High-affinity sub-nanomolar clinical antagonist crystallized in 4EIY."
    },
    "Adenosine (Natural Ligand)": {
        "formula": "C10H13N5O4",
        "mw": 267.24,
        "rings": ["adenine", "ribose"],
        "hbond_donors": 4,
        "hbond_acceptors": 6,
        "logP": -1.05,
        "desc": "Endogenous full agonist. Triggers G-protein conformational shift."
    }
}

print("Pocket model & ligands initialized!")

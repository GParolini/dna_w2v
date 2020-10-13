#!/usr/bin/env python

from dna2vec.multi_k_model import MultiKModel
from itertools import combinations


filepath = 'pretrained/dna2vec-20161219-0153-k3to8-100d-10c-29320Mbp-sliding-Xat.w2v'
mk_model = MultiKModel(filepath)


dna_genetic_code_dict = {'Phe': ['TTT','TTC'],'Leu': ['TTA', 'TTG','CTT', 'CTC','CTA','CTG'],'Ile':['ATT', 'ATC','ATA'], "Met": ["ATG"], 'Val': ['GTT', 'GTC', 'GTA', 'GTG'], "Ser": ["TCT", "TCC", "TCA", "TCG"], "Pro":["CCT", "CCC", "CCA", "CCG"], "Thr": ["ACT", "ACC", "ACA", "ACG"], "Ala": ["GCT", "GCC", "GCA", "GCG"], "Tyr": ["TAT", "TAC"], "STOP": ["TAA", "TAG", "TGA"], "His": ["CAT", "CAC"], "Gln": ["CAA", "CAG"], "Asn": ["AAT", "AAC"], "Lys": ["AAA", "AAG"], "Asp": ["GAT", "GAC"], "Glu": ["GAA", "GAG"], "Cys": ["TGT", "TGC"], "Trp": ["TGG"], "Arg": ["CGT", "CGC", "CGA", "CGG"], "Ser": ["AGT", "AGC"], "Arg": ["AGA", "AGG"], "Gly": ["GGT", "GGC", "GGA", "GGG"]}

am_dict = {'Phe': "Phenylalanine", 'Leu':"Leucine" , 'Ile': "Isoleucine", "Met": "Methionine", 'Val': "Valine", "Ser": "Serine", "Pro":"Proline" , "Thr": "Threonine", "Ala": "Alanine", "Tyr": "Tyrosine", "STOP": "STOP", "His": "Histidine", "Gln": "Glutamine", "Asn": "Asparagine", "Lys":"Lysine" , "Asp": "Aspartic acid" , "Glu": "Glutamic acid", "Cys": "Cysteine", "Trp": "Tryptophan", "Arg": "Arginine", "Ser": "Serine", "Arg": "Arginine", "Gly":"Glycine" }


for key in dna_genetic_code_dict.keys():
    print("\n")
    print(am_dict[key])
    for value in dna_genetic_code_dict[key]:
        print(mk_model.vector(value))


for key in dna_genetic_code_dict.keys():
    print("\n")
    print(am_dict[key])
    my_list = list(combinations(dna_genetic_code_dict[key], 2))
    print(my_list)
    if len(my_list)>=1:
        for el in my_list:
            print(el[0], el[1],mk_model.cosine_distance(el[0], el[1]))




#print(mk_model.cosine_distance('TTT', 'TTC'))

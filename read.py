#!/usr/bin/env python

from dna2vec.multi_k_model import MultiKModel

filepath = 'results/dna2vec-20200829-2236-k3to8-100d-10c-470Mbp-sliding-OTM.w2v'
mk_model = MultiKModel(filepath)


print(mk_model.vector('AAA'))
print(mk_model.vector('AAAAA'))
print(mk_model.vector('TTTTT'))


print(mk_model.cosine_distance('AAA', 'AAA'))
print(mk_model.cosine_distance('AAA', 'AAAAA'))
print(mk_model.cosine_distance('AAA', 'TTTTT'))
print(mk_model.cosine_distance('AAAAA', 'TTTTT'))

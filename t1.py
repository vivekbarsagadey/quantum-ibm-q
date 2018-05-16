"""
Example used in the readme. In this example a Bell state is made
"""
import sys
import os
from pprint import pprint
from qiskit import QuantumProgram
import Qconfig

qp = QuantumProgram()
qp.set_api('a2c1e632e1d80403ae002b7fde0fb7dfe4afd5a4093292c24c75a65060ed81c16644cf1d7a5b5a4075c08e3530ee8e125d0405b910e73ee79d2441c990145be4', 'https://quantumexperience.ng.bluemix.net/api') # set the APIToken and API url
# set up registers and program
qr = qp.create_quantum_register('qr', 16)
cr = qp.create_classical_register('cr', 16)
qc = qp.create_circuit('my_test', [qr], [cr])

# rightmost eight (qu)bits have ')' = 00101001
qc.x(qr[0])
qc.x(qr[3])
qc.x(qr[5])

# second eight (qu)bits have ysuperposition of
# '8' = 00111000
# ';' = 00111011
# these differ only on the rightmost two bits
qc.h(qr[9]) # create superposition on 9
qc.cx(qr[9],qr[8]) # spread it to 8 with a cnot
qc.x(qr[11])
qc.x(qr[12])
qc.x(qr[13])

qc.barrier(qr)
# measure
for j in range(16):
    qc.measure(qr[j], cr[j])

# run and get results
results = qp.execute(["my_test"], backend='ibmqx5', shots=1024 , timeout=500)
print("results >>> ",results)
stats = results.get_counts("my_test")
print("Experiment end ....")
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
qr = qp.create_quantum_register('qr', 1)
cr = qp.create_classical_register('cr', 1)
qc = qp.create_circuit('my_test', [qr], [cr])

qc.x(qr[0])
#qc.y(qr[0])
#qc.z(qr[0])

qc.h(qr[0])



qc.barrier(qr)
# measure
for j in range(1):
    qc.measure(qr[j], cr[j])

# run and get results
#results = qp.execute(["my_test"], backend='ibmqx5', shots=1024 , timeout=500)
results = qp.execute(["my_test"], backend='ibmqx_qasm_simulator', wait=2 , timeout=500)
print("results >>> ",results)
stats = results.get_counts("my_test")
print("stats ....",stats)
out = results.get_ran_qasm('my_test')
print("out ....",out)
print("Get data " ,results.get_data('my_test'))
print("Experiment end ....")
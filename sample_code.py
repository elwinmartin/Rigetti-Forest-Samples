## Adapted from Rigetti's documentation

# Program is the object that will contain our experiment
from pyquil.quil import Program 
# QVM 
from pyquil.api import QVMConnection 
from pyquil.gates import H, CNOT, MEASURE 
# Instantiating a new qvm instance 
qvm = QVMConnection() 
# Our program p requires 2 qubits, labeled 0 & 1
p = Program(H(0), CNOT(0, 1), MEASURE(0, 0), MEASURE(1, 1)) 
results = qvm.run(p, classical_addresses=[0, 1], trials=10)

# Seeing the results is nice! 
# There are ten trials so this should return an array such that len(results) === 10.
print(results)
# [[1,1], [1,1], [1,1], [0,0], [1,1], [1,1], [1,1], [1,1], [1,1], [1,1]]

# There's also a wavefunction representation of the program from the qvm.
wavefunction = qvm.wavefunction(p)
print(wavefunction)
# (1+0j)|11>

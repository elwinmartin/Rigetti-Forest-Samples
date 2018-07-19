## Adapted from Rigetti's documentation

# Program is the object that will contain our experiment
from pyquil.quil import Program 
# QVM 
from pyquil.api import QVMConnection 
from pyquil.gates import Z, H, CNOT, MEASURE 
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

## Large qubit count test
p30 = Program(
  Z(0), 
  Z(1),
  Z(2),
  Z(3),
  Z(4),
  Z(5),
  Z(6),
  Z(7),
  Z(8),
  Z(9),
  Z(10),
  Z(11),
  Z(12),
  Z(13),
  Z(14),
  Z(15),
  Z(16),
  Z(17),
  Z(18),
  Z(19),
  Z(20),
  Z(21),
  Z(22),
  Z(23),
  Z(24),
  Z(25),
  Z(26),
  Z(27),
  Z(28),
  Z(29),
  MEASURE(0,0), 
  MEASURE(1,1),
  MEASURE(2,2),
  MEASURE(3,3),
  MEASURE(4,4),
  MEASURE(5,5),
  MEASURE(6,6),
  MEASURE(7,7),
  MEASURE(8,8),
  MEASURE(9,9),
  MEASURE(10,10),
  MEASURE(11,11),
  MEASURE(12,12),
  MEASURE(13,13),
  MEASURE(14,14),
  MEASURE(15,15),
  MEASURE(16,16),
  MEASURE(17,17),
  MEASURE(18,18),
  MEASURE(19,19),
  MEASURE(20,20),
  MEASURE(21,21),
  MEASURE(22,22),
  MEASURE(23,23),
  MEASURE(24,24),
  MEASURE(25,25),
  MEASURE(26,26),
  MEASURE(27,27),
  MEASURE(28,28),
  MEASURE(29,29)
)
results30 = qvm.run(p30, classical_addresses=[0..29], trials=1)
'''
pyquil.api.errors.TooManyQubitsError: 30 qubits were requested, but the QVM is limited to 19 qubits.

You requested too many qubits on the QVM. More qubits are available when you use
the queue. Pass the use_queue parameter to QVMConnection to enable additional
qubits (however, each program will take longer to run). For example:

    qvm = QVMConnection(use_queue=True)
    qvm.run(twenty_qubit_program)

See https://go.rigetti.com/connections for more info.
'''
# Funny since the docs say "Most API keys give access to the QVM with up to 30 qubits."

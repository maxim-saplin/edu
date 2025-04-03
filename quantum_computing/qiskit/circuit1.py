from qiskit import QuantumCircuit


qc = QuantumCircuit(3)
#Construct using hard-wired code
qc.reset(0)
qc.reset(1)
qc.reset(2)
qc.h(0)
qc.cx(0,1)
qc.cx(0,2)
qc.measure_all()
qc.draw(output="mpl")
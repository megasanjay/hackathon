from neurondm import *

config = Config()

n = Neuron(Phenotype("TEMP:myPhenotype"))

config.write()
config.write_python()

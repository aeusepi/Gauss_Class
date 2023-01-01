from distrib_ae import Gaussian
from distrib_ae import Binomial

import distrib_ae as ds

print(ds.__file__)


gauss = Gaussian(10,5)
bino = Binomial(0.5,30)

print(gauss)
print(bino.calculate_mean())
print(bino.calculate_stdev())


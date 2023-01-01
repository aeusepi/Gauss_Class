from distributions import Gaussian
from distributions import Binomial

import distributions as ds

print(ds.__file__)


gauss = Gaussian(10,5)
bino = Binomial(0.5,30)

print(gauss)
print(bino.calculate_mean())
print(bino.calculate_stdev())


import numpy
import pandas
from sklearn.preprocessing import StandardScaler

def genearate_data(data_size=1000) -> pandas.DataFrame:
    numpy.random.seed(42) # For reproducibility
    speed = numpy.random.uniform(0, 100, data_size) # Speed in km/h
    mass = numpy.random.uniform(0, 1000, data_size) # Mass in kg
    energy = 0.5 * mass * speed**2
    momentum = mass * speed
    data = numpy.column_stack((speed, mass, momentum, energy))
    return _wrap_in_df(data)

def _wrap_in_df(numpy_data):
    return pandas.DataFrame(numpy_data, columns=['Speed', 'Mass', 'Momentum', 'Energy'], )

def scaled_data(data_size=1000) -> pandas.DataFrame:
    return _wrap_in_df(StandardScaler().fit_transform(genearate_data(data_size)))


print("Data generation functions compiled")
d = scaled_data()
print("data generation executed")
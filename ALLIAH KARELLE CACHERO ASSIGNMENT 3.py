import numpy as np

#QUESTION 1

#EXAMPLE 1.1
complex_array = np.array([7+8j, 9+10j, 11+12j])
np.save('complex_array.npy', complex_array)

#EXAMPLE 1.2
random_int_array = np.random.randint(100, 200, size=(10,))
random_int_array.tofile('random_int_array.bin')

#EXAMPLE 1.3
structured_array = np.array([(3, 'Charlie', 45.2), (4, 'David', 55.8)],
                            dtype=[('id', 'i4'), ('name', 'U10'), ('score', 'f4')])
np.savetxt('structured_array.csv', structured_array, delimiter=',', fmt=['%d', '%s', '%.2f'])

#QUESTION 2

#EXAMPLE 2.1
loaded_complex_array = np.load('complex_array.npy')
print("Loaded complex array:")
print(loaded_complex_array)

#EXAMPLE 2.2
loaded_random_int_array = np.fromfile('random_int_array.bin', dtype=int)
print("Loaded random integer array:")
print(loaded_random_int_array)

#EXAMPLE 2.3
loaded_structured_array = np.genfromtxt('structured_array.csv', delimiter=',', dtype=[('id', 'i4'), ('name', 'U10'), ('score', 'f4')])
print("Loaded structured array:")
print(loaded_structured_array)
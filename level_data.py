import pickle



level = 1
pickle_in = open('Cyber_level1_data', 'rb')
world_data = pickle.load(pickle_in)

pickle_in2 = open('Cyber_level2_data', 'rb')
world2_data = pickle.load(pickle_in2)

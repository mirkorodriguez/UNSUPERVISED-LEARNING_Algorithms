import math
from collections import defaultdict

dataset = [[1, 1, 0, 0],
           [0, 0, 0, 1],
           [1, 0, 0, 0],
           [0, 0, 1, 1]]

print("\ndataset:",dataset)

sigma=0.3
lr = 0.6
epocas=100


from minisom import MiniSom
som = MiniSom(x = 1, y = 2, input_len = 4, sigma = sigma, learning_rate = lr) # initialization of 1x2 SOM
som.random_weights_init(dataset) # initialize the weights in a data driven fashion
som.train_batch(dataset, epocas) # trains the SOM with 100 iterations

print ("\nGrupos ganadores:")
for i, x in enumerate(dataset):
    winner = som.winner(x)
    print ("Data["+str(i)+"]:", x," pertenece al Grupo ", winner) 

print ("\nMapa de ganadores:")
mappings = som.win_map(dataset)
for k, v in mappings.items():
    print(f'{k} - {v}')
   

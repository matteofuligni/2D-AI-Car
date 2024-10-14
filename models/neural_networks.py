# Definizione della rete neurale (costruzione e forward pass)

import tensorflow as tf 
from keras import layers, models 

class NeuralNewtwok:
    def __init__(self, input_size, output_size, hidden_layers=[32, 32]):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_layers = hidden_layers
        
        self.model = self.build_model(self.input_size, self.output_size, self.hidden_layers)
        
    
# Definizione della rete neurale (costruzione e forward pass)

import tensorflow as tf 
from keras import layers, models 

class NeuralNewtwok:
    def __init__(self, input_size, output_size, hidden_layers=[32, 32]):
        # self.input_size = input_size
        # self.output_size = output_size
        # self.hidden_layers = hidden_layers
        
        # self.model = self.build_model(self.input_size, self.output_size, self.hidden_layers)
        self.model = self.build_model(input_size, output_size, hidden_layers)
        
    def build_model(self, input_size, output_size, hidden_layers):
        model = models.Sequential()
        model.add(layers.InputLayer(shape=(input_size,)))
        
        for layer in hidden_layers:
            model.add(layers.Dense(layer, activation='relu'))
            
        model.add(layers.Dense(output_size, activation='linear'))
        
        model.compile(optimizer='adam', loss='mean_squared_error')
        
        return model
    
    def predict(self, inputs):
        return self.model.predict(inputs)
    
    def train(self, x_train, y_train, epochs=10):
        self.model.fit(x_train, y_train, epochs=epochs)
        
    def save_model(self, filepath):
        self.model.save(filepath)
        
    def load_model(self, filepath):
        self.model.load(filepath)
        

#modello = NeuralNewtwok(5, 2, hidden_layers=[64, 64])

#print(modello)
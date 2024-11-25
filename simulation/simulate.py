# Simulazione complessiva (inizializza automobili, applica reti neurali, simula movimento)

from ..models.neural_networks import NeuralNetwork
from config.config import input_size, output_size, hidden_layers

def simulate():
    # Crea una rete neurale per ogni macchina
    nn = NeuralNetwork(input_size, output_size, hidden_layers)
    
    # Dati fittizi per testare la rete (posizione auto, velocità, ostacoli, ecc.)
    input_data = [0.1, 0.5, 0.2, 0.3, 0.7]
    
    # Esegui una predizione
    output_data = nn.predict([input_data])
    
    print(f"Output della rete neurale: {output_data}")

if __name__ == "__main__":
    simulate()


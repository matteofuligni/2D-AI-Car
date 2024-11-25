# Configurazioni e parametri principali (ipermetri, setup genetico, parametri della rete)

# Configurazione per la rete neurale
input_size = 5  # Numero di input (es. posizione auto, distanza da ostacoli, ecc.)
output_size = 2  # Numero di output (es. sterzata, accelerazione)
hidden_layers = [64, 64]  # Struttura della rete (2 strati nascosti con 64 neuroni ciascuno)

# Parametri dell'algoritmo genetico
population_size = 50  # Dimensione della popolazione
mutation_rate = 0.1  # Tasso di mutazione
crossover_rate = 0.5  # Tasso di crossover

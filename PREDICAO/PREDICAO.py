# -*- coding: utf-8 -*-
"""Cópia de LSTM_Publicações.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Uqf51T3mibShCPx_luz29juXsr4EBgwG
"""

#Pacotes para rede neural
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model

df = pd.read_csv('dados_processados_encoded.csv')

#@title Treinando o Tokenizador que irá transformar Palavras em Vetores
top_words = 5000
tokenizer = Tokenizer(num_words=top_words)
tokenizer.fit_on_texts(df['texto'])
max_review_length = 50

"""###Predições"""

# Função para pré-processamento e vetorização do texto
def preprocess_text(text, tokenizer, max_sequence_length):
    # Tokenização do texto
    tokenized_text = tokenizer.texts_to_sequences([text])

    # Padding para garantir que todas as sequências tenham o mesmo comprimento
    padded_text = pad_sequences(tokenized_text, maxlen=max_sequence_length, padding='post')

    # Retorne o texto pré-processado e vetorizado
    return padded_text

# Função para fazer previsões com o modelo
def predict_class(model, text, tokenizer, max_sequence_length):
    # Pré-processar e vetorizar o texto
    processed_text = preprocess_text(text, tokenizer, max_sequence_length)

    # Fazer previsões usando o modelo
    predictions = model.predict(processed_text)

    # Decodificar as previsões em rótulos de classe (se necessário)
    # Por exemplo, você pode ter um dicionário que mapeia índices de previsão para rótulos de classe
    predicted_class = np.argmax(predictions, axis=1)

    # Retorne a classe prevista
    return predicted_class

model = load_model('modelo_lstm.h5')
# Texto de exemplo para fazer previsões
input_text ='Audiência Una (Telepresencial) Designada(Agendada para 21 de Fevereiro de 2024 às 16:10 h)'

# Fazer previsão com o texto de exemplo
predicted_class = predict_class(model, input_text, tokenizer, max_review_length)


# Exibir a classe prevista
if predicted_class == 0:
  print("Classe prevista: Acordao")
elif predicted_class == 1:
  print("Classe prevista: Audiencia")
else:
  # Add an else statement to handle any other potential values of predicted_class
  pass
  print("Classe prevista: Sentença")
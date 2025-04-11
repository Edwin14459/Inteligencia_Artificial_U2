import numpy as np  # Importamos la librería numpy (aunque no se usa en este código)

# Definir probabilidades iniciales de spam y no spam
prob_spam = 0.4     # Probabilidad de que un mensaje sea spam
prob_no_spam = 0.6  # Probabilidad de que un mensaje no sea spam

# Diccionario con palabras clave y sus probabilidades condicionales
# Cada palabra tiene una tupla con (P(palabra|spam), P(palabra|no spam))
diccionario_palabras = {
    "oferta": (0.8, 0.2),  
    "gratis": (0.7, 0.1),
    "urgente": (0.6, 0.3),
    "Hola": (0.9, 0.1)
}

# Función para calcular la probabilidad de que un mensaje sea spam usando el teorema de Bayes
def calcular_probabilidad_spam(palabras):
    prob_spam_dado_palabras = prob_spam  
    prob_no_spam_dado_palabras = prob_no_spam  
    
    # Iteramos sobre cada palabra en el mensaje
    for palabra in palabras:
        if palabra in diccionario_palabras:  
            prob_palabra_dado_spam, prob_palabra_dado_no_spam = diccionario_palabras[palabra]
            prob_spam_dado_palabras *= prob_palabra_dado_spam  
            prob_no_spam_dado_palabras *= prob_palabra_dado_no_spam  
    
    # Aplicamos el teorema de Bayes para calcular la probabilidad final
    prob_total = prob_spam_dado_palabras + prob_no_spam_dado_palabras
    prob_spam_final = prob_spam_dado_palabras / prob_total if prob_total > 0 else 0  
    
    return prob_spam_final  # Retornamos la probabilidad final de spam

# Lista de mensajes de prueba
mensajes = ["oferta", "gratis", "urgente", "Hola"]

# Función para mostrar la probabilidad de spam en un formato más legible
def mostrar_probabilidades(mensajes):
    for mensaje in mensajes:
        probabilidad = calcular_probabilidad_spam([mensaje]) 
        porcentaje = probabilidad * 100  
        decision = "Spam" if probabilidad >= 0.5 else "No es spam"  
        
        # Mostramos los resultados en pantalla
        print(f"Mensaje: {mensaje}")
        print(f"Probabilidad de spam: {probabilidad:.4f}")
        print(f"Porcentaje de spam: {porcentaje:.2f}%")
        print(f"Predicción: {decision}\n")

# Llamamos a la función para mostrar los resultados
mostrar_probabilidades(mensajes)


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Datos
textos = [
    "Me encanta dormir", 
    "Odio hacer tareas", 
    "Me gusta fascinante",
    "No me gusta el tráfico", 
    "Scikit-learn es genial", 
    "El clima es hermoso",
    "No soporto esperar", 
    "Python es versátil", 
    "Las matemáticas son interesantes",
    "Detesto madrugar"
]
labels = [1, 0, 1, 0, 1, 1, 0, 1, 1, 0]  # 1 = positivo, 0 = negativo

# Vectorización ve el modelo 
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(textos)

# Entrenar modelo Se entrena un modelo Naive Bayes con frases etiquetadas.
modelo = MultinomialNB()
modelo.fit(X, labels)

# Función de predicción Se entrena el modelo con datos de sentimiento positivo y negativo.
def predecir_sentimiento(texto):
    texto_vectorizado = vectorizer.transform([texto])
    prediccion = "Positivo" if modelo.predict(texto_vectorizado)[0] == 1 else "Negativo"
    return f"{texto}: {prediccion}"

# Prueba Se hace una función para predecir el sentimiento de nuevas frases.
print(predecir_sentimiento("Me gusta aprender"))
print(predecir_sentimiento("Odio los lunes")) 


import numpy as np
import re

# Paso 1: Dataset de Reglamento Estudiantil (10 artículos)
articulos_reglamento = [
    "ARTÍCULO 3: El número de créditos de cada asignatura es determinado por elConsejo Académico, previo estudio del Comité de Currículo del Programa.",
    "ARTÍCULO 4: El número de créditos académicos de una actividad circunscrita en el plan de estudios será aquel que resulte de dividir por 48 el número total de horas que deba emplear el estudiante para cumplir satisfactoriamente los resultados del aprendizaje",
    "ARTÍCULO 5: La Institución, dentro de su autonomía y de acuerdo con la naturaleza del programa, distinguirá entre créditos académicos obligatorios y electivos.",
    "ARTÍCULO 6: El Consejo Académico podrá adoptar diferentes períodos calendario bimestre, trimestre, semestre, anualidad u otro) para el desarrollo de los programas académicos.",
    "ARTÍCULO 10: La Institución se reserva el derecho de seleccionar a los estudiantes para cada cohorte, de acuerdo con los criterios fijados por el Consejo Académico y en ningún caso discrimina por razones de edad, religión, nacionalidad, ideas políticas, raza, sexo o estado civil.",
    "ARTÍCULO 13: Los aspirantes que no sean admitidos o que habiéndolo sido no se matriculen, así como aquellos que se retiren definitivamente, pueden retirar sus documentos en el Departamento de Registro Académico, previa solicitud escrita.",
    "ARTÍCULO 15: Una vez culminado el proceso de admisión, el Departamento de Promoción y Divulgación informa los resultados del proceso al aspirante.",
    "ARTÍCULO 17: Los resultados del proceso de admisión en cada una de las pruebas y procedimientos desarrollados, son de reserva institucional y en ningún caso se comunican a los interesados ni a terceras personas.",
    "ARTÍCULO 18: Los aspirantes extranjeros están sujetos a los mismos requisitos de inscripción y matrícula exigidos para los aspirantes colombianos, de acuerdo con las leyes vigentes.",
    "ARTÍCULO 19: Se entiende por transferente al aspirante que, habiendo cursado estudios superiores en otra institución debidamente reconocida por el Estado, es aceptado como estudiante regular en uno de los programas académicos de la Institución.",
]

def limpiar_texto(texto):
    """Limpia el texto: minúsculas y elimina caracteres especiales."""
    return re.sub(r'[^\w\s]', '', texto.lower())

def calcular_tf(termino, documento):
    """TF = frecuencia_palabra / total_palabras_doc"""
    palabras = limpiar_texto(documento).split()
    if not palabras: return 0
    return palabras.count(termino) / len(palabras)

def calcular_idf(termino, todos_documentos):
    """IDF = log(Total_Docs / Docs_con_la_palabra)"""
    N = len(todos_documentos)
    df = sum(1 for doc in todos_documentos if termino in limpiar_texto(doc).split())
    # Usamos validación simple para evitar división por cero
    if df == 0: return 0
    return np.log(N / df)

def buscar(consulta, documentos):
    """Busca una frase y calcula el score final sumando el TF-IDF de cada palabra."""
    palabras_consulta = limpiar_texto(consulta).split()
    resultados = []
    
    # Pre-calcular IDF para cada palabra de la consulta
    idfs = {palabra: calcular_idf(palabra, documentos) for palabra in palabras_consulta}
    
    for i, doc in enumerate(documentos):
        score_total = 0
        for palabra in palabras_consulta:
            tf = calcular_tf(palabra, doc)
            score_total += tf * idfs.get(palabra, 0)
            
        resultados.append({
            "id": i + 1,
            "contenido": doc,
            "score": score_total
        })
    
    # Ordenar por relevancia (score)
    return sorted(resultados, key=lambda x: x['score'], reverse=True)

# --- Ejecución del Motor ---
if __name__ == "__main__":
    print("-" * 50)
    print("   MOTOR DE BÚSQUEDA - FUNDACIÓN UNIVERSITARIA KONRAD LORENZ")
    print("-" * 50)
    query = input("¿Qué artículo del reglamento buscas?: ")
    
    ranking = buscar(query, articulos_reglamento)
    
    print(f"\nResultados para: '{query}'")
    print("=" * 50)
    
    encontrado = False
    for i, res in enumerate(ranking, 1):
        if res['score'] > 0:
            print(f"{i}. [Score: {res['score']:.4f}] {res['contenido']}")
            encontrado = True
    
    if not encontrado:
        print("No se encontraron artículos con esos términos. Intenta con: 'beca', 'fraude' o 'matrícula'.")
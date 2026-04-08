# Motor de Búsqueda Académico: Índices Invertidos y TF-IDF

Este proyecto implementa un motor de búsqueda simplificado diseñado para procesar y recuperar información relevante de reglamentos estudiantiles. Se centra en el uso de la métrica **TF-IDF (Term Frequency - Inverse Document Frequency)** para priorizar la relevancia de los resultados.

## 📌 Descripción del Proyecto

Para este ejercicio práctico, se han seleccionado **10 artículos clave del Reglamento Académico de la Fundación Universitaria Konrad Lorenz**. Estos fragmentos cubren temas críticos como becas de excelencia, faltas disciplinarias, procesos de matrícula y cancelaciones.

El objetivo es permitir que un usuario realice consultas en lenguaje natural y reciba una lista de artículos ordenados de mayor a menor relevancia, simulando el comportamiento de un motor de búsqueda profesional.

## 🚀 ¿Por qué usar Índices Invertidos (TF-IDF) en lugar de Búsqueda Simple?

En una búsqueda simple (secuencial), el sistema escanea cada palabra de cada documento cada vez que se hace una consulta. Esto presenta dos problemas principales:

1.  **Eficiencia**: A medida que el número de documentos crece, el escaneo secuencial se vuelve extremadamente lento. Los índices invertidos permiten ir directamente a los documentos que contienen la palabra, eliminando la necesidad de leer todo el dataset.
2.  **Relevancia (Ranking)**: Una búsqueda simple trata todas las palabras por igual. **TF-IDF** es superior porque:
    *   **TF (Term Frequency)**: Premia a los documentos que mencionan más veces el término buscado.
    *   **IDF (Inverse Document Frequency)**: Penaliza palabras muy comunes (como "el", "la", "de") que no aportan valor semántico, y premia términos específicos (como "fraude", "beca" o "supletorio"), asegurando que los resultados sean realmente útiles.

## 🛠️ Instrucciones de Ejecución

Sigue estos pasos para configurar y ejecutar el motor de búsqueda en tu entorno local:

### 1. Activar el entorno virtual
Asegúrate de estar en la carpeta del proyecto y ejecuta:
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar dependencias
Si aún no tienes las librerías necesarias, instálalas con:
```powershell
pip install numpy
```

### 3. Ejecutar el motor
Lanza el script principal de Python:
```powershell
python TF_IDF.PY
```

### 4. Realizar una búsqueda
Cuando el programa lo solicite, ingresa los términos que deseas encontrar. 
*   **Ejemplos recomendados**: "beca de excelencia", "fraude exámenes", "cancelar materia".

---
**Desarrollado como ejercicio práctico de Procesamiento de Información.**

|Requisito	|Cumple 2 Parcialmente 1 No cumple 0 |	Evidencia (página/tabla/figura/sección) |
|-------------------|-------------------------|----------------------------------------|
|Contexto aeronáutico claro y relevante |2 | reto-u3-pseudocodigo.py (comentarios y menú), reto-u3-analisis.md |
|Clara definición y clasificación de las variables de entrada, salida, de control e intermedias		|  2  | reto-u3-analisis.md (tabla de análisis) |
|Clara definición de las constantes que se utilizan en el problema		|   2 | reto-u3-analisis.md (tabla, aunque no hay constantes explícitas, el combustible inicial puede considerarse constante por etapa) |
|Ecuación que relaciona adecuadamente las variables del problema	|  2  | reto-u3-pseudocodigo.py (comb_restante = cant_comb - sum(comb_cons)) |
|No es solo cálculo directo		|  1  | reto-u3-pseudocodigo.py (hay bucle y condicional, pero el cálculo es directo) |
|Al menos un bucle (variable de control, condición de parada)	|  2  | reto-u3-pseudocodigo.py (for etapa_actual in range) |
|Al menos una sentencia condicional significativa	|	2   | reto-u3-pseudocodigo.py (if comb_restante <= 0) |
|Menú repetitivo hasta “Salir”		| 2    | reto-u3-pseudocodigo.py (while True, opción 4 para salir) |
|Sin listas, diccionarios, tuplas ni sets	|	2   | reto-u3-pseudocodigo.py (no se usan colecciones) |
|Declaración de uso de IA (si aplica)	|	 2   | reto-u3-analisis.py (comentario al final sobre el uso de IA para ayudar) |
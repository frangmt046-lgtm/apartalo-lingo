# 7. Requisitos no funcionales
> Ejercicio 7 · Tema 9 · 🎩 PO y 🎩 desarrollador
> Cada restricción va como **issue** (formulario "Requisito no funcional"). Aquí va el resumen.

| Issue | Restricción SMART | Externa / interna | Cualidad | Historia (T) | Prueba práctica (Tabla 2) o práctica (Tabla 4) |
|---|---|---|---|---|---|
| #21 RNF | la app debe procesar 30 reservas por hora con un tiempo de respuesta máximo de 3 segundos por reserva. | Externa | Desempeño | #2 | Prueba de desempeño (Tabla 2): medir el tiempo de respuesta |
| #22 RNF | El 100 % de las entradas inválidas deben rechazarse con un mensaje de error, sin que la app se cierre. | Externa | Robustez | #1 y #3 | Prueba de robustez (Tabla 2): entradas inválidas |
| #23 RNF | El 100 % de las reglas de negocio se programan con al menos 3 ciclos rojo-verde, visibles en el historial de commits. | Externa | Pruebas | #1 y #3 | Práctica red-green-refactor (Tabla 4) |

## 7.3 La que compruebo con código

- **Restricción:** #22
- **Prueba:** tests/rnf/test_robustez.py 

## 7.4 Una por sprint

- **La que agrego a mi DoD en el Sprint 1:** #23 RNF
- **Las que dejo para después y por qué:** #21 RNF y #22 RNF, por que aun no he realizado las pruebas suficientes para definirlas como terminadas.

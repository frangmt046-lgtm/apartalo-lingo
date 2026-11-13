# 6. Pruebas de aceptación y TDD
> Ejercicio 6 · Tema 8 · 🎩 desarrollador

## 6.2 Mis ciclos de TDD

| Ciclo | Commit ROJO | Commit VERDE | Commit REFACTOR (si hubo) | Qué aprendí |
|---|---|---|---|---|
| 1 | [f3dac67](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/f3dac67) | [2294952](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/2294952) | — | Como se inician las pruebas y como redactarlas correctamente |
| 2 | [45c6d9d](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/45c6d9d) | [c9e802f](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/c9e802f) | — | Cambiar de resultados fijos a posibles escenarios y el manejo de estos |
| 3 | [4cfee9f](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/4cfee9f) | [a5744d2](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/a5744d2) | — | manejo de errores y mejora del codigo con el REFACTOR |
| 4 | [901f594](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/901f594) | [ec3c5dc](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/ec3c5dc) | [706dc51](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/706dc51) | manejo de errores y mejora del código con el REFACTOR |
 
## 6.6 Cobertura de caminos

- **Función:** cambio_de_sesion
- **Caminos** (cada `return` y cada `raise`): 4 (3 return y 1 raise)
- **Caminos que recorren mis pruebas:** Los 3 return los recorren test_menos_de_4_horas_la_sesion_se_pierde, test_cambio_entre_4_y_24_horas_cobra_80 y test_cambio_con_24_horas_o_mas_se_reprograma_sin_costo. El raise lo recorre test_horas_negativas_lanzan_error
- **Cobertura:** 100%
- **Pruebas que agregué para completar:** Ninguna

## 6.7 Regresión

- **Defecto** (encontrado o provocado): total_compra no sumaba las compras combinadas, porque regresaba en el primer if
- **Prueba que lo detecta:** test_compra_combinada_suma_todo
- **Qué pasaba y cómo lo corregí:** Solia tener un if por cada tipo de sesion lo que ocasionaba que al hacer una compra combinada no sumaba los totales, lo corregi haciendo una formula en el return y solo dejando 2 if para los ValueError (commit [19cd20d](https://github.com/frangmt046-lgtm/apartalo-lingo/commit/19cd20d))

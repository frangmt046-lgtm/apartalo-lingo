# 3. El tablero kanban
> Ejercicio 3 · Tema 3 · 🎩 SM

## 3.2 Límites WIP

| Columna | Límite | Por qué ese número |
|---|---|---|
| Aceptación | 2 | Afinar criterios es rápido; se puede dejar lista la siguiente historia mientras se programa otra |
| Desarrollo | 1 | Al ser un equipo de una persona solo puedo programar una cosa a la vez|
| Pruebas | 1 | Se prueba una hisotoria y se libera antes de tomar otra|

## 3.3 Políticas explícitas

| Para pasar a… | La tarjeta debe cumplir… |
|---|---|
| Aceptación | Cuando su prioridad es must o should y sus puntos asignados los mas bajos. |
| Desarrollo | Cuando los criterios de aceptación son claros, los escenarios BDD ya están escritos y que no rebase la carga máxima. |
| Desarrollo listo | Cuando pasa todas las unitarias. |
| Pruebas | Cuando ya paso por Desarrollo listo y hay un lugar disponible. |
| Pruebas listo | Cuando todos los escenarios pasan |
| Liberación | Cuando todas las pruebas pytest fueron aprobadas. |

## 3.4 Las seis prácticas de kanban en mi tablero

| Práctica | Cómo la aplico (o por qué todavía no aplica) |
|---|---|
| 1. Visualizar el trabajo | Se aplico en las historias de usuario con estatus, puntos y prioridad. |
| 2. Limitar el WIP | Limites 2,1 y 1. |
| 3. Administrar el flujo | El estatus con respecto a las fechas de inicio y terminado. |
| 4. Hacer explícitas las políticas | Las politicas quedan bien definidas en la tabla Políticas explícitas. |
| 5. Implementar ciclos de retroalimentación | Con la junta diaria, la revisión y la retrospectiva |
| 6. Mejora colaborativa y evolución experimental | Aprendo al avanzar el proyecto, me doy cuenta de errores y cosas que podrian mejorar mientras trabajo. |

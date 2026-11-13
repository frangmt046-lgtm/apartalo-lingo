# Apártalo — Lingo

| Dato | |
|---|---|
| Estudiante | `Francisco Guadarrama Martinez` |
| Matrícula | `Al02893971` |
| Variante | ` 6 — Escuela de idiomas Lingo ` |
| Project (tablero) | `https://github.com/users/frangmt046-lgtm/projects/2` |

## Visión del producto


La app es una plataforma para comprar y agendar sesiones, esta esta enfocada para que la usen alumnos y tutores, la app resuelve problemas de administración para la dirección de la escuela, evitando mensajes en todo momento moviendo y cancelando sesiones, problemas con pagos atrasados y facilita la coordinacion de sesiones grupales e individuales. 

## Mi equipo Scrum (los tres sombreros)

| Sombrero | Lo que hago con él en este proyecto |
|---|---|
| 🎩 PO | se desarrollo y priorizo el backlog del proyecto |
| 🎩 SM | se configuro el tablero en github y los límites WIP |
| 🎩 Desarrollador | se desarrollaron R1 y R2 con sus pruebas  |

## Cómo está organizado este repositorio

| Carpeta o archivo | Qué contiene | Ejercicio |
|---|---|---|
| `docs/01_vision_y_problema.md` | Paradigmas, manifiesto, requisito vs. solución, incertidumbre | 1 |
| Issues `historia` y `epica` + `docs/02_backlog.md` | Product backlog, plantilla invertida, glosario, iceberg | 2 |
| `docs/03_tablero.md` | Columnas, límites WIP, políticas y prácticas de kanban | 3 |
| `docs/04_refinamiento.md` + `features/` | Grooming, carga máxima, división, escenarios BDD, tabla FIT | 4 |
| `docs/05_sprint1.md` | Planeación, bitácora, revisión y retrospectiva | 5 |
| `src/apartalo/` + `tests/` + `docs/06_tdd.md` | Código, pruebas y ciclos de TDD | 6 |
| Issues `rnf` + `docs/07_rnf.md` | Requisitos no funcionales | 7 |
| `metricas/` + `docs/08_metricas.md` | Fotografía del tablero y consultas SQL | 8 |
| `ENTREGA.md` | Enlaces a cada evidencia | Entrega |

## Cómo correr las pruebas

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                           # todas las pruebas
pytest -m aceptacion             # solo la suite de aceptación
pytest -m unitaria               # solo las unitarias
pytest -m rnf                    # solo las de requisitos no funcionales
```

# language: es
Característica: total de una compra en Lingo

  Esquema del escenario: Calcular el total de una compra
    Dado que un alumno compra <sueltas> sesiones sueltas, <grupales> sesiones grupales de <personas> personas y <paquetes> paquetes
    Cuando paga su compra
    Entonces el total es de <total> pesos

    Ejemplos:
      | sueltas | grupales | personas | paquetes | total |
      | 1       | 0        | 0        | 0        | 320   |
      | 0       | 1        | 2        | 0        | 380   |
      | 0       | 1        | 4        | 0        | 760   |
      | 0       | 0        | 0        | 1        | 2700  |
      | 1       | 1        | 2        | 1        | 3400  |

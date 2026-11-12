# language: es
Característica: Cambio o cancelación de una sesión en Lingo

  Esquema del escenario: Decidir qué pasa según las horas de anticipación
    Dado que un alumno avisa con <horas> horas de anticipación
    Cuando pide cambiar su sesión
    Entonces el resultado es <resultado> con un cargo de <cargo> pesos

    Ejemplos:
      | horas | resultado  | cargo |
      | 24   | reprograma | 0 |
      | 23   | reprograma | 80 |
      | 4   | reprograma | 80 |
      | 3   | pierde | 0 |
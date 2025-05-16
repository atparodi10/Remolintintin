# Propósito del Código

El propósito de este programa es registrar y reportar la asistencia académica de estudiantes durante una semana, en función de los días de clase y la cantidad de estudiantes por sección o aula.

Este sistema permite:

1) Registrar el estado de asistencia de cada estudiante por día.

2) Clasificar cada asistencia como:

    a) Presente

    b) Inasistencia No Justificada

    c) Inasistencia Justificada

3) Generar un resumen diario de asistencia.

4) Calcular un reporte semanal total con el número acumulado de cada tipo de asistencia.

# Funcionamiento General

Inicialización de datos:

    1) Se define cuántas aulas hay (aunque en tu código se simula solo una).

    2) Se define una lista de días de clase.

    3) Se establece el número de estudiantes por sección.

Entrada de asistencia:

    1) Por cada día y para cada estudiante, se solicita el estado de asistencia.

    2) El usuario puede ingresar el estado escribiéndolo completo o usando siglas (P, INJ, IJ).

Validación de entrada:

     1) El sistema rechaza entradas numéricas o vacías.

     2) Solo acepta los tres tipos de asistencia válidos.

Acumulación de datos:

     Se lleva un conteo diario y semanal de los tipos de asistencia.

Visualización ordenada:

     Se muestra un resumen diario después de cada jornada.

     Al final, se imprime un reporte semanal total.

(Opcional):

    1) Se pueden usar mejoras visuales como tabulate para mostrar los datos de forma tabular.

    2) También se puede limpiar la consola entre días para una mejor experiencia visual.

# Objetivo Final

El objetivo del código es facilitar el seguimiento de la asistencia estudiantil de forma manual pero organizada, permitiendo generar reportes útiles para docentes o administradores académicos.
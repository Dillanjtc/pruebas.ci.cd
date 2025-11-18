Ciclo CI/CD: De la Pruebas a la Construcción del Paquete
Este repositorio demuestra un flujo de trabajo completo de Integración Continua (CI) y Entrega Continua (CD) utilizando GitHub Actions y Python.

 Conceptos Clave
El ciclo CI/CD automatiza las etapas del desarrollo de software para garantizar calidad y rapidez:

Integración Continua (CI): Es la práctica de integrar cambios de código frecuentemente.

En este repo: Cada vez que se sube código (push), se activa un "Runner" en la nube que descarga el código y ejecuta pruebas automatizadas. Si las pruebas fallan, el proceso se detiene, evitando errores en producción.

Entrega Continua (CD): Es la automatización de la liberación del software.

En este repo: Si las pruebas (CI) pasan exitosamente, se inicia automáticamente la etapa de Build, que empaqueta el código fuente en un archivo instalable (un archivo .whl o .tar.gz).

Diagrama del Flujo
Fragmento de código

graph LR
    A[Desarrollador hace Push] --> B{GitHub Actions}
    B --> C[Job: Test]
    C -- Ejecuta Unit Tests --> D{¿Pasan Tests?}
    D -- No --> E[Fallo del Pipeline ]
    D -- Si --> F[Job: Build]
    F -- Genera Paquete --> G[Artefacto /dist✅]
 Estructura del Proyecto
src/: Contiene la lógica de la aplicación (funciones matemáticas simples).

tests/: Contiene pruebas unitarias que validan que la lógica sea correcta.

.github/workflows/pipeline.yml: Archivo YAML que define los pasos que ejecuta GitHub automáticamente.

 Cómo funciona el Pipeline (Paso a Paso)
El archivo de configuración pipeline.yml define dos trabajos secuenciales:

1. Etapa de Pruebas (job: test)
Levanta una máquina virtual Ubuntu.

Instala Python 3.9.

Ejecuta python -m unittest discover tests.

Resultado: Verifica que las sumas y multiplicaciones den el resultado matemático correcto.

2. Etapa de Construcción (job: build)
Tiene una dependencia: needs: test. Solo corre si las pruebas pasaron.

Instala la librería build.

Ejecuta python -m build.

Resultado: Genera una carpeta dist/ con el paquete listo para instalarse en cualquier computadora.

 Pruebas Incluidas
El sistema valida automáticamente casos como:

sumar(2, 3) debe ser 5.

multiplicar(3, 4) debe ser 12.

Si modificas el código y rompes esta lógica (ej. cambias + por - en la suma), GitHub Actions marcará el commit con una  roja.

 Descargar el Artefacto (Package)
Una vez que el pipeline finaliza en la pestaña "Actions" de GitHub:

Entrar a la ejecución del workflow.

Ir a la sección Artifacts.

Descargar paquete-distribuible.

Este archivo zip contiene el instalable .whl generado automáticamente
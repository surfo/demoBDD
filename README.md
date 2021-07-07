## Definición de BDD 

BDD o Desarrollo impulsado por comportamiento (Behavor Driven Development), es una práctica de ingeniería de software diseñada para ayudar a los equipos a diseñar y a entregar un software más valioso y de mayor calidad con gran rapidez.  Se basa principalmente en prácticas agiles que incluye el desarrollo basado en pruebas (TDD) y el diseño impulsado por dominio (DDD). BDD proporciona un lenguaje basado en oraciones estructuradas de una forma simple (Gherkin), que facilitan la comunicación entre los miembros del equipo.  

## Integrando BDD en metodología Agile 

Si damos una mirada de forma simplificada en la metodología de desarrollo tradicional, supongamos que un cliente quiere desarrollar un nuevo módulo en su software, el proceso para desarrollar esta nueva funcionalidad seria la siguiente 

(Ver Figura 1):  
![figura1](https://user-images.githubusercontent.com/55904664/124683239-f9af1000-dea2-11eb-8da9-a15a140a9ce3.png)

- 1.- El cliente le dice al analista de negocio como le gustaría que funcionara la nueva funcionalidad. 

- 2.- El analista de negocio traduce el pedido del cliente en un conjunto de requisitos para los desarrolladores, describiendo lo que debería hacer el software. 

- 3.- El desarrollador, traduce los requisitos en código y en pruebas unitarias en algún lenguaje de programación para implementar el nuevo feature.  

- 4.- Los tester traducen este documento de requisitos en casos de pruebas, y los utiliza para corroborar que el nuevo feature o funcionalidad cumpla con los requisitos del cliente. 

- 5.- Se realizan la documentación técnica y funcional del código y software (DTEC y AFUN). 

De esta forma, es muy probable que a través de este modelo la información se pierda o sea mal entendida. Hay una alta probabilidad de que el nuevo módulo desarrollado no funcione exactamente como quería cliente y que la documentación realizada no refleje los requisitos iniciales del cliente.  

 

Figura 1. Modelo Tradicional  

Si observamos otro caso donde utilizan el modelo agile aplicando BDD, se muestra un equipo donde los analistas de negocios, desarrolladores y testers colaboran para comprender juntos los requisitos, utilizando un lenguaje común que les permite un camino fácil y menos ambiguo desde los requisitos del usuario final hasta las pruebas automatizadas. Estas pruebas automatizadas especifican como debe comportarse el software funcional que se centra principalmente en las funciones que realmente le importa al negocio. 

![figra2](https://user-images.githubusercontent.com/55904664/124683592-bf923e00-dea3-11eb-89ba-2d2d774e4b6d.png) 
***Figura 2. Modelo Agile aplicando BDD***  

 

- 1.- El analista de negocio habla con el cliente sobre lo que quiere, esto con la finalidad de reducir el riesgo de malentendidos y suposiciones ocultas, hablan a través de ejemplos de lo que debería hacer la función  

- 2.- Antes de comenzar a trabajar en la función, el analista de negocio se reúne con los desarrolladores y testers, tienen una conversación sobre la nueva funcionalidad. En esta conversación, discuten y traducen ejemplos claves de cómo debería funcionar la función en un conjunto de requisitos escritos en un formato de idioma denominado Gherkin. 

- 3.- El desarrollador utiliza la herramienta BDD para convertir estos requisitos en un conjunto de pruebas que se ejecutan contra el código de la aplicación. 

- 4.- El tester utiliza los resultados de estas pruebas como punto de partida para las pruebas manuales y exploratorias. 

- 5.- Las pruebas automatizadas actúan como especificación técnica de bajo nivel y proporcionan ejemplos actualizados de cómo funciona el sistema. Donde, se puede revisar los informes de las pruebas para ver que funciones se han entregado y si funciona de la manera esperada.  

Comparando ambos escenarios en el modelo BDD hay conversaciones intensivas con la finalidad de reducir la cantidad de información perdida, en el paso 2 se comienza con las especificaciones escritas en lenguaje Gherkin, basados en las especificaciones dadas por el cliente, de esta forma gran parte de la ambigüedad se eliminan al traducir estos requisitos iniciales del cliente en el código, informes y documentación. 

## Ciclo de BDD y TDD 

El Desarrollo guiado por pruebas TDD (Test Driven Development)  y el Desarrollo guiado por comportamiento BDD (Behavior Driven Development) son dos metodologías que tienen como objetivo principal asegurar la calidad del software desde la fuente de la misma. Podemos decir que, en términos generales BDD no es un reemplazo de TDD, sino que son dos enfoques de calidad aplicados en distintos niveles del producto o servicio a desarrollar. 

 

 
![figura3](https://user-images.githubusercontent.com/55904664/124683600-c456f200-dea3-11eb-98a7-4812f6417545.png)
***Figura 3. Ciclo de BDD***  

 

BDD es un proceso que amplía las ideas de TDD y las combina con otras ideas de diseño de software y análisis de negocio para proporcionar un proceso y herramientas a los desarrolladores (Developers y Testers), con la intención de mejorar el desarrollo del software. 

Dicho esto, podemos mencionar ciertos aspectos importantes de BDD: 

- En BDD no se prueban unidades o clases, probamos escenarios y el comportamiento de las clases a la hora de cumplir dichos escenarios, los cuales pueden estar compuestos de varias clases. 

- BDD toma el enfoque de prueba presentado por TDD y agrega semántica funcional y de usuario, con la finalidad de seguir la misma fórmula para todo el software. 

- BDD ayuda a definir flujos, pero no nos ayuda a diseñar el software, tal como lo hace TDD. Por tanto, ambas metodologías son complementarias. 

- BDD ha evolucionado a partir de prácticas ágiles establecidas y está diseñado para hacerlas más accesibles y efectivas para los equipos. Con el tiempo, esta metodología ha crecido para abarcar un espectro más amplio del análisis ágil y de las pruebas de aceptación automatizadas. 

En la figura 3, podemos observar cómo se complementan ambas metodologías, describiéndolas en resumen de la siguiente manera: 

 

## Historia de Usuarios 

Cuando un equipo practica BDD y decide implementar una funcionalidad, trabaja junto los usuarios y otras partes interesadas para definir las Historias y Criterios de aceptación de la función que esperan entregar. En concreto, los usuarios ayudan a definir un conjunto de ejemplos precisos que ilustre el resultado de la funcionalidad. 

Para ello se utiliza un lenguaje común que puede entenderse fácilmente para ambos extremos, hablamos de los usuarios y el equipo de desarrollo. Por lo general, se hace mediante el uso del siguiente formato: 

```gherkins
Como [rol/usuario] 

Quiero [funcionalidad/característica] 

Para [Beneficio/valor] 
```

Cuando se define una historia de Usuario, se debe tomar en cuenta ciertos aspecto, en que esta Historia debe estar escrita con el método **INVEST**:  

**Independiente (I):** Cada historia de usuario pueda ser planificada e implementada en cualquier orden. No dependen unas de otras, si ocurre se deben dividir o combinar. 

**Negociable (N):** Las historias deben ser negociables ya que sus detalles serán acordados por el cliente/usuario y el equipo durante la fase de “conversación”. 

**Valor (V):** Una historia de usuario tiene que ser valiosa para el cliente o el usuario. 

**Estimable (E):** Una buena historia de usuario debe ser estimada con la precisión suficiente para ayudar al cliente o usuario a priorizar y planificar su implementación. Si no podemos estimarla debemos indicar en la fase de conversación o dividirla. 

**Pequeña (S):** Solemos hacerlas de tal modo que ocupen como máximo un sprint. 

**Testeable (T):** La historia de usuario debe probarse. Tanto el usuario como el equipo de desarrollo tienen que poder probarla para saber cuándo está finalizada. 

En la imagen 4, podemos observar un ejemplo de cómo es la estructura de una historia de usuario con el modelo INVEST, esta cuenta con las siguientes secciones: 

- ID: Identificador de la historia. 

- Título: Texto descriptivo de la historia de usuario 

- Descripción: Descripción sintetizada de la historia de usuario, siguiendo el patrón: Como [rol], quiero [objetivo], para [beneficio]. 

- Estimación: también conocido como puntos de historia, es la estimación del esfuerzo de la implementación de la Historia de Usuario. 

- Valor: es el valor que aporta la Historia de Usuario al cliente o usuario. Con el tiempo este campo determinará el orden con el que la historia de usuario va a ser implementadas. 

- Criterios de aceptación: o pruebas de aceptación cumplen dos funciones, clarificar el contexto en el que ocurre la historia de usuario y facilitar saber cuándo está terminada. 

 
![figura4](https://user-images.githubusercontent.com/55904664/124683606-c8830f80-dea3-11eb-98bc-b3fe4e367a10.png)
***Figura 4. Ejemplo de la Composición de una Historia de Usuario (INVEST) en Octane*** 

 

Para la implementación de estas Historias de Usuarios en BDD, se usan distintas herramientas las cuales en su mayoría utilizan un formato general denominado **DSL** (Domain-Specific Language), estos son lenguajes naturales que expresan comportamientos y definen la salida esperada.  

Los más usados actualmente a la hora de definir escenarios BDD, es el lenguaje Gherkin el cual suele constar de pasos que tienen el formato explicado en la sección anterior **Como-Quiero-Para**. 

## Criterios de Aceptación 

Los criterios de aceptación definen los requisitos del Product Owner sobre cómo debe comportarse la aplicación para que una determinada acción se pueda llevar a cabo.  

## ¿Quién debe escribir los criterios de aceptación? 

Esto depende de los equipos agiles, es muy común que lo desarrolle todo el equipo (Product Owner, Tester, Developer), pudiendo ser en un brainstorming, como parte de refinamiento de la historia, se pueden agregar ejemplos de cómo debería funcionar la aplicación a desarrollar, estos ejemplos juegan un papel primordial en BDD, porque son una forma muy efectiva de comunicar los requisitos de forma clara y concisa. Luego el Tester se encargaría de asegurarse que este bien escritas, completas y con la cobertura de acuerdo a la estrategia de las pruebas.  

Los criterios de aceptación deben describir siempre un contexto, un evento y la respuesta o consecuencia esperada del sistema. La forma más utilizada para describir los criterios de aceptación es conocida como Given-When-Then (Dado-Cuando-Entonces) 

## Lenguaje Gherkin 

Gherkin es el lenguaje específico de dominio (DSL) utilizado por los practicantes de BDD de todo el mundo por su gramática legible para los negocios. Gherkin tiene su propia forma de organizar las historias de usuario ágiles usando reglas de formato como características, escenarios, pasos, ejemplos, etc. 

Una vez tengamos las historias de usuario, generaremos un archivo con los test funcionales, usando lenguaje Gherkin. Estos después son implementados usando frameworks específicos. 

Existen diferentes frameworks y librería en distintas tecnologías para especificar las pruebas BDD, como JBehave para Java, Cucumber para JS o behave para Python, todos soportan el estándar Gherkin. De esta manera se puede documentar los requisitos y las pruebas automatizadas de las nuevas funcionalidades desarrolladas.  

Dicho esto, en Gherkin, los requisitos relacionados con las características se agrupan en un solo archivo denominado: features files. Un feature file, o archivo de características, contiene una breve descripción de la característica o feature, seguido de una serie de escenarios (scenarios) o ejemplos formalizados de como funcionaria nuestro nuevo feature a implementar (Ver ejemplo Figura 5.). 

Para entender lo que es un feature file, debemos considerar que un Feature contiene la Historia de Usuario que estaríamos implementando, además de ellos el Feature file contiene los Scenarios, los cuales serían nuestros criterios de aceptación transformadas en pruebas de aceptación, escritas como un ejemplo representativo de cómo debería funcionar nuestra aplicación. En la siguiente imagen, se muestra el contenido de un Feature file:   

```gherkin
Feature: transferir dinero entre cuentas 
    Como cliente bancario Quiero transferir fondos entre mis cuentas siempre que lo necesite. 

    Para administrar mi dinero de manera más eficiente 


Scenario: transferir dinero a una cuenta de ahorros 
    Given que mi cuenta corriente tiene un saldo de 1000,00 
    And mi cuenta de ahorros tiene un saldo de 2000,00 
    When transfiero 500,00 de mi cuenta corriente a mi cuenta de ahorros 
    Then debería tener 500,00 en mi cuenta corriente 
    And debería tener 2500,00 en mi cuenta de ahorros 

 
Scenario: Transferencia con fondos insuficientes 
    Given que mi cuenta corriente tiene un saldo de 1000,00 
    And mi cuenta de ahorros tiene un saldo de 2000,00 
    When transfiero 1500,00 de mi cuenta corriente a mi cuenta de ahorros 
    Then debería recibir un error de 'fondos insuficientes' 
    And debería tener 1000,00 en mi cuenta corriente 
    And debería tener 2000,00 en mi cuenta de ahorros 
```
***Figura 5. Transformando mi Historia de Usuario a un Feature File***   

 

Para escribir los escenarios, debemos considerar las siguientes características o palabras claves: 

***Given (Dado):*** describe las condiciones previas para el escenario y prepara la prueba. 

***When (Cuando):*** define interacción del usuario que acciona la funcionalidad que deseamos testear. 

***Then (Entonces):*** En este paso vamos a observar los cambios en el sistema y ver si son los deseados. 

También existen otras palabras claves como ***And (Y)*** y ***But (Pero)***, los cuales son utilizados para unir varios pasos. 

Existen distintas formas de cómo desarrollar los escenarios, está la forma simple (Figura 5.), a continuación, mostraremos un repaso por las otras formas de desarrollar escenarios en Gherkin: 

## Documentación adicional en BDD con Gherkin 

A veces es necesario agregar una documentación extra en algún patrón, se puede utilizar las cadenas de texto como figura en el siguiente ejemplo:  


```gherkin
Feature: Búsqueda en google 
    Como usuario web, Quiero buscar en Google 
    Para poder responder mis dudas. 

Scenario: Búsqueda simple en Google 
    Given un navegador web en la página de Google 
    When se introduce la palabra de búsqueda “pingüino” 
    Then se muestra el resultado de “pingüino” 
    And la página de resultados muestra el texto en Wikipedia 
“““ 
Nombre Científico: Spheniscidae 
Clase Aves 
””” 
```


Figura 6. Ejemplo de documentación extra delimitada por “””

### Tabla o Listado de valores en BDD con Gherkin 

Se pueden añadir estructuras “Data tables” para agregar ejemplos que luego se pueden pasar en las pruebas. 


```gherkin
Feature: Búsqueda en google 

    Como usuario web, Quiero buscar en Google 
    Para poder responder mis dudas. 
 
Scenario: Búsqueda simple en Google 
    Given un navegador web en la página de Google 
    When se introduce la palabra de búsqueda “pingüino” 
    Then se muestra el resultado de “pingüino” 
    And se muestran los siguientes resultados 

|Relate               | 
|pingüino emperador   | 
|videos pingüino      | 
|pingüinos rey	      | 
```


***Figura 7. Ejemplo de tabla o listado de valores*** 

 

## Antecedentes y Escenarios en BDD con Gherkin 

Los scenarios de una feature pueden compartir pasos de configuración comunes. En lugar de duplicar estos patrones, se pueden definir como Background: 


```gherkin
Feature: Búsqueda en google 

    Como usuario web, Quiero buscar en Google 
    Para poder responder mis dudas. 

Background: Given un navegador web en la página de Google 

Scenario: Búsqueda simple en Google 
    When se introduce la palabra de búsqueda “pingüino” 
    Then se muestra el resultado de “pingüino” 

Scenario: Búsqueda simple en Google 
    When se introduce la palabra de búsqueda “panda” 
    Then se muestra el resultado de “panda” 
```



***Figura 8. Ejemplo de Antecedentes***  

 

## Esquemas de escenarios Outline  en BDD con Gherkin 

Los scenarios outlines permiten automatizar la definición en Gherkin. Al observar el ejemplo anterior, los dos escenarios son idénticos si no fuese por sus términos de búsqueda “pingüino” y “panda”. Como se puede observar utilizando las “Data Tables” EXAMPLES, cada columna de la tabla contiene el título definidos en los patrones con los diferentes ejemplos: 


```gherkin
Feature: Búsqueda en google 
    Como usuario web, Quiero buscar en Google 
    Para poder responder mis dudas. 

Scenario Outline: Búsqueda simple en Google 

    Given un navegador web en la página de Google 
    When se introduce la palabra de búsqueda “<frase>” 
    Then se muestra el resultado de “<frase>” 
    And se muestran los siguientes resultados “<relacionado>” 

 

Examples: 
|    frase     |  relacionado        | 
|   pingüino   |  pingüino emperador | 
|   panda      |  panda gigante      | 
|   elefante   |  elefante africano  | 
```


***Figura 9. Ejemplo de Escenario Outline*** 

 

## Tags en BDD con Gherkin 

Las ***etiquetas*** o ***‘tags’ “@”*** son una excelente manera de clasificar escenarios. Se pueden usar para ejecutar selectivamente pruebas basadas en el nombre de la etiqueta. Las etiquetas comienzan con el símbolo "@". Los nombres de las etiquetas distinguen entre mayúsculas y minúsculas y espacios en blanco. 

```gherkin
Feature: Búsqueda en google 
    Como usuario web, Quiero buscar en Google Para poder responder mis dudas.	 

@automatización @google  @pingüino 
Scenario: Búsqueda simple en Google 
    Given un navegador web en la página de Google 
    When se introduce la palabra de búsqueda “pingüino” 
    Then se muestra el resultado de “pingüino” 
```

***Figura 10. Ejemplo de Tags***

 

## BDD Test End to End y Test funcionales que fallan 

En este punto un test de aceptación puede ser definido usando las técnicas de BDD que hemos visto. Estas técnicas definen la funcionalidad usando una sintaxis estricta (Gherkin) como lo vimos en la sección anterior. La funcionalidad especificada prueba los criterios de aceptación de la historia. La especificación del test también es una especificación funcional del sistema, a partir de este punto, nos referiremos a los test de aceptación (criterios de aceptación) como especificaciones ejecutables de alto nivel. 

Cuando las especificaciones ejecutables de alto nivel son ejecutadas, estas fallan (ya que no se generado código aún para implementar la historia). 

## Ciclo TDD 

Es momento de definir tests de bajo nivel, los test unitarios, siguiendo el proceso propuesto por TDD, en este punto nos referiremos a nuestros test unitarios como especificaciones ejecutables de bajo nivel. Especificar estos tests es un doble ejercicio que se debe: definir los tests y diseñar una actividad en detalle. Es necesario, escribir estos tests antes de codificar, como  hemos visto, nos obliga a pensar sobre el diseño del software planificado. 

Cuando estas especificaciones ejecutables de bajo nivel son ejecutadas, estas fallaran, debido a que igual que antes, aún no se ha escrito una línea de código. 

Una vez hecho esto, es momento de escribir el código que resuelva los test unitarios siguiendo el proceso propuesto por TDD. El objetivo es asegurar que todos los tests de bajo nivel corren con éxito. Esto incluye corregir bugs y refactorizar el código del producto y también el de los tests o especificaciones de bajo nivel. 

## BDD Test que pasan y Refactorización 

Una vez que todos los tests de bajo nivel han pasado con éxito, podemos ejecutar los tests de alto nivel (e2e o funcionales), ajustando el código, corrigiendo bugs, entre otras tareas. 

La refactorización se repite hasta que todos los test de alto nivel y los de bajo nivel son pasados con éxito. 

## Historia siguiente 

Este proceso que embebe TDD en un BDD se repite para todas las historias de usuario dentro del ciclo iterativo (un sprint). Al finalizar dicho sprint tendremos la implementación con el nivel de calidad deseado a alto nivel y a bajo nivel; con la ventaja de que la calidad está garantizada desde la fuente. 

 

Este proceso se represa en el siguiente esquema: 

 
![figura11](https://user-images.githubusercontent.com/55904664/124683617-ce78f080-dea3-11eb-9edb-ac2d74a06197.jpg)
***Figura 11. Proceso iterativo de TDD*** 

 

## Buenas prácticas en BDD 
### Pirámide de Pruebas 

BDD admite la automatización de pruebas de componentes y de la interface de usuario (UI). Y como buena práctica general para el mantenimiento y la mejora futura, se recomienda que se siga el enfoque de la pirámide de pruebas en términos de número de pruebas y cobertura en todo el espectro de pruebas automatizadas. (Pruebas unitarias, Prueba de componente (API) y Pruebas de UI. 

 
![figura12](https://user-images.githubusercontent.com/55904664/124683629-d20c7780-dea3-11eb-9b2b-326b8f09709d.png)
***Figura 12. Pirámide de pruebas*** 

 

## Background de las pruebas 
### Objetivos de las Pruebas 

Establecer los objetivos de una prueba es clave. En principio, cada escenario en una característica debe cubrir un solo objetivo. Sin embargo, esto no necesita ser una regla estricta, si fuese más adecuado para escenarios específicos cubrir objetivos múltiples. (Validación y resultados, por ejemplo). Como guía, las pruebas de UI solo deberían cubrir trayectos válidos extremo a extremo. (Se pueden incluir mensajes de advertencia según corresponda). Los objetivos de la prueba no deben confundirse con las condiciones de la prueba. Cada objetivo puede tener múltiples condiciones de prueba (puntos de verificación). 

Beneficios: Separación de responsabilidades y mantenimiento más fácil. 

## Escenarios Guiados por Datos 

Es necesario asegurarse que los escenarios se basen en datos (tanto como sea posible). 

Beneficios: Evita la duplicación de escenarios y permite una mayor flexibilidad para el mantenimiento. 

## Scripts Independientes 

Los scripts deben ser independientes de otros scripts, para que estos puedan ejecutarse por sí mismos. 

Beneficios: A medida que el paquete de prueba sigue creciendo, es importante poder investigar los fallos individuales y poder mejorar para futuros cambios. Si se crea una interdependencia compleja, será más difícil y podría terminar siendo inmanejable para los equipos de proyectos más nuevos. 

## Idempotente 

El paquete de prueba o la secuencia de comandos individual debe volver a ejecutarse en un entorno de destino y dar como resultado exactamente el mismo comportamiento que la primera ejecución. Un script debe estar diseñado para limpiar sus actualizaciones o garantizar la existencia del estado de datos requerido como parte de los antecedentes para llevar a cabo la prueba. 

Beneficios: Garantiza que el usuario que no esté familiarizado con una funcionalidad en particular pueda ejecutar y analizar los resultados. 

## Lenguaje de Negocio 

El archivo de características debe estar escrito en lenguaje comercial sin referencia a objetos técnicos. 

Beneficios: El objetivo final de BDD es tener especificaciones de negocio comprensibles que se utilicen para validar el sistema creado. Cuando estas especificaciones se vuelven técnicas, se frustra el propósito del paquete de prueba. 

## Prueba de concepto  

## Definición de Historia de Usuario y Criterios de aceptación 

## Escribiendo nuestro test E2E o funcional que fallan 

## Ciclo de TDD haciendo nuestra prueba unitaria 

 

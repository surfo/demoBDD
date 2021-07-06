
Feature: Calculadora
Scenario Outline: Sumar
        Given se inicia la calculadora
        When el usuario quiere sumar dos numeros <num1> y <num2>
        Then el resultado de la suma es <resultado>
    
Examples:
| num1 | num2 | resultado |
|  2   |  6   |   8       |
|  2   |  8   |   10      |
|  2   | 14.4 |   16.4    |

Scenario: restar
        Given se inicia la calculadora
        When el usuario quiere restar dos numeros 10 y 3 
        Then el resultado de la resta es 7




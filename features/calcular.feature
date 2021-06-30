
Feature: Calculadora
Scenario Outline: Sumar
        Given se inicia la calculadora
        When el usuario ingresa dos numeros <num1> y <num2>
        Then el resultado es <result>
    
Examples:
| num1 | num2 | result |
|  2   |  6  |  8     |
|  2   |  8  |  10     |

Scenario: restar
        Given se inicia la calculadora
        When el usuario ingresa dos numeros "10" y "3" 
        Then el resultado es "7"


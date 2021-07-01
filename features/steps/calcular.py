from typing import Type
from behave import given, when, then
from src.calculadora import *


@given(u'se inicia la calculadora')
def step_impl(context):
    print(u'STEP: Given se inicia la calculadora')
    pass


@when(u'el usuario quiere sumar dos numeros {num1} y {num2}')
def step_impl(context, num1, num2):
    print(u'STEP: When el usuario quiere sumar dos numeros {} y {}'.format(num1,num2))
    suma = sumar(float(num1),float(num2))
    context.resultado = suma
    
    
@then(u'el resultado de la suma es {out}')
def step_impl(context,out):
    print(u'STEP: Then el resultado de la suma es {}'.format(out))
    assert context.resultado == float(out)

@when(u'el usuario quiere restar dos numeros {num1} y {num2}')
def step_impl(context, num1, num2):
    print(u'STEP: When el usuario quiere restar dos numeros {} y {}'.format(num1,num2))
    resta = restar(float(num1),float(num2))
    context.resultado = resta
    
    
@then(u'el resultado de la resta es {out}')
def step_impl(context,out):
    print(u'STEP: Then el resultado de la resta es {}'.format(out))
    assert context.resultado == float(out)

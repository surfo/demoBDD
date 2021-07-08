from typing import Type
from behave import given, when, then
from werkzeug.wrappers import response
import requests
import json
from selenium import webdriver
# from src.calculadora import *


# @given(u'se inicia la calculadora')
# def step_impl(context):
#     print(u'STEP: Given se inicia la calculadora')
    

# @when(u'el usuario quiere sumar dos numeros {num1} y {num2}')
# def step_impl(context, num1, num2):
#     print(u'STEP: When el usuario quiere sumar dos numeros {} y {}'.format(num1,num2))
#     suma = sumar(float(num1),float(num2))
#     context.resultado = suma
    
    
# @then(u'el resultado de la suma es {out}')
# def step_impl(context,out):
#     print(u'STEP: Then el resultado de la suma es {}'.format(out))
#     assert context.resultado == float(out)

# @when(u'el usuario quiere restar dos numeros {num1} y {num2}')
# def step_impl(context, num1, num2):
#     print(u'STEP: When el usuario quiere restar dos numeros {} y {}'.format(num1,num2))
#     resta = restar(float(num1),float(num2))
#     context.resultado = resta
    
    
# @then(u'el resultado de la resta es {out}')
# def step_impl(context,out):
#     print(u'STEP: Then el resultado de la resta es {}'.format(out))
#     assert context.resultado == float(out)


@given(u'se inicia la calculadora')
def step_impl(context):
    print(u'STEP: Given se inicia la calculadora')
    context.url = 'http://localhost:4000/sumar'

@when(u'el usuario quiere sumar dos numeros {num1} y {num2}')
def step_impl(context, num1, num2):
    print(u'STEP: When el usuario quiere sumar dos numeros {} y {}'.format(num1,num2))
    context.body = {
            "argumento1": float(num1),
            "argumento2": float(num2)
            }
    context.headers = { 'content-type' : 'application/json'}
    
    context.resultado = requests.post('http://localhost:4000/sumar', data= json.dumps(context.body), headers= context.headers)
    assert context.resultado.status_code == 200    
   
    
@then(u'el resultado de la suma es {out}')
def step_impl(context,out):
    print(u'STEP: Then el resultado de la suma es {}'.format(out))
    print(context.resultado.json())
    assert context.resultado.json() == {'resultado': float(out)} 

@when(u'el usuario quiere restar dos numeros {num1} y {num2}')
def step_impl(context, num1, num2):
    print(u'STEP: When el usuario quiere restar dos numeros {} y {}'.format(num1,num2))
    context.body = {
            "argumento1": float(num1),
            "argumento2": float(num2)
            }
    context.headers = { 'content-type' : 'application/json'}            
    context.resultado = requests.post('http://localhost:4000/restar', data= json.dumps(context.body), headers= context.headers)
        
    
@then(u'el resultado de la resta es {out}')
def step_impl(context,out):
    print(u'STEP: Then el resultado de la resta es {}'.format(out))
    assert context.resultado.json() == {'resultado': float(out)} 
    

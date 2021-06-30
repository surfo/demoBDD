from behave import given, when, then
from src.calculadora import sumar

@given(u'se inicia la calculadora')
def step_impl(context):
    print(u'STEP: Given se inicia la calculadora')
    pass


@when(u'el usuario ingresa dos numeros {num1} y {num2}')
def step_impl(context, num1, num2):
    print(u'STEP: When el usuario ingresa dos numeros {} y {}'.format(num1,num2))
    context.sumar(num1,num2)
    



@then(u'el resultado es {out}')
def step_impl(context,out):
    print(u'STEP: Then el resultado es {}'.format(out))
    assert context.sumar.result == out
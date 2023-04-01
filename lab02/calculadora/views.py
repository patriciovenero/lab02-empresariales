from django.shortcuts import render

# Create your views here.
def formulario2(request):
    return render(request, 'calculo/formulario2.html')

def calcular(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        operacion = request.POST['operacion']
        calcular = 0
        if operacion == 'suma':
            calcular = int(num1) + int(num2)
        elif operacion == 'resta':
            calcular = int(num1) - int(num2)
        elif operacion == 'multiplicacion':
            calcular = int(num1) * int(num2)
        return render(request, 'calculo/respuesta2.html', {'calcular': calcular})
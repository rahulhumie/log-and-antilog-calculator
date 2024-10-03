from django.shortcuts import render
import math

# Create your views here.
def logbase10(request):
    result = None
    result2 = None 
    error_message = None
    
    if request.method == "POST":  # Check if the request is POST (form submitted)
        number = float(request.POST.get('num1'))  # Get the input from the form (number field)
        
        if number > 0:  # Check if the number is positive (logarithm is defined for positive numbers)
            result = math.log10(number)
            result2 = math.pow(10,number) 
            
            
             # Calculate log base 10 of the number
        else:
            error_message = "Logarithm undefined for zero or negative numbers!"  # Error for invalid input
            
    return render(request, 'index.html', {'num1':number,'result': result,'result2':result2 })

import random
import string

def msghola():
   return "Hola mundo...!!"

def getrandomstring(length):
  # choose from all lowercase letter
  letters = string.ascii_uppercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

def generate_random_int(start,end):
  # choose from all lowercase letter
  return random.randint(start, end)

def generate_random_float(start,end):
  # choose from all lowercase letter
  return round(random.uniform(start, end),2)

def generate_dni():
  numbers = string.digits
  result_dni =''
  #print(numbers)
  for i in range(1,9,1):# FOR desde 1 hasta 8, i++
      result_dni = result_dni+(random.choice(numbers)) 
  return result_dni   

def generate_province(number):
  if (number==1): 
    return "Abancay"
  elif(number==2):
    return "Andahuaylas"
  elif (number==3): 
    return "Antabamba"
  elif(number==4):
    return "Aymaraes"
  elif (number==5): 
    return "Grau"
  elif(number==6):
    return "Cotabambas"
  elif(number==7):
    return "Chincheros"  
  else:
    return "sin provincia"

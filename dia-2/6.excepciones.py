try:
    print(5/0)
except ZeroDivisionError:
    print('Error al hacer la division entre 0')
    
except TypeError:
    print('Error por cuestiones de tipos de datos')

except Exception:
    print('Ya no se cual es el error!')
else:
    # en el caso que nunca ingrese a ningun except
    print('TODO BIEN!')
finally:
    # ingresa ya sea si estuvo bien o si entro a algun except
    print('Yo ingreso SI O SI')

print('Yo soy el final del archivo')
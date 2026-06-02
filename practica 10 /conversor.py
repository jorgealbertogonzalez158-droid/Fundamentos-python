print("Bienvenido al conversor de millas a kilómetros")

print("Escribe un número en millas:")
millas = input()#string

print("Tipo de dato de millas", type(millas))
#Convertir su atring a numero
millas = float(millas)
print("Tipo de datos de millas", type(millas))

# 1 millas = 1.609 kms
kílometros = millas * 1.609

print("Millas ingresadas:",millas)
print("Kilometro:", kílometros)

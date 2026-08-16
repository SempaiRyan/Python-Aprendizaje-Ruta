# Profundizar en set
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables
# conjunto = {[1,2],[3,4]}


# Operaciones de conjuntos con set
# Personas con distintas características
pelo_negro = {'Juan','Karla','Pedro','María'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'Karla','Laura'}
menores_30 = {'Juan','Karla','María'}
# Todos con ojos_cafe y pelo rubio (Union) (no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

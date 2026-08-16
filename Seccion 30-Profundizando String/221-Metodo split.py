# Profundizar python
# help(str.split)

# Lista
cursos='Java Python Angular Sprint Excel'

# listacurso=cursos.split()
# print(f'Lista de cursos: {listacurso}')


curso_separado_coma='Java,Python,Javascript,Excel'
listacurso=curso_separado_coma.split(',')


print(f'Lista de cursos: {listacurso}')
# print(len(listacurso))
# print(f'Lista de cursos: {cursos}')


listacurso=curso_separado_coma.split(',',2)
print(len(listacurso))
print(f'Lista de cursos: {cursos}')
# p131-func-mas-param

def saluda_todos(*todos: str) -> None:
    print(f'Saluda a todos: {len(todos)}')
    for nombre in todos:
        print(f'Saludos a : {nombre}')
    print()

saluda_todos('Carlos')
saluda_todos('Carlos', 'Jose', 'Luis')
saluda_todos('a', 'b', 'c', 'd', 'e', 'f')
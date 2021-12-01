pre = None
line = None
usuario = None
registrado = 0

print("\nEste es tu nuevo terminal de Linux en Python.")

def inicio():
    
    pre = ""
    line = input("Introduce un nombre de usuario registrado: "+pre)
    if (line == "usuario" or line == "root"):
        usuario = line
        return usuario
    elif (line == "quit" or line == "exit"):
        print()
    else:
        print(line + " no es un usuario registrado.")


def comLine():
    usuario = inicio()
    registrado = 1
    if (usuario == "root"):
        homepath = "/root"
    else:
        homepath = "/home/"+usuario+"/"
    if (registrado == 1):
        print()
        print("Bienvenido," + usuario)
        pre = "> "
        while registrado == 1:
            line = input(pre)

            # Comandos
            commands = {
                'exit',
                'quit',
                'ls',
                'dir',
                'pwd',
                'info'
            }
            commandnotfound = 0;
            for command in commands:
                if (line == command):
                    if (command == 'exit'):
                        usuario = None
                        registrado = 0
                        print("Logging out...")
                        print("")
                    elif(command == "quit"):
                        usuario = None
                        registrado = 0
                        print("Closing terminal...")
                        break
                    elif (command == 'ls' or command == 'dir'):
                        print("Listing directory:")
                        print("-rwxr-xr-x prueba.txt")
                    elif(command == "pwd"):
                        print(homepath)
                    elif(command == "info"):
                        print(commands)
                else:
                    commandnotfound = commandnotfound + 1
                    if commandnotfound == len(commands):
                        print("Command not found: Work in progress...")
                    continue
    return line

while True:
    terminal = comLine()
    """if(terminal == "quit" or terminal == "exit"):
        print("Usuario desconocido")"""

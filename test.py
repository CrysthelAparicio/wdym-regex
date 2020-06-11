import re # Para las Regex
import os # Para el archivo
import subprocess as sp # Entradas y salidas

# ===============================================
# Ruteo
def getPath():
    actualPath = os.getcwd()[1:].split("/")
    retValue = ""
    newPath = []
    for path in actualPath:
        if(path != "home"):
            newPath.append(path)
    for path in newPath:
        if(path == actualPath[1]):
            retValue = path + ":~"
        else:
            retValue += "/" + path
    return retValue
# ===============================================



# ===============================================
# Analizador de entrada erronea 
def inputA(args, cmd, exists):
    # Busca si el comando ya está en list
    if(args[0] in exists):
        execute(cmd)
    else:
        # Sugiere la palabra y guarda lo que quiso decir como futuro comando
        answer = input(f"Did you mean '{cmd}'? 😅 [y/n]: ")
        if(answer):
            answer = answer.lower()
        if(not answer or answer[0] == 'y'):
            print()
            print("My job is to remember it, don't worry about it anymore 🥳")
            print()
            exists.append(args[0])
            args[0] = cmd
            execute(args)
        elif(answer[0] == 'n'):
            print()
            print("I think I'm not understanding you, let's try again 🤔")
            print()
        else:
            print("I think I'm not understanding you, let's try again 🤔")
        return exists
# ===============================================

# ===============================================
# Bloque de código que ejecuta el comando
def execute(args):
    try:
        if(args[0] == "ping" and len(args) == 2):
            args = [args[0], "-c", "4", args[1]]
        sp.call(args)
    except:
        print("")
        print(f"Command '{args}' not found ❌")
# ===============================================

# ===============================================


def writeFile(df_cmd, ping_cmd, ls_cmd):
    save = ""
    index = 0
    # Toma el comando y lo imprime, ejecuta lo que realmente hace el comando
    for index in range(len(df_cmd)):
        if(df_cmd[index] != ""):
            save += df_cmd[index]
            if(index + 1 < len(df_cmd)):
                save += "+"
    save += "#"
    index = 0
    for index in range(len(ls_cmd)):
        if(ls_cmd[index] != ""):
            save += ls_cmd[index]
            if(index + 1 < len(ls_cmd)):
                save += "+"
    save += "#"
    index = 0
    for index in range(len(ping_cmd)):
        if(ping_cmd[index] != ""):
            save += ping_cmd[index]
            if(index + 1 < len(ping_cmd)):
                save += "+"

    file = open("comanditos.txt", "w+")
    file.write(save)
    file.close()
# ===============================================


def main():
    exist = True
    save = ""
    df_cmd = []
    ping_cmd = []
    ls_cmd = []
    try:
        # Verifica el archivo para leerlo
        file = open("comanditos.txt", "r")
        save = file.readline()
        file.close()
        # si el archivo existe pero esta vacio no hace nada
        # si el archivo existe y no esta vacio, toma los datos leidos y los guarda en las listas
        if (len(save) >= 2):
            arraySaved = save.split("#")
            df_cmd = arraySaved[0].split("+")
            ping_cmd = arraySaved[1].split("+")
            ls_cmd = arraySaved[2].split("+")
    except IOError:
        # Si el archivo no existe, lo crea
        file = open("comanditos.txt", "w+")
        file.close()
    path = getPath()
    while exist:
        command = input(f"{path}:👉 ")
        if(re.match(r'^[Bb][Yy][Ee]$', command)):
            print()
            print("May the force be with you! 💫")
            print()
            # Escribe las sugerencias guardadas en un archivo txt
            writeFile(df_cmd, ping_cmd, ls_cmd)
            exist = False
        elif(command):
            args = command.split()
            if(len(args) > 0):
                if(args[0] == "df" or args[0] == "ping" or args[0] == "ls"):
                    execute(args)
                else:
                    if(re.match(r'^[asdfg][sdfgh]$', args[0])):
                        # Analiza df
                        inputA(args, "df", df_cmd)
                    elif(re.match(r'^[iop][yuiop][vbnm,][dfghj]$', args[0])):
                        # Analiza ping
                        inputA(args, "ping", ping_cmd)
                    elif(re.match(r'^[jklñ{][asdf]$', args[0])):
                        # Analiza ls
                        inputA(args, "ls", ls_cmd)
                    else:
                        print()
                        print("I try to understand you 👀")
                        print()
            else:
                print("I try to understand you 👀")
# ===============================================


# ===============================================
if '__main__' == __name__:
    main()
# ===============================================

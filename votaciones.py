# Votaciones

# Presentamos los dos candidatos para votar --check--
# Pedimos al usuario ingresar su voto --check--
# SI es voto valido agrega a la urna --check--
# Si es voto incorrecto pedimos que vuelva a intentar
# Le preguntamos al usuario si quiere realizar otro voto
# si o no.
# si responde si volvemos a preguntar
# si responde no preguntamos si quiere ver los resultados finales
# muestra resultados finales, ganador, numero de votos,y ganador
# Crea un archivo .txt con los votos y el ganador

## -- PENDIENTE -- ##
# arreglar en la funcion sorteddicc si hay empate, pues solo impreme un ganador

import functions


print("\n\t---- VOTACIONES ----\n")
print(" Estas son las votaciones para representante.")
print(" Escoja uno de los siguientes candidatos para su voto: ")
print(" Candidato 1: 'Lalo'")
print(" Candidato 2: 'Lulu'")
print(" Candidato 3: 'Persi'")
print("\nIngrese 'q' para salir.")

urna = []
cand1 = "lalo"
cand2 = "lulu"
cand3 = "persi"

flag = True
while flag:
    vote = input("\nIngrese el nombre del candidato para su voto: ").lower()
    if vote == 'q':
        print("\nGracias por participar")
        flag = False
    if vote == cand1 or vote == cand2 or vote == cand3:
        urna.append(vote)
        another_user = input("Desea que otro usuario realice el voto? ('y'/'n'): ")
        if another_user == "n":
            print("\nGracias por participar")
            flag = False
        else:
            continue

print("\n --- Resultados ---")
num_votos = len(urna)
print(f"Numero de votos en total: {num_votos}")


cf = functions.CountFrequency(urna)
winner = functions.sortedDicc(cf)
print(f"Con X votos el ganador es: {winner.capitalize()}")


print("\t\nGRACIAS")

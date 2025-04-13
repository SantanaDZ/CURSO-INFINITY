def saudacao_por_horario(horario):
    if 0 <= horario < 12:
        print("Bom dia!")
    elif 12 <= horario < 18:
        print("Boa tarde!")
    elif 18 <= horario <= 23:
        print("Boa noite!")
    else:
        print("Horário inválido. Informe um número entre 0 e 23.")


saudacao_por_horario(1)


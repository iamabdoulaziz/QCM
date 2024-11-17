

def ask_user_choice(_min, _max):
    answer_str = input(f'Quel est ton choix entre {str(_min)} et {str(_max)} ? : ')
    try:
        answer_int = int(answer_str)
        if not _min <= answer_int <= _max:
            print(f"Erreur : Tu dois rentrer un nombre entre {_min} et {_max} !")
            return ask_user_choice(_min, _max)
        return answer_int
    except ValueError:
        print("Erreur : Tu dois rentrer un nombre")
        return ask_user_choice(_min, _max)

choice = ask_user_choice(1, 4)
print("Ton choix est", choice)

from rock_paper_scissors_ai import Rock_Paper_Scissors_AI

username = input('username (case-sensitive): ')

rock_paper_scissors = Rock_Paper_Scissors_AI()
while True:
    rock_paper_scissors.play(
        username,
        nrounds = 9
    )
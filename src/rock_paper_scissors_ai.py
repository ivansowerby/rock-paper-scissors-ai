import csvine
import numpy as np
from random import randint
from time import sleep
from keyboard import read_key
from cursor import hide as hide_cursor, show as show_cursor
from hashlib import sha256

UNICODE = {
    'rock': '🪨',
    'paper': '📰',
    'scissors': '✂️'
}

UNICODE_REF = [
    'rock',
    'paper',
    'scissors'
]

def backspace(n: int) -> str:
    return '\b' * n

def sha256_encode(string: str) -> str:
    return sha256(string.encode('ascii')).hexdigest()

class Rock_Paper_Scissors_AI:

    def __init__(self) -> None:
        self.score = {
            'user': 0,
            'machine': 0,
            'tie': 0
        }
        self.user_record = {
            'rock': 0,
            'paper': 0,
            'scissors': 0
        }
        self.result = ''

        return None

    def __selected_wrap__(self, interger: int, increment: int) -> int:
        interger += increment
        if interger < 0 or interger > 2: interger %= 3
        return interger

    def __user_input__(self) -> str:
        selected = 0
        while True:
            print(''.join([
                backspace(2),
                UNICODE[UNICODE_REF[selected]]
            ]), end = '')

            key_stroke = read_key()

            if key_stroke == 'left' or key_stroke == 'a':
                selected = self.__selected_wrap__(selected, -1)
            elif key_stroke == 'right' or key_stroke == 'd':
                selected = self.__selected_wrap__(selected, 1)
            elif key_stroke == 'enter' or key_stroke == 'e':
                return UNICODE_REF[selected]
            sleep(0.4)
    
    def __binomial_move__(self, diviser: int) -> str:
        return UNICODE_REF[int(np.random.binomial(
            n = 2,
            p = diviser / 2
        ))]

    def __outcome__(self, user: str, machine: str) -> int:
        if user == machine:
            return 'tie'
        elif user == 'rock' and machine == 'scissors' or \
            user == 'paper' and machine == 'rock' or \
            user == 'scissors' and machine == 'paper':
            return 'user'
        elif user == 'rock' and machine == 'paper' or \
            user == 'paper' and machine == 'scissors' or \
            user == 'scissors' and machine == 'rock':
            return 'machine'
    
    def __save_record__(self, hash_id: str, csv_filename: str) -> None:
        csv_data = csvine.parse(csv_filename)
        
        coordinates = csvine.filter_for_coordinates(
            csv_data,
            header_key = 'hash_id',
            value = hash_id,
        )
        if coordinates == -1:
            coordinates = (0, len(csv_data))
            csv_data.append([hash_id, '0', '0', '0/0'])
        
        row = csv_data[coordinates[1]]

        win_rate = list(
            map(int, row[3].split('/'))
        )
        if self.result == 'user':
            row[1] = str(int(row[1]) + 1)
            win_rate[0] += 1
        else:
            if int(row[1]) > int(row[2]):
                row[2] = row[1]
            row[1] = '0'
        
        if self.result == 'user' or self.result == 'machine':
            win_rate[1] += 1

        row[3] = '/'.join(map(str, win_rate))
        
        csv_data[coordinates[1]] = row

        csvine.save(
            csv_data,
            csv_filename
        )

        if win_rate[0] != 0:
            win_rate = str(win_rate[0] / win_rate[1])
        else:
            win_rate = 'N/A'
        print(''.join([
            '\n-----------',
            '\n',
            '\nStatistics:',
            '\nwin streak: ',
            '\n  -current: ', row[1],
            '\n  -highest: ', row[2],
            '\nwin rate: ', win_rate,
            '\n',
            '\n-----------'
        ]))

    def play(self, username: str = None, csv_filename: str = None, nrounds: int = None, best_to: int = None):
        if nrounds == None and best_to == None:
            print('Error: at least one arguement, "nrounds" or "best_to", needs to be passed')
            return None
        elif nrounds != None and best_to != None:
            print('Error: only one arguement should be passed, either "nrounds" or "best_to"')
            return None
        elif best_to == None:
            best_to = -1

        if csv_filename == None:
            csv_filename = 'player_database.csv'
        elif csv_filename.endswith('csv') == False:
            csv_filename == ''.join([
                csv_filename,
                '.csv'
            ])

        self.__init__()
        print('\nRock🪨, Paper📰, Scissors✂️')
        if username == None:
            username = input('username (case-sensitive): ')

        hash_id = sha256_encode(
            username
        )

        print(end = '\n')
        rounds = 1
        hide_cursor()
        while True:
            if rounds == 1:
                machine = UNICODE_REF[randint(0, 2)]
            else:
                machine = self.__binomial_move__(
                    diviser = list(self.user_record)
                    .index(min(self.user_record))
                )

            user = self.__user_input__()
            self.user_record[user] += 1
            
            print(''.join([
                '  Vs  ', UNICODE[machine]
            ]), end = '')

            outcome = self.__outcome__(
                user,
                machine
            )
            self.score[outcome] += 1
            print(''.join([
                '  |  ',
                outcome,
            ]), end = '\n')
            sleep(0.5)
            
            if rounds == nrounds or self.score['user'] == best_to or self.score['machine'] == best_to:
                break
            rounds += 1
        
        if self.score['user'] > self.score['machine']:
            self.result = 'user'
        elif self.score['machine'] > self.score['user']:
            self.result = 'machine'
        else:
            self.result = 'tie'
        
        print(''.join([
            '\nFinal Score:',
            '\nuser: ', str(self.score['user']),
            '\nmachine: ', str(self.score['machine'])
        ]))

        self.__save_record__(
            hash_id,
            csv_filename
        )
        show_cursor()
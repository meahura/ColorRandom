import random


class color : 

    def __init__(self) -> None:
        pass

    def Color(text:str): 
        # list color in pyhton ! 
        ResetAll = "\033[0m"
        Bold       = "\033[1m"
        Dim        = "\033[2m"
        Underlined = "\033[4m"
        Blink      = "\033[5m"
        Reverse    = "\033[7m"
        Hidden     = "\033[8m" 
        # 'random color : text def color 16 color ' 
        random_ = random.randrange(1,16)
        if random_ == 1 : 
            print(f"\033[39m{ResetAll}{text}") 
        elif random_ == 2 : 
            print(f"\033[30m{Bold}{text}") 
        elif random_ == 3 : 
            print(f"\033[31m{Dim}{text}") 
        elif random_ == 4 : 
            print(f"\033[32m{Underlined}{text}") 
        elif random_ == 5 : 
            print(f"\033[33m{Blink}{text}") 
        elif random_ == 6 : 
            print(f"\033[34m{Reverse}{text}") 
        elif random_ == 7 : 
            print(f"\033[35m{ResetAll}{text}") 
        elif random_ == 8 : 
            print(f"\033[35m{Bold}{text}") 
        elif random_ == 9 : 
            print(f"\033[36m{Dim}{text}") 
        elif random_ == 10 : 
            print(f"\033[37m{Underlined}{text}") 

        elif random_ == 11 : 
            print(f"\033[90m{Blink}{text}") 
        elif random_ == 12: 
            print(f"\033[91m{Reverse}{text}") 
        elif random_ == 13: 
            print(f"\033[92m{ResetAll}{text}") 
        elif random_ == 14 : 
            print(f"\033[93m{Dim}{text}") 
        elif random_ == 15 : 
            print(f"\033[94m{Underlined}{text}")   

        else: 
            raise ValueError(f'\033[1mError value in text')

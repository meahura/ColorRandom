import random
import sys

class color : 
    def __init__(self) -> None:pass
    def Color(text:str): 
        # list color in pyhton ! 
        ResetAll = "\033[0m";Bold       = "\033[1m";Dim        = "\033[2m"
        Underlined = "\033[4m";Blink      = "\033[5m";Reverse    = "\033[7m";Hidden     = "\033[8m" 
        # colors
        Cyan = "\033[36m"  ; Purple = "\033[35m" ; blue = "\033[34" 
        Brown = "\033[33m" ; Dark_Gray = "\033[1;30m"

        # 'random color : text def color 16 color ' 
        random_ = random.randrange(1,21)
        if random_ == 1 :print(f"\033[39m{ResetAll}{text}")
        elif random_ == 2:print(f"\033[30m{Bold}{text}") 
        elif random_ == 3:print(f"\033[31m{Dim}{text}") 
        elif random_ == 4:print(f"\033[32m{Underlined}{text}") 
        elif random_ == 5:print(f"\033[33m{Blink}{text}") 
        elif random_ == 6:print(f"\033[34m{Reverse}{text}") 
        elif random_ == 7:print(f"\033[35m{ResetAll}{text}") 
        elif random_ == 8:print(f"\033[35m{Bold}{text}") 
        elif random_ == 9:print(f"\033[36m{Dim}{text}") 
        elif random_ == 10:print(f"\033[37m{Underlined}{text}") 
        elif random_ == 11:print(f"\033[90m{Blink}{text}") 
        elif random_ == 12:print(f"\033[91m{Reverse}{text}") 
        elif random_ == 13:print(f"\033[92m{ResetAll}{text}") 
        elif random_ == 14:print(f"\033[93m{Dim}{text}") 
        elif random_ == 15:print(f"\033[94m{Underlined}{text}")  
        elif random_ == 16:print(f"{Cyan}{text}")
        elif random_ == 17:print(f"{Purple}{text}") 
        elif random_ == 18:print(f"{blue}{text}")
        elif random_ == 19:print(f"{Brown}{text}")
        elif random_ == 20:print(f"{Dark_Gray}{text}")
        else:raise ValueError(f'\033[1mError value in text')
        # list color in pyhton ! 

# sys argv - input 
try : 
    ext = sys.argv[1:100]
    text =  " ".join(ext) 
    ResetAll = "\033[0m";Bold       = "\033[1m";Dim        = "\033[2m"
    Underlined = "\033[4m";Blink      = "\033[5m";Reverse    = "\033[7m";Hidden     = "\033[8m" 
    # 'random color : text def color 16 color ' 
            # colors
    Cyan = "\033[36m"  ; Purple = "\033[35m" ; blue = "\033[34" 
    Brown = "\033[33m" ; Dark_Gray = "\033[1;30m"

    random_ = random.randrange(1,21)
    
    if text == "-h" or text =="--help":
        print('''
[name File] [text] 

for example : colorMeakUP.py [text]
For Example to python code : color.Color() [Enter Text(String)]

OPTIONS
    -h --helo                           helo tools colorRandom
    -o --owner                          owner colorRandom''')
    elif text == "-o" or text == "--owner": 
        print('''\033[31m
            github : http://github.com/AhSiber 
            Telegram : https://t.me/SI_Developers
            virgool : http://virgool.io/@ahura 
''')

    elif random_ == 1 :print(f"\033[39m{ResetAll}{text}")
    elif random_ == 2:print(f"\033[30m{Bold}{text}") 
    elif random_ == 3:print(f"\033[31m{Dim}{text}") 
    elif random_ == 4:print(f"\033[32m{Underlined}{text}") 
    elif random_ == 5:print(f"\033[33m{Blink}{text}") 
    elif random_ == 6:print(f"\033[34m{Reverse}{text}") 
    elif random_ == 7:print(f"\033[35m{ResetAll}{text}") 
    elif random_ == 8:print(f"\033[35m{Bold}{text}") 
    elif random_ == 9:print(f"\033[36m{Dim}{text}") 
    elif random_ == 10:print(f"\033[37m{Underlined}{text}") 
    elif random_ == 11:print(f"\033[90m{Blink}{text}") 
    elif random_ == 12:print(f"\033[91m{Reverse}{text}") 
    elif random_ == 13:print(f"\033[92m{ResetAll}{text}") 
    elif random_ == 14:print(f"\033[93m{Dim}{text}") 
    elif random_ == 15:print(f"\033[94m{Underlined}{text}")
    elif random_ == 16:print(f"{Cyan}{text}")
    elif random_ == 17:print(f"{Purple}{text}") 
    elif random_ == 18:print(f"{blue}{text}")
    elif random_ == 19:print(f"{Brown}{text}")
    elif random_ == 20:print(f"{Dark_Gray}{text}")
    else:raise ValueError(f'\033[1mError value in text')
except: 
    pass

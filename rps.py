import random, termcolor, subprocess,time

def info_and_score():
    subprocess.call('clear', shell=True)
    info = """
    ██████╗░░░░██████╗░░░░░██████╗
    ██╔══██╗░░░██╔══██╗░░░██╔════╝
    ██████╔╝░░░██████╔╝░░░╚█████╗░
    ██╔══██╗░░░██╔═══╝░░░░░╚═══██╗
    ██║░░██║██╗██║░░░░░██╗██████╔╝
    ╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚═════╝░

    [*] [code]Box | Andrei A. Abd 2022.
    [*] Source : https://github.com/codeBOX-projects
    [*] Python game to implement Rock Paper Scissor, aginst computer player.

    [I] Winning Rules of the Rock Paper Scissor game as follows:

        > Rock  vs Paper   >> Paper   (wins)
        > Rock  vs Scissor >> Rock    (wins)
        > Paper vs Scissor >> Scissor (wins)
        
    [?] Select your choice:

        1 > Rock.
        2 > Paper.
        3 > Scissor.
    """
    print(info)
    
def players_values(value_input):
    if value_input == "1":
        value_input = termcolor.colored("\n Rock", 'white')
        return print(value_input)
    elif value_input == "2":
        value_input = termcolor.colored("\n Paper", 'white')
        return print(value_input)
    elif value_input == "3":
        value_input = termcolor.colored("\n Scissor", 'white')
        return print(value_input)
    elif value_input == "":
        pass
    else:
        pass
def result_game():
    global player_1_score, player_2_score
    result_win = """
    
    ██╗░░░██╗░█████╗░██╗░░░██╗
    ╚██╗░██╔╝██╔══██╗██║░░░██║
    ░╚████╔╝░██║░░██║██║░░░██║
    ░░╚██╔╝░░██║░░██║██║░░░██║
    ░░░██║░░░╚█████╔╝╚██████╔╝
    ░░░╚═╝░░░░╚════╝░░╚═════╝░
    
    ░██╗░░░░░░░██╗██╗███╗░░██╗
    ░██║░░██╗░░██║██║████╗░██║
    ░╚██╗████╗██╔╝██║██╔██╗██║
    ░░████╔═████║░██║██║╚████║
    ░░╚██╔╝░╚██╔╝░██║██║░╚███║
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
    """
    result_lose = """
    
    ██╗░░░██╗░█████╗░██╗░░░██╗
    ╚██╗░██╔╝██╔══██╗██║░░░██║
    ░╚████╔╝░██║░░██║██║░░░██║
    ░░╚██╔╝░░██║░░██║██║░░░██║
    ░░░██║░░░╚█████╔╝╚██████╔╝
    ░░░╚═╝░░░░╚════╝░░╚═════╝░
    
    ██╗░░░░░░█████╗░░██████╗███████╗
    ██║░░░░░██╔══██╗██╔════╝██╔════╝
    ██║░░░░░██║░░██║╚█████╗░█████╗░░
    ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░
    ███████╗╚█████╔╝██████╔╝███████╗
    ╚══════╝░╚════╝░╚═════╝░╚══════╝
    """
    result_Draw = """
    ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
    ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
    ██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
    ██║░░██║██╔══██╗██╔══██║░░████╔═████║░
    ██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
    ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░
    """
    if take_user_value == "2" and value_computer == "1" or take_user_value == "1" and value_computer == "3" or take_user_value == "3" and value_computer == "2":
        take_user_value == value_computer == ""
        player_1_score += 1
        subprocess.call('clear', shell=True)
        print(termcolor.colored(result_win, 'green'))
        time.sleep(1.5)
    elif take_user_value == "1" and value_computer == "1" or take_user_value == "2" and value_computer == "2" or take_user_value == "3" and value_computer == "3":
        take_user_value == value_computer == ""
        subprocess.call('clear', shell=True)
        print(result_Draw)
        time.sleep(1.5)
    elif take_user_value == "1" and value_computer == "2" or take_user_value == "3" and value_computer == "1" or take_user_value == "2" and value_computer == "3":
        take_user_value == value_computer == ""
        player_2_score += 1
        subprocess.call('clear', shell=True)
        print(termcolor.colored(result_lose, 'red'))
        time.sleep(1.5)
    else:
        pass
    
if __name__=='__main__':
    player_1_score = 0
    player_2_score = 0
    while True:
        try:
            info_and_score()
            print(termcolor.colored("\t" + "=" * 39 + "\n\t || Score || Human {} || Computer  {} ||".format(player_1_score,player_2_score) + "\n\t" + "=" * 39, 'yellow'))
            value_computer = str(random.randint(1,3))
            take_user_value = str(input("\nSelect Your Sign > "))
            print(termcolor.colored(f"[!] Human Choice: {take_user_value}",'yellow'))
            print(termcolor.colored(f"[!] Computer Choice: {value_computer}",'yellow'))
            time.sleep(1.5)
            result_game()
        except:
            pass
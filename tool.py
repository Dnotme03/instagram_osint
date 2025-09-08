#insta brute-force tool
# note:-
# made by dhani
# just for time worst 

import os
import time
import random
from datetime import datetime

def glow(text, color):
    ANSI = {
        'red': '\033[91;1m',
        'green': '\033[92;1m',
        'yellow': '\033[93;1m',
        'blue': '\033[94;1m',
        'magenta': '\033[95;1m',
        'cyan': '\033[96;1m',
        'white': '\033[97;1m',
        'pink': '\033[95;1m',
        'orange': '\033[38;5;208m',
        'reset': '\033[0m'
    }
    return f"{ANSI.get(color, ANSI['white'])}{text}{ANSI['reset']}"

#BANNER
def show_banner():
    banner = """
  _____   _  _    _____   _  __    _  __ __  _   _   _____  
 |  __ \\ | || |  |  __ \\ | |/ /   | |/ //_ || \\ | | / ____| 
 | |  | || || |_ | |__) || ' /    | ' /  | ||  \\| || |  __  
 | |  | ||__   _||  _  / |  <     |  <   | || . ` || | |_ | 
 | |__| |   | |  | | \\ \\ | . \\    | . \\  | || |\\  || |__| | 
 |_____/    |_|  |_|  \\_\\|_|\\_\\   |_|\\_\\ |_||_| \\_| \\_____| 
                                                            
"""
    print(glow(banner, "pink"))
    print(glow("               Developer : DARKKING", "orange"))
    print(glow("               Instagram brute-force  tool", "cyan"))
    print(glow("               Started at: ", "yellow") + str(datetime.now()))

def simulate_bruteforce(username, realname, contact):
    print(glow(f"\n[~] Starting brute-force on @{username}", "cyan"))
    start_time = time.time()
    duration = 300  # 5 minutes
    attempt = 0
    tried = set()

    #words
    base_words = [
        username, realname.replace(" ", ""), contact,
        "123456", "password", "ronaldo", "mylove", "loveyou", "darkking", "admin", "welcome",
        "insta123", "hackme", "forever", "baby", "sweetie", "king2025", "love@123"
    ]

    
    password_pool = set()
    for word in base_words:
        for i in range(50):  # <<< CHANGED: reduced loop for faster generation
            number = str(random.randint(100, 999))  # <<< CHANGED: only numbers between 100–999
            password_pool.add(word + number)
            password_pool.add(word + "@" + number)
            password_pool.add(word.capitalize() + number)
            password_pool.add(word.lower() + number)
    password_list = list(password_pool)
    random.shuffle(password_list)

    
    while time.time() - start_time < duration:
        if attempt >= 1000:
            break  # <<< CHANGED: Stop after 1000 attempts

        selected = random.sample(password_list, 5)
        for pwd in selected:
            if pwd in tried:
                continue
            attempt += 1
            tried.add(pwd)
            print(glow(f"\n[{attempt}] Trying password: ", "blue") + glow(pwd, "white"), end="", flush=True)
            for dot in "...":
                print(glow(dot, "yellow"), end="", flush=True)
                time.sleep(0.05)  # <<<
            print(glow(" Failed", "red"))
            time.sleep(0.05)  # <<<

        #a
        print(glow("\n1 sec brak", "cyan"))  # <<<
        time.sleep(0.1)  # <<<: faster delay
        print(glow("↪ don\n", "magenta"))  # <<<
        time.sleep(0.1)  # <<<

    print(glow("\n[✓] Brute-force  completed!", "green"))
    print(glow("[!] No valid password found. Instagram security is strong.", "red"))
    print(glow("Stay ethical 😎", "yellow"))

# === MAIN ===
def main():
    os.system("clear")
    show_banner()
    username = input(glow("\n[?] Enter Instagram username: ", "white")).strip()
    contact = input(glow("[?] Enter email or phone number: ", "white")).strip()
    dob = input(glow("[?] Enter date of birth (DD/MM/YYYY): ", "white")).strip()
    realname = input(glow("[?] Enter their real name: ", "white")).strip()

    print(glow("\n[+] Gathering  data from dark web...", "blue"))
    time.sleep(1)
    print(glow("[+] Cross-referencing breach records...", "blue"))
    time.sleep(1)
    print(glow("[+] Generating password permutations...", "blue"))
    time.sleep(1.5)

    simulate_bruteforce(username, realname, contact)

    print(glow("\n[✓]  data stored in imaginary vault 🧠", "magenta"))
    print(glow("Thank you for using D4RK K1NG tool 💀", "cyan"))


if __name__ == "__main__":
    main()

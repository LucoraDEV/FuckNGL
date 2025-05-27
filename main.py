import requests
import random
import time
import uuid
import sys
from colorama import init, Fore, Style

# Initialiser Colorama
init(autoreset=True)

# === Affichage "Script By" ===
print(Fore.CYAN + "Script By")
time.sleep(0.5)

# === Affichage du tag ASCII principal ===
ascii_tag = f"""{Fore.LIGHTYELLOW_EX}
 ▄█       ███    █▄   ▄████████  ▄██████▄     ▄████████    ▄████████ 
███       ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
███       ███    ███ ███    █▀  ███    ███   ███    ███   ███    ███ 
███       ███    ███ ███        ███    ███  ▄███▄▄▄▄██▀   ███    ███ 
███       ███    ███ ███        ███    ███ ▀▀███▀▀▀▀▀   ▀███████████ 
███       ███    ███ ███    █▄  ███    ███ ▀███████████   ███    ███ 
███▌    ▄ ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
█████▄▄██ ████████▀  ████████▀   ▀██████▀    ███    ███   ███    █▀  
▀                                            ███    ███              
"""
print(ascii_tag)
time.sleep(1)

# Quelques lignes vives (espaces colorés pour séparer visuellement)
print(Fore.LIGHTGREEN_EX + "\n\n\n")

# === Nouveau tag du nom du programme en rouge et orange ===
program_name_tag = (
    f"{Fore.GREEN}   ,d8888b                 d8b                                d8b \n"
    f"   88P'                    ?88                                88P \n"
    f"d888888P                    88b                              d88  \n"
    f"  ?88'    ?88   d8P d8888b  888  d88'      88bd88b  d888b8b  888  \n"
    f"  88P     d88   88 d8P' `P  888bd8P'       88P' ?8bd8P' ?88  ?88  \n"
    f" d88      ?8(  d88 88b     d88888b        d88   88P88b  ,88b  88b \n"
    f"d88'      `?88P'?8b`?888P'd88' `?88b,    d88'   88b`?88P'`88b  88b\n"
    f"                                                          )88     \n"
    f"                                                         ,88P     \n"
    f"                                                     `?8888P      "
)
print(program_name_tag)
time.sleep(1)

# === Suite de ton script ===

print(Fore.CYAN + "[INFO] Chargement du script...")
time.sleep(0.8)
print(Fore.CYAN + "[INFO] Initialisation...")
time.sleep(0.6)
print(Fore.CYAN + "[PRÊT] Lancement !\n")
time.sleep(0.5)

NGL_API_URL = "https://ngl.link/api/submit"
IP_CHECK_URL = "https://httpbin.org/ip"
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

DEFAULT_MESSAGES = [
    "Wsh y’avait genre personne en cours d’anglais, contrôle surprise ou fuite collective ? 😭",
    "Le mec a laissé son sac dans le couloir toute la journée… vol ou oubli intentionnel ? 👀",
    "Y’a encore eu une baston à la récré, mais cette fois c’était pour une place à la prise 😭🔌",
    "Le micro du prof de musique a buggé, ça a crié comme dans un film d’horreur 😭💀",
    "Y’a un mec qui a ramené une pizza en plein cours… et il a partagé avec personne 😤",
    "Les chiottes du 2e étage sont encore bouchées… qui met du PQ comme ça sérieux 😭",
    "Un prof a dit 'ouvrez Pronote' et 3 élèves ont littéralement disparu 😭📉",
    "Une alarme a sonné en plein DS… et tout le monde s’est regardé genre ‘c’est un signe ?’ 🔥",
    "La machine à café marche plus… j’vous jure c’est la fin du monde pour les terminales ☕💔",
    "Quelqu’un a écrit 'vive les vacances' sur le TNI… en avril. Motivation à -200.",
    "Y’avait un pigeon en salle de SVT… il assistait au cours ou il notait les absents ? 🐦",
    "Un élève a mis une sono dans son sac, on avait ambiance boîte à la cantine 🔊😂",
    "Le CPE a dit 'vous êtes fatigués ? Moi aussi'. Instant respect ✊",
    "Quelqu’un a ramené un oreiller en cours… respect au roi de la sieste 👑💤",
    "La sonnerie a pas marché ce matin, toute la classe en mode 'on vient ou pas ?' ⏰❓",
    "Y’avait un ballon coincé dans les lumières du gymnase… il date de 2018 je crois 😭",
    "Un gars s’est endormi avec son stylo dans la bouche… il s’est réveillé genre ‘j’ai loupé quoi ?’ 💤✍️",
    "Le tableau affichait 'journée portes ouvertes'… sauf qu’on était déjà enfermés 😭🚪",
    "Le prof a sorti 'j’ai eu pire que vous cette année'… ambiance 💀",
    "Un mec a crié 'j’ai eu 4' après avoir vu sa note, la classe a applaudi comme s’il avait 18 😂👏"
]

MODES = {
    "normal": (4.0, 5.0),
    "slow": (15.0, 25.0)
}

def get_ip_address():
    try:
        response = requests.get(IP_CHECK_URL)
        ip = response.json().get("origin", "Inconnue")
        print(Fore.GREEN + f"[INFO] Adresse IP détectée : {ip}")
    except Exception as e:
        print(Fore.RED + f"[ERREUR] Impossible de récupérer l'adresse IP : {e}")
        sys.exit(1)

def get_message_source():
    choice = input(Fore.MAGENTA + "[CHOIX] Utiliser les messages par défaut ou un message personnalisé ? (defaut/custom) : ").strip().lower()
    if choice == "custom":
        msg = input(Fore.YELLOW + "[ENTRÉE] Entrez le message à envoyer : ").strip()
        return "custom", msg
    else:
        return "defaut", None

def get_user_input():
    mode = input(Fore.MAGENTA + "[CHOIX] Choisissez le mode d'envoi (normal / slow) : ").strip().lower()
    if mode not in MODES:
        print(Fore.RED + "[ERREUR] Mode invalide. Choisissez 'normal' ou 'slow'.")
        sys.exit(1)

    username = input(Fore.YELLOW + "[ENTRÉE] Entrez le nom d'utilisateur NGL : ").strip()

    try:
        count = int(input(Fore.YELLOW + "[ENTRÉE] Combien de messages souhaitez-vous envoyer ? "))
        interval = int(input(Fore.YELLOW + "[ENTRÉE] Tous les combien de messages changer le device ID ? "))
    except ValueError:
        print(Fore.RED + "[ERREUR] Veuillez entrer un nombre valide.")
        sys.exit(1)

    return mode, username, count, interval

def generate_device_id():
    return str(uuid.uuid4())

def send_message(username, device_id, message_index, message_source, custom_message=None):
    message = custom_message if message_source == "custom" else random.choice(DEFAULT_MESSAGES)

    payload = {
        "username": username,
        "question": message,
        "deviceId": device_id,
        "gameSlug": "",
        "referrer": ""
    }

    try:
        response = requests.post(NGL_API_URL, data=payload, headers=HEADERS)
        if response.status_code == 200:
            print(Fore.GREEN + f"[OK] Message {message_index} envoyé.")
        elif response.status_code == 429:
            print(Fore.YELLOW + "[ATTENTE] Trop de requêtes. Pause de 2 minutes...")
            time.sleep(120)
        else:
            print(Fore.RED + f"[ERREUR] Réponse {response.status_code} : {response.text}")
    except Exception as e:
        print(Fore.RED + f"[ERREUR] Exception lors de l'envoi : {e}")

def main():
    get_ip_address()

    message_source, custom_message = get_message_source()
    mode, username, total_messages, device_change_interval = get_user_input()
    delay_min, delay_max = MODES[mode]

    device_id = generate_device_id()
    print(Fore.CYAN + f"[INFO] Device ID initial : {device_id}\n")

    for i in range(1, total_messages + 1):
        if i % device_change_interval == 0:
            device_id = generate_device_id()
            print(Fore.BLUE + f"[INFO] Nouveau Device ID : {device_id}")

        send_message(username, device_id, i, message_source, custom_message)
        time.sleep(random.uniform(delay_min, delay_max))

    print(Fore.GREEN + "\n[TERMINÉ] Tous les messages ont été envoyés !")

if __name__ == "__main__":
    main()

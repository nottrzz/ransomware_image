from cryptography.fernet import fernet
import os
from rich.console import Console
from rich.prompt import Prompt
from time import Sleep

console = Console()

#fungsi untuk generate key
def generate_key():
    return Fernet.generate_key()

#fungsi untuk enkripsi file
def encrypt_file(key, filename):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
        encrypted = fernet.encrypt(original)
        with open(filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)




# Fungsi untuk menampilkan menu utama
def display_main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[bold cyan] Pilih aksi: [/bold cyan]")
    console.print("1: Enkripsi")
    console.print("2: Dekripsi")
    console.print("3: Keluar")

# Fungsi untuk menampilkan sub menu
def display_sub_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[bold cyan] Pilih aksi: [/bold cyan]")
    console.print("1: Masukkan Direktori")
    console.print("2: Kembali")


# Fungsi untuk dekripsi file
def decrypt_file(key, filename):
    fernet Fernet (key)
    with open(filename, 'rb') as encrypted_file:
        encrypted encrypted_file.read()
    decrypted fernet.decrypt(encrypted)
    with open(filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Fungsi untuk melakukan enkripsi pada semua file gambar dalam direktori

def encrypt_images_in_directory(directory, key):
    for filename in os.listdir (directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath) and (filename.lower().endswith('.jpg') or filename.lower().endswith('.png')): encrypt_file(key, filepath)
                console.print(f"[bold green] {filename} berhasil dienkripsi.[/bold green]")

# Fungsi untuk melakukan dekripsi pada semua file gambar dalam direktori
def decrypt_images_in_directory(directory, key):
    for filename in os.listdir(directory):
            filepathos.path.join(directory, filename)
            if os.path.isfile(filepath) and (filename.lower().endswith('.jpg') or filename.lower().endswith('.png')):
                decrypt_file(key, filepath) 
                console.print(f"[bold green] {filename} berhasil didekripsi.[/bold green]")


# Fungsi untuk memilih aksi di menu utama

def main menu():
    while True:
        display main_menu()
        action Prompt.ask("[bold cyan] Masukkan pilihan [/bold cyan]", choices=["1", "2", "3"])
        if action '1':
            sub_menu("enkripsi")
        elif action="2": sub_menu("dekripsi")
        elif action == "3":
            console.print("[bold cyan] Keluar dari program. Sampai jumpa![/bold cyan]")
            break

#Fungsi untuk memilih aksi di sub menu (enkripsi/dekripsi)
def sub menu(action_type):
    while True:
        display_sub_menu()
        action = Prompt.ask("[bold cyan] Masukkan pilihan [/bold cyan]", choices=["1", "2"])
        if action='1':
            directory Prompt.ask("Masukkan direktori tempat file gambar (.jpg/.png) berada")
            if not os.path.isdir(directory):
                console.print("[bold red]Direktori tidak ditemukan. Silakan coba lagi.[/bold red]")
                sleep(2)
                continue
            if action type "enkripsi":
                key generate_key()
                encrypt_images_in_directory(directory, key)
                console.print(f"[bold yellow] Kunci enkripsi Anda: {key.decode()}[/bold yellow]") #Menampilkan kunci enkripsi, bisa disimpan secara aman
                while True:
                    confirmed Prompt.ask("[bold cyan]Apakah Anda sudah mencatat kunci enkripsi? (y/n)[/bold cyan]", choices=["y", "n"])
                    if confirmed 'y':
                        break
            elif action_type == "dekripsi":
                key Prompt.ask("Masukkan kunci enkripsi").encode()
                decrypt_images_in_directory(directory, key)
                    break
                elif action '2':
                    return #Kembali ke menu utama

# Memilih aksi utama
main_menu()
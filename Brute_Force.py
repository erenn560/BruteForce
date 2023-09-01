import itertools
import string

def bruteforce_attack(password):
    chars = string.digits  # Sadece rakam karakterlerini kullan
    attempts = 0
    max_length = 5  # Tahmin edilen maksimum parola uzunluğu
    flag = False

    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            print(guess)  # Tahminleri ekrana yazdır

            if guess == password:
                return (attempts, guess)
    
    return (attempts, None)

password = input("Kırmak istediğiniz parolayı girin: ")
attempts, guess = bruteforce_attack(password)
if guess:
    print(f"Parola {attempts} denemede kırıldı. Parola: {guess}.")
else:
    print(f"{attempts} deneme sonucu parola kırılamadı.")

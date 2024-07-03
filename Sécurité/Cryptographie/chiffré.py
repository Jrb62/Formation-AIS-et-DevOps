from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import hashlib

# génère la paire de clés
def generer_cle_asymetrique():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    return private_key, private_key.public_key()

# encrypt le message
def chiffre(message, public_key):
    return public_key.encrypt(message.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

message_original = input("Entrez votre message : ")
private_key, public_key = generer_cle_asymetrique()
message_chiffre = chiffre(message_original, public_key)

# écris tout dans les fichiers
with open("cle_publique.pem", "w") as f:
    f.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo).decode())
with open("cle_privee.pem", "w") as f:
    f.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()).decode())
with open("message_chiffre.bin", "wb") as f:
    f.write(chiffre(message_original, public_key))

# Affiche les infos
print("Clé publique enregistrée dans 'cle_publique.pem'")
print("Clé privée enregistrée dans 'cle_privee.pem'")
print("Message chiffré enregistré dans 'message_chiffre.bin'")
print("Message chiffré:", message_chiffre.hex())

# Calcule le hash est l'enregistre dans un fichier
try:
    with open('message_chiffre.bin', 'rb') as file:
        hash_value = hashlib.sha256(file.read()).hexdigest()
        print(f"La signature est : {hash_value}")
        with open('hash.txt', 'w') as hash_file:
            hash_file.write(hash_value)
            print(f"Le hachage a été enregistré dans hash.txt")
except FileNotFoundError:
    print(f"Fichier hash.txt introuvable.")
except Exception as e:
    print(f"Erreur lors du calcul du hachage : {e}")

input("Appuyez sur Entrée pour quitter...")

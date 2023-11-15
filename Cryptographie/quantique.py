import pyspx.shake_128f as sphincs
import os

# Génération de clés : clé privée + clé publique
seed = os.urandom(sphincs.crypto_sign_SEEDBYTES)
public_key, secret_key = sphincs.generate_keypair(seed)

# Signature du message et vérification de la signature
message = b"Tony mon ami pour la vie"
signature = sphincs.sign(message, secret_key)
valid = sphincs.verify(message, signature, public_key)

print("Message:", message)
print("Signature valide?", valid)

# Vérification d'un message modifié + signature
message_modifie = b"Tony mon ami pour la vie"
valid_modifie = sphincs.verify(message_modifie, signature, public_key)

print("Message modifié:", message_modifie)

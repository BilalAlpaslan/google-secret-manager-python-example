

from utils import SecretManager

secret = SecretManager("neon-radius-312707")

print(secret.get_secret('DENEME_SECRET'))

print(secret.get_secret('DENEME_SECRET', 'prod'))
print(secret.get_secret('DENEME_SECRET', 'dev'))

import hashlib

from .poll_app import SALT_KEY


def generate_password_hash(password) -> str:
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        SALT_KEY.encode(),
        100000
    ).hex()
    return password_hash


def check_password_hash(password_hash, candidate) -> bool:
    candidate_hash = generate_password_hash(candidate)
    return password_hash == candidate_hash

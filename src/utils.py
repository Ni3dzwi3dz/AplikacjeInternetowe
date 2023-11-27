# Probably will move this functions somwhere. One day...
import binascii
import hashlib
import os


def hash_password(password: str):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    return (
        salt
        + binascii.hexlify(
            hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt, 100000)
        )
    ).decode("ascii")


def compare_password(stored_password: str, provided_password: str):
    salt = stored_password[:64]
    pwdhash = hashlib.pbkdf2_hmac(
        "sha512", provided_password.encode("utf-8"), salt.encode("ascii"), 100000
    )
    pwdhash = binascii.hexlify(pwdhash).decode("ascii")
    return pwdhash == stored_password[64:]

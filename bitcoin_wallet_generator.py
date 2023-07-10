#!/usr/bin/python3

import os
import binascii
import ecdsa
import requests
import hashlib
import base58

# Generate Bitcoin wallet key
def generate_btc_wallet_key():
    # Generate a random 32-byte private key
    private_key = os.urandom(32)
    # Use the SECP256k1 curve
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    # Get the public key in compressed format
    public_key = ('02' if vk.to_string()[-1] % 2 == 0 else '03') + binascii.hexlify(vk.to_string()[:32]).decode('utf-8')
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(binascii.unhexlify(public_key)).digest())
    # Add the version byte
    extended_ripemd160 = '00' + ripemd160.hexdigest()
    # Double hash using SHA256 to get the checksum
    checksum = hashlib.sha256(hashlib.sha256(binascii.unhexlify(extended_ripemd160)).digest()).hexdigest()[:8]
    bin_addr = extended_ripemd160 + checksum
    # Convert binary address to base58
    wallet_key = base58.b58encode(binascii.unhexlify(bin_addr))
    return wallet_key, binascii.hexlify(private_key).decode()

# Set the file name for the output
filename = "wallet_key_balance.txt"

while True:
    # Generate a new wallet key and private key
    wallet_key, private_key = generate_btc_wallet_key()

    # You need an API key to check balance from blockchain.com
    url = f'https://api.blockchain.info/q/addressbalance/{wallet_key.decode()}'
    response = requests.get(url)
    balance = int(response.text)

    # If balance is greater than zero, print and save to file
    if balance > 0:
        print(f"Wallet Key: {wallet_key}\nPrivate Key: {private_key}\nBalance: {balance} satoshi\n")

        with open(filename, "a") as f:
            f.write(f"Wallet Key: {wallet_key}\nPrivate Key: {private_key}\nBalance: {balance} satoshi\n")
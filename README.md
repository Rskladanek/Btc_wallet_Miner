Bitcoin Wallet Generator and Balance Checker
This Python script generates Bitcoin wallets (private-public key pairs) and checks their balance using the Blockchain.com API.

Disclaimer:
Please do not use this script for illegal activities. It is illegal and unethical to try and access Bitcoin wallets that do not belong to you. This script is for educational purposes only, such as generating new wallets for yourself and checking their balances.

Usage
Make sure you have Python 3.6 or later installed. You can download it here.

Install the required Python libraries if you haven't already done so:

Copy code
pip install ecdsa requests base58
Clone this repository:
bash
Copy code
git clone https://github.com/Rskladanek/bitcoin-wallet-generator.git
Run the script:
Copy code
python3 bitcoin_wallet_generator.py
The script will run indefinitely, generating Bitcoin wallets and checking their balance on the Blockchain.com API. If it finds a wallet with a balance, it will print the wallet key and the balance to the console and write them to a file named wallet_key_balance.txt.

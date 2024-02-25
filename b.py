import pandas as pd
from eth_account import Account
from eth_utils import to_hex
from web3 import Web3

# Function to create a Metamask-style wallet
def create_metamask_wallet():
    account = Account.create()
    private_key_hex = to_hex(account._private_key)
    seed_bytes = bytes.fromhex(private_key_hex[2:])  # Remove the '0x' prefix before converting to bytes
    seed_phrase = to_hex(seed_bytes)
    address = account.address
    return seed_phrase, private_key_hex, address

# Function to save seed phrase, private key, and address to an Excel sheet
def save_to_excel(wallet_data, file_name='walletwithsedd_info.xlsx'):
    df = pd.DataFrame(wallet_data, columns=['Seed Phrase', 'Private Key', 'Address'])
    df.to_excel(file_name, index=False)
    print(f"Data saved to {file_name}")

# Main program
if __name__ == "__main__":
    # Create 100 Metamask-style wallets
    wallet_data = {'Seed Phrase': [], 'Private Key': [], 'Address': []}
    for _ in range(100):
        seed_phrase, private_key, address = create_metamask_wallet()
        wallet_data['Seed Phrase'].append(seed_phrase)
        wallet_data['Private Key'].append(private_key)
        wallet_data['Address'].append(address)

    # Save seed phrases, private keys, and addresses to Excel sheet
    save_to_excel(wallet_data)

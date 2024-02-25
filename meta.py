import pandas as pd
from web3 import Web3
from eth_account import Account

# Function to create a Metamask-style wallet
def create_metamask_wallet():
    account = Account.create()
    private_key = account._private_key.hex()
    address = account.address
    return private_key, address

# Function to save seed phrase and private key to an Excel sheet
def save_to_excel(wallet_data, file_name='wallet_info.txt'):
    df = pd.DataFrame(wallet_data, columns=['Private Key', 'Address'])
    df.to_excel(file_name, index=False)
    print(f"Data saved to {file_name}")

# Main program
if __name__ == "__main__":
    # Create 100 Metamask-style wallets
    wallet_data = {'Private Key': [], 'Address': []}
    for _ in range(100):
        private_key, address = create_metamask_wallet()
        wallet_data['Private Key'].append(private_key)
        wallet_data['Address'].append(address)

    # Save private keys and addresses to Excel sheet
    save_to_excel(wallet_data)

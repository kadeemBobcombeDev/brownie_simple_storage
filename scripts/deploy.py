from brownie import accounts, config


def deploy_simple_storage():
    account = accounts[0]
    # print(account)
    # print("account is above this")

    # load from brownie accounts
    # account = accounts.load("mm-rink")

    # account = accounts.add(config["wallets"]["from_key"])
    print(account)


def main():
    deploy_simple_storage()
    # print("Hello!")

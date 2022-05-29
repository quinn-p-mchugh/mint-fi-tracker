from mintapi import Mint
from pathlib import Path
from configparser import ConfigParser

config = ConfigParser()
config.read(Path(__file__).parent / "config.ini")

mint: Mint = Mint(
    email=config["MintCredentials"]["Email"],
    password=config["MintCredentials"]["Password"],
    # mfa_method="sms",
    # mfa_input_callback=None,
    # mfa_token=None,
    intuit_account=None,
    session_path=None,
    imap_account=None,
    imap_password=None,
    imap_server=None,
    imap_folder="INBOX",
    wait_for_sync=True,
    wait_for_sync_timeout=300,
    use_chromedriver_on_path=False,
)

# Get basic account information
print(mint.get_account_data())

# Get bills
print(mint.get_bills())

# Close session and exit cleanly from selenium/chromedriver
mint.close()

# Initiate an account refresh
mint.initiate_account_refresh()

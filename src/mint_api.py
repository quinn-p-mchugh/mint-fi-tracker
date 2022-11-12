import json
import pandas as pd
import yagmail
import plotly.express as px
import plotly.graph_objects as go

from mintapi import Mint
from pathlib import Path
from configparser import ConfigParser
from expense_categories import CATEGORIES, get_expense_categories

CONFIG = ConfigParser()
CONFIG.read(Path(__file__).parent / "config.ini")
MINT_TRANSACTIONS_CSV = (
    Path(__file__).parents[1] / "data/mint_transactions.csv"
)
print(MINT_TRANSACTIONS_CSV)
MINT_TRANSACTIONS_JSON = (
    Path(__file__).parents[1] / "data/mint_transactions.json"
)
EXPENSE_CATEGORIES_OVER_TIME_PNG = (
    Path(__file__).parents[0] / "img/expense_categories_over_time.png"
)
EXPENSE_CATEGORIES_OVER_TIME_HTML = (
    Path(__file__).parents[0] / "expense_categories_over_time.html"
)


def import_mint_transactions(
    config, mint_transactions_csv, mint_transactions_json
):
    """Extract Mint transactions using (unofficial) Mint API and store them in JSON & CSV files.

    Args:
        config (ConfigParser): Config file with Mint account credentials.
        mint_transactions_csv (Path): The path of the CSV file used to store Mint transactions.
        mint_transactions_json (Path): The path of the JSON file used to store Mint transactions.
    """

    mint = Mint(
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

    mint_transactions = mint.get_transaction_data()
    with open(mint_transactions_json, "w") as f:
        json.dump(mint_transactions, f)
    mint_transactions = pd.json_normalize(mint_transactions)
    mint_transactions.to_csv(mint_transactions_csv)

    mint.close()

    # Initiate an account refresh
    mint.initiate_account_refresh()


if MINT_TRANSACTIONS_CSV.is_file():
    transactions = pd.read_csv(MINT_TRANSACTIONS_CSV)[
        [
            "category.parentName",
            "category.parentId",
            "category.name",
            "category.id",
            "id",
            "date",
            "description",
            "amount",
            "isExpense",
            "type",
            "discretionaryType",
            "accountRef.name",
            "accountRef.type",
        ]
    ]
else:
    import_mint_transactions(
        CONFIG, MINT_TRANSACTIONS_CSV, MINT_TRANSACTIONS_JSON
    )

# Add column for grouping by month
transactions["yearMonth"] = pd.to_datetime(transactions["date"]).map(
    lambda dt: dt.replace(day=1)
)


expenses = transactions[
    transactions["category.name"].isin(get_expense_categories())
]
print(expenses)

expenses_by_category = expenses.groupby(
    ["yearMonth", "category.id"], as_index=False
).agg(
    {"amount": "sum", "category.parentName": "first", "category.name": "first"}
)


def expense_categories_over_time():
    fig = px.bar(
        expenses_by_category.sort_values(by=["category.name"]),
        x="yearMonth",
        y="amount",
        color="category.name",
        color_discrete_sequence=px.colors.qualitative.Alphabet,
    )

    def add_legend_group(trace):
        for category in CATEGORIES.keys():
            if trace.name in CATEGORIES[category].keys():
                trace.update(
                    legendgroup=f"{category}",
                    legendgrouptitle_text=f"{category}",
                )

    fig.for_each_trace(lambda trace: add_legend_group(trace))

    fig.update_traces(legendgroup="Derp", selector=dict(name="ATM Fee"))

    fig.update_layout(
        template="plotly_white",
        yaxis=dict(dtick=1000),
        xaxis=dict(dtick="M1", showgrid=True),
        legend=dict(groupclick="toggleitem", title_text="Expense Categories"),
    )

    fig.write_html(
        EXPENSE_CATEGORIES_OVER_TIME_HTML,
        full_html=False,
        include_plotlyjs="cdn",
    )
    fig.write_image(EXPENSE_CATEGORIES_OVER_TIME_PNG)
    fig.show()


expense_categories_over_time()


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename


def send_mail(
    send_from: str, subject: str, text: str, send_to: list, files=None
):
    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = ", ".join(send_to)
    msg["Subject"] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f) as fil:
            ext = Path(f).stem
            attachedfile = MIMEApplication(fil.read(), _subtype=ext)
            attachedfile.add_header(
                "content-disposition", "attachment", filename=basename(f)
            )
        msg.attach(attachedfile)

    smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


username = CONFIG["GMailCredentials"]["Email"]
password = CONFIG["GMailCredentials"]["Password"]

send_mail(
    send_from=username,
    subject="test",
    text="text",
    send_to=CONFIG["GMailCredentials"]["Email"]
    files=[
        "C:/Users/Quinn/Documents/Code Repositories/mint-fi-tracker/src/expense_categories_over_time.html",
        "C:/Users/Quinn/Documents/Code Repositories/mint-fi-tracker/src/expense_categories_over_time.html",
    ],
)


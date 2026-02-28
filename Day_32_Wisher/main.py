# ----------------------------------------------------- IMPORTS ----------------------------------------------------------- #
import datetime as dt
import random
import smtplib
import pandas

# ----------------------------------------------------- CONSTANTS --------------------------------------------------------- #

# CHANGE TO YOUR EMAIL AND APP PASSWORD

MY_GMAIL = "WRITE YOUREMAIL HERE @gmail.com"
MY_PASSWORD = "WRITE YOUR APP PASSWORD FOR THE EMAIL ACCOUNT HERE"
SMTP_FOR_GMAIL = "smtp.gmail.com"

# ----------------------------------------------------- CURRENT DATE ------------------------------------------------------ #
current_dt = dt.datetime.now()
current_dt_day = current_dt.day
current_dt_month = current_dt.month
# ----------------------------------------------------- BIRTHDAYS DF ------------------------------------------------------ #
birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_total_names = birthdays_df.name

# ----------------------------------------------------- PROGRAM ----------------------------------------------------------- #
for each_person in range(len(birthdays_total_names)):

    birthdates_day = list(birthdays_df.day)[each_person]
    birthdates_month = list(birthdays_df.month)[each_person]

    if current_dt_month == birthdates_month and current_dt_day == birthdates_day:
        letter_file = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(f"{letter_file}", "r") as letter_format:
            letter_format_read = letter_format.read()
            letter_to_send = letter_format_read.replace(
                "[NAME]", f"{birthdays_total_names[each_person]}")

            birthday_peroson_email = birthdays_df.email[each_person]
            with smtplib.SMTP(SMTP_FOR_GMAIL) as connection:
                connection.starttls()
                connection.login(user=MY_GMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_GMAIL,
                                    to_addrs=birthday_peroson_email, msg=f"Subject:Happy Birthday\n\n{letter_to_send}")

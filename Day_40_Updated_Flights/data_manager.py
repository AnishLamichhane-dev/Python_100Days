import gspread
import pandas
import json


class DataManager:

    def __init__(self):
        self.client_gspread = gspread.service_account(
            filename="credentials.json")

        self.opens_google_sheets = self.client_gspread.open("FlightDeals")

        self.first_tab_of_google_sheets = self.opens_google_sheets.get_worksheet(
            0)

        self.dataframe_of_sheets = pandas.DataFrame(
            self.first_tab_of_google_sheets.get_all_records())

        self.list_of_all_cities_iata_code_in_sheets = list(
            self.dataframe_of_sheets["IATA Code"])
        self.list_of_all_cities_lowest_price_in_sheets = list(
            self.dataframe_of_sheets["Lowest Price"])

    def ask_email(self):
        """
        Ask user email twice and repeat until its the same.
        """
        self.user_email = "a" # input("What is your email?:\n")
        rechecking_email = "a" #input("Type your email again.\n")
        if self.user_email == rechecking_email:
            pass
        else:
            self.ask_email()

    def ask_user_info(self):
        """
        Ask first name, last name and email.
        """

        print("Welcome to Anish's Flight Club.")
        print("We find the best flight deals and email you.")
        self.first_Name = "a" #input("What is you first name?:\n")
        self.last_name = "a" #input("What is your last name?:\n")
        self.ask_email()
        print("You're in the club!")

    def upload_user_data(self):
        """
        Uploads user first name, last name and email to spreadsheet.
        """
        self.second_tab_of_google_sheets = self.opens_google_sheets.get_worksheet(
            1)
        user_info = [self.first_Name, self.last_name, self.user_email]
        self.second_tab_of_google_sheets.append_row(user_info)

    def cheapest_flight_data(self, response_amadeus, each_city_iata_code):
        """
        Gets the lowest flight price and also the city name and code for each.
        """

        all_data = response_amadeus.data
        lowest_price_data = all_data[0]

        self.all_departure_info = lowest_price_data["itineraries"][0]["segments"]

        segment_number = 0
        self.list_of_total_stop_overs = []
        for each_departure in self.all_departure_info:
            self.list_of_total_stop_overs.append(
                self.all_departure_info[segment_number]["departure"]['iataCode'])
            segment_number += 1

        self.lowest_grand_total = float(
            lowest_price_data["price"]["grandTotal"])
        self.arrival_time_for_cheapest_flight = lowest_price_data["itineraries"][0]["segments"][0]["arrival"]["at"].split("T")[
            0]

        self.cell = self.first_tab_of_google_sheets.find(
            each_city_iata_code, in_column=2)
        self.city_name = self.first_tab_of_google_sheets.acell(
            f"A{self.cell.row}").value
        self.city_code = self.first_tab_of_google_sheets.acell(
            f"B{self.cell.row}").value

    def update_sheet(self):
        """
        Updates the cell with lower price.
        """

        row_to_change = self.cell.row

        self.first_tab_of_google_sheets.update_cell(
            row_to_change, 3, f"{self.lowest_grand_total}")

    def get_all_user_emails(self):
        self.client_gspread_2ndTab = gspread.service_account(
            filename="credentials.json")

        opens_google_sheets_2ndTab = self.client_gspread_2ndTab.open("FlightDeals").get_worksheet(1)

        self.all_emails = opens_google_sheets_2ndTab.col_values(3)[1:]
        

import gspread
import pandas


class DataManager:

    def __init__(self):
        self.client_gspread = gspread.service_account(
            filename="credentials.json")

        self.opens_google_sheets = self.client_gspread.open("FlightDeals")

        self.first_tab_of_google_sheets = self.opens_google_sheets.sheet1

        self.dataframe_of_sheets = pandas.DataFrame(
            self.first_tab_of_google_sheets.get_all_records())

        self.list_of_all_cities_iata_code_in_sheets = list(
            self.dataframe_of_sheets["IATA Code"])
        self.list_of_all_cities_lowest_price_in_sheets = list(
            self.dataframe_of_sheets["Lowest Price"])

    def cheapest_flight_data(self, response_amadeus, each_city_iata_code):
        """
        Gets the lowest flight price and also the city name and code for each.
        """

        all_data = response_amadeus.data
        lowest_price_data = all_data[0]
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

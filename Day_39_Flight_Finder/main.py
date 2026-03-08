from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch


notification_manager = NotificationManager()
data_manager = DataManager()

CITY_NUMBER_FOR_LIST = 0
for each_city_iata_code in data_manager.list_of_all_cities_iata_code_in_sheets:

    flight_search = FlightSearch(each_city_iata_code)
    data_manager.cheapest_flight_data(
        flight_search.response_amadeus, each_city_iata_code)

    if data_manager.lowest_grand_total < float(data_manager.list_of_all_cities_lowest_price_in_sheets[CITY_NUMBER_FOR_LIST]):
        data_manager.update_sheet()
        notification_manager.send_sms(
            data_manager.lowest_grand_total, data_manager.arrival_time_for_cheapest_flight, flight_search.DATE_FOR_FLIGHT, data_manager.city_name, data_manager.city_code)
    CITY_NUMBER_FOR_LIST += 1

# When you complete watching the movie then delete that number from the txt file.

from bs4 import BeautifulSoup

with open("top100movies.html", "r", encoding="utf-8") as movies_html_file:
    entire_html_code = movies_html_file.read()


soup = BeautifulSoup(entire_html_code, "html.parser")

all_100_movies = soup.select(selector="span h2 strong")

with open("movies.txt", "w", encoding="utf-8") as txt_file_with_top_100_movies:
    for movie_rank in range(100, 0, -1):
        txt_file_with_top_100_movies.write(
            f"{all_100_movies[movie_rank].getText()}\n")

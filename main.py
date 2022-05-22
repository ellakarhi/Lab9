import random 

movie = {"Title":"The Batman","Year":"2022","Rated":"PG-13","Released":"04 Mar 2022","Runtime":"176 min","Genre":"Action, Crime, Drama","Director":"Matt Reeves","Writer":"Matt Reeves, Peter Craig, Bill Finger","Actors":"Robert Pattinson, Zoë Kravitz, Jeffrey Wright","Plot":"When a sadistic serial killer begins murdering key political figures in Gotham, Batman is forced to investigate the city's hidden corruption and question his family's involvement.","Language":"English","Country":"United States","Awards":"2 wins & 7 nominations","Poster":"https://m.media-amazon.com/images/M/MV5BMDdmMTBiNTYtMDIzNi00NGVlLWIzMDYtZTk3MTQ3NGQxZGEwXkEyXkFqcGdeQXVyMzMwOTU5MDk@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"8.0/10"},{"Source":"Rotten Tomatoes","Value":"85%"},{"Source":"Metacritic","Value":"72/100"}],"Metascore":"72","imdbRating":"8.0","imdbVotes":"464,193","imdbID":"tt1877830","Type":"movie","DVD":"19 Apr 2022","BoxOffice":"$369,202,709","Production":"N/A","Website":"N/A","Response":"True"}

def the_year():
  if movie["Year"] == "2022":
    return "This year"
  else:
    return "in " + movie["Year"]

def work_des():
  num = random.randint (0,1)
  if num == 0:
    return "beautiful work of art"
  elif num == 1:
    return "masterpiece"
  
def pg_level():
  if movie["Rated"] == "G":
    return " is sutable for all ages so bring your family! "
  if movie["Rated"] == "PG":
    return " has parental guidance suggested when watching as some material may not be suitable for children. "
  if movie["Rated"] == "PG-13":
    return "  is rated PG - 13 so, parents are strongly cautioned as some material may be inappropriate for children under 13. "
  if movie["Rated"] == "R":
    return " has very mature material. Parents are warned to look into the films contents before allowing children to watch. "
    

def awards():
  if awards != None:
    return movie["Title"] + " has had " + movie["Awards"]
  else:
    return

def box_time():
  if movie["Year"] == "2022":
    return " so far! "
  else:
    return "! "

def rating_sources():
  rating1 = movie["Ratings"][0]["Value"]
  rating2 = movie["Ratings"][1]["Value"]
  rating3 = movie["Ratings"][2]["Value"]
  if rating1.strip("/10") > "6.0":
    if rating2.strip("%") > "70":
      if rating3.strip("/100") > "60":
        return " This movie was received well by critics and deserves a watch! "
      else:
        " This movie is okay so you can watch it if you like but there are better movies to waste your time with. "
    else:
      return " This movie is nothing special but you can watch it if you want. "
  else:
    return " This movie sucks. Don't waste your time unless you like garbage movies for the funny factor of it. "

def blog():
  print(movie["Title"] + " is about " + movie["Plot"] + movie["Title"] + " was released " + the_year() +", with a cast of famous actors " + movie["Actors"] +". The writers, " + movie["Writer"] + "and director " + movie["Director"] + " created a " + work_des() + " that has made " + movie["BoxOffice"] + " in the box office" + box_time() + movie["Title"] + pg_level() + movie["Title"] + "is a " + movie["Genre"] + "movie, and has a runtime of " + movie["Runtime"] + ". " + awards() + "." + rating_sources() + "It has been given a rating of " + movie["Ratings"][0]["Value"] + " by " + movie["Ratings"][0]["Source"] + ", " + movie["Ratings"][1]["Source"] + " has giving it a rating of " + movie["Ratings"][1]["Value"] + ", and " + movie["Ratings"][2]["Source"] + " has rated it a " + movie["Ratings"][2]["Value"] + ".")
      

blog()
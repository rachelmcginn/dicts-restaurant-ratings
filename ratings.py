"""Restaurant rating lister."""


# put your code here
def get_restaurant_ratings(file_name):

    restaurant_ratings_dict = {}
    restaurant_ratings_list = []

    file_name = open(file_name)

    for line in file_name:
        line = line.rstrip()
        restaurant_ratings_list.append(line.split(":"))
  
    for current_list in range(0,len(restaurant_ratings_list)):
        restaurant, rating = restaurant_ratings_list[current_list][0], restaurant_ratings_list[current_list][1]
        restaurant_ratings_dict[restaurant] = rating

    restaurant_ratings_tuple = restaurant_ratings_dict.items()
    restaurant_ratings_tuple = sorted(restaurant_ratings_tuple)
    
    for i in range(0,len(restaurant_ratings_tuple)):
        message = print(f"{restaurant_ratings_tuple[i][0]} is rated {restaurant_ratings_tuple[i][1]}.")

    return message

get_restaurant_ratings("scores.txt")
    

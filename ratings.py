"""Restaurant rating lister."""

#read the ratings from the file
#open the file
    #look at each line in the file
    #split into a list 
#sort the list alphabetically 

#items() 
#sorted()




# put your code here
def get_restaurant_ratings(file_name):

    restaurant_ratings = {}
    restaurant_ratings_list = []

    file_name = open(file_name)

    for line in file_name:
        line = line.rstrip()
        restaurant_ratings_list.append(line.split(":"))
    #print(restaurant_ratings_list)
    for current_list in restaurant_ratings_list: #for each sublist 
        #restaurant_ratings = restaurant_ratings_list[0]
        #restaurant_ratings[1] = restaurant_ratings[1]

        restaurant = restaurant_ratings_list[0]
        #ratings = restaurant_ratings[1]

        #restaurant_ratings[restaurant] = ratings

    print(restaurant)
#     #print(restaurant_ratings)
#     print(restaurant_ratings_list)
#         #restaurant_ratings[key] = 'value'

# #print(restaurants)
get_restaurant_ratings("scores.txt")
    

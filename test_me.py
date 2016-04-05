"""Matt, Matt, Peter 4/4/2016

Practice: Restaurant Reviews
We're going to make a mini version of Yelp. There are local business listings and users can post reviews, with a rating and some text, of each business.

Make a class that represents a review: it will have "rating" and "review text" fields.
Make a class that represents a business: it will have "name" and a list of reviews fields.
Load the following data into those classes. Don't use raw_business_review_data for any further operations.
raw_business_review_data = [
  {
    'business_name': 'Salt & Straw',
    'reviews': [
      {'rating': 5, 'text': 'Lucious ice cream!'},
      {'rating': 4, 'text': 'Super tasty, but such a long line!'}
      {'rating': 2, 'text': 'Overrated, but I like sugar.'}
    ],
  },
  {
    'business_name': 'Voodoo Donuts',
    'reviews': [
      {'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
      {'rating': 5, 'text': 'Pink building is so cute!'}
      {'rating': 2, 'text': 'Diabetes inducing.'}
    ],
  },
]
Add a function to the business class that returns the average rating.
Implement searching by name: Prompt for the a name of a business, and print out the average rating for that business and one review.

Add a user class: it will have a "user name" field.

Add a "user name" field to the review class.
In real life, data like this is not hierarchical. This is so you can ask questions like "what are all the reviews I wrote?" Let's denormalize or break apart the hierarchy we currently have.

Add a "business name" field to the review class.
Remove the list of reviews field from the business class.
Load the following data into those refactored classes. Don't use these variables for any further operations.
raw_business_data = [
  {
    'business_name': 'Salt & Straw',
  },
  {
    'business_name': 'Voodoo Donuts',
  },
]
raw_user_data = [
  {'user_name': 'Abby'},
  {'user_name': 'Helen'},
  {'user_name': 'Bobby'},
]
raw_review_data = [
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 5, 'text': 'Lucious ice cream!'},
  {'user_name': 'Bobby', 'business_name': 'Salt & Straw', 'rating': 4, 'text': 'Super tasty, but such a long line!'},
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 2, 'text': 'Overrated, but I like sugar.'},
  {'user_name': 'Helen', 'business_name': 'Voodoo Donuts', 'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
  {'user_name': 'Bobby', 'business_name': 'Voodoo Donuts', 'rating': 5, 'text': 'Pink building is so cute!'},
  {'user_name': 'Abby', 'business_name': 'Voodoo Donuts', 'rating': 2, 'text': 'Diabetes inducing.'},
]
Re-implement the searching by name above.
Implement searching for reviews by user: Prompt for the a name of a user, and print out all reviews for that user.






"""

class Review:
  def __init__(self, business_name, user_name, rating, review):
    self.business_name = business_name
    self.user_name = user_name
    self.rating = rating
    self.review = review

  def __str__(self):
    my_str = "{} rating: {}".format(self.review, self.rating)
    return my_str

class Business:
    def __init__(self, business_name):
        self.business_name = business_name

    def __str__(self):
        return '{}'.format(self.business_name)

    # def return_average(self):
    #     my_value_counter = 0
    #     for i in self.review_list:
    #         my_value_counter += i['rating']
    #     my_average = (my_value_counter/len(self.review_list))
    #     return my_average

class User:
  def __init__(self, user_name):
    self.user_name = user_name

# def query_dict_for_reviews(dict, user_input_string):
#     for i in dict:
#         if user_business_search in i['business_name']:
#             average_counter = 0
#             my_list = []
#             for j in i['reviews']:
#                 average_counter += j['rating']
#                 my_list.append(j)
#             total_average = (average_counter/len(i['reviews']))
#             my_new_business = Business(i['business_name'], my_list)
#             print('Average: {}'.format(total_average))
#             print(my_list[0])



# raw_business_review_data = [
#   {
#     'business_name': 'Salt & Straw',
#     'reviews': [
#       {'rating': 5, 'text': 'Lucious ice cream!'},
#       {'rating': 4, 'text': 'Super tasty, but such a long line!'},
#       {'rating': 2, 'text': 'Overrated, but I like sugar.'}
#     ],
#   },
#   {
#     'business_name': 'Voodoo Donuts',
#     'reviews': [
#       {'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
#       {'rating': 5, 'text': 'Pink building is so cute!'},
#       {'rating': 2, 'text': 'Diabetes inducing.'}
#     ],
#   },
# ]

# salt_and_straw_rating_list = []
# voodoo_donuts_rating_list = []

# for i in raw_business_review_data[0]['reviews']:
#   salt_and_straw_rating_list.append(i)

# for i in raw_business_review_data[1]['reviews']:
#   voodoo_donuts_rating_list.append(i)

# rating_counter_salt = 0
# rating_counter_voodoo = 0

# for i in salt_and_straw_rating_list:
#   rating_counter_salt += i['rating']

# for i in voodoo_donuts_rating_list:
#   rating_counter_voodoo += i['rating']

# voodoo_donuts = Business('Voodoo Donuts', voodoo_donuts_rating_list)
# salt_and_straw = Business("Salt & Straw", salt_and_straw_rating_list)
def search_by_name(dict, user_input_string):
    for i in dict:
      if user_input_string in i['business_name']:
          my_average = get_average_by_search(dict, user_input_string)
          my_string = 'Average Rating: {}. Review: {}'.format(my_average, i['text'])
    return my_string

def get_average_by_search(dict, user_input_string):
    average_counter = 0
    for i in dict:
        if user_input_string in i['business_name']:
            average_counter += i['rating']
    my_average = (average_counter/len(i))
    return my_average

def search_by_user(dict, user_input_string):
    review_list = []
    count_number = 1
    for i in dict:
        if user_input_string in i['user_name']:
            if count_number > 0:
                my_line = "{}: {} {} {}".format(i['user_name'], i['text'], i['rating'], i['business_name'])
                count_number -= 1
            elif count_number <= 0:
                my_line = "{} {} {}".format(i['text'], i['rating'], i['business_name'])
            review_list.append(my_line)
    return review_list


raw_business_data = [
  {
    'business_name': 'Salt & Straw',
  },
  {
    'business_name': 'Voodoo Donuts',
  },
]
raw_user_data = [
  {'user_name': 'Abby'},
  {'user_name': 'Helen'},
  {'user_name': 'Bobby'},
]
raw_review_data = [
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 5, 'text': 'Lucious ice cream!'},
  {'user_name': 'Bobby', 'business_name': 'Salt & Straw', 'rating': 4, 'text': 'Super tasty, but such a long line!'},
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 2, 'text': 'Overrated, but I like sugar.'},
  {'user_name': 'Helen', 'business_name': 'Voodoo Donuts', 'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
  {'user_name': 'Bobby', 'business_name': 'Voodoo Donuts', 'rating': 5, 'text': 'Pink building is so cute!'},
  {'user_name': 'Abby', 'business_name': 'Voodoo Donuts', 'rating': 2, 'text': 'Diabetes inducing.'},
]

user_business_search = input("Search for a business?\n: ")
my_search_results = search_by_name(raw_review_data, user_business_search)
print(my_search_results)
user_name_search = input("Search for a reviewer?\n: ")
my_user_reviews = search_by_user(raw_review_data, user_name_search)
print(my_user_reviews)

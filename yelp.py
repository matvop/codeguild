"""4/5/2016 Matt, Matt, & Peter


"""

import random


class Review:
    def __init__(self, business_name, user_name, rating, review):
        self.rating = rating
        self.business_name = business_name
        self.user_name = user_name
        self.review = review

    def __repr__(self):
        my_str = "{}: {} rating: {}".format(self.business_name,
                                            self.review, self.rating)
        return my_str


class Business:
    def __init__(self, business_name):
        self.business_name = business_name

    def __repr__(self):
        return '{}'.format(self.business_name)


class User:
    def __init__(self, user_name):
        self.user_name = user_name


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
  {'user_name': 'Abby', 'business_name': 'Salt & Straw',
   'rating': 5, 'text': 'Lucious ice cream!'},
  {'user_name': 'Bobby', 'business_name': 'Salt & Straw',
   'rating': 4, 'text': 'Super tasty, but such a long line!'},
  {'user_name': 'Abby', 'business_name': 'Salt & Straw',
   'rating': 2, 'text': 'Overrated, but I like sugar.'},
  {'user_name': 'Helen', 'business_name': 'Voodoo Donuts',
   'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
  {'user_name': 'Bobby', 'business_name': 'Voodoo Donuts',
   'rating': 5, 'text': 'Pink building is so cute!'},
  {'user_name': 'Abby', 'business_name': 'Voodoo Donuts',
   'rating': 2, 'text': 'Diabetes inducing.'},
]


def search_business_name(review_class_list, user_input_string):
    review_list = [i for i in review_class_list
                   if user_input_string in i.business_name]
    average_counter = sum([i.rating for i in review_class_list
                           if user_input_string in i.business_name])
    average_rating = average_counter/len(review_list)
    print(average_rating)
    print(random.choice(review_list))
    return review_list


def search_user_name(review_class_list, user_input_string):
    list_of_user_reviews = [i for i in review_class_list
                            if user_input_string in i.user_name]
    print(list_of_user_reviews)


business_class_list = [Business(i['business_name']) for i in raw_business_data]
user_class_list = [User(i['user_name']) for i in raw_user_data]
review_class_list = [Review(i['business_name'], i['user_name'],
                     i['rating'], i['text']) for i in raw_review_data]
business_search_string = input('Enter a business name\n: ')
search_business_name(review_class_list, business_search_string)
user_search_string = input('Enter a user name\n: ')
search_user_name(review_class_list, user_search_string)

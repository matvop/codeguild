from . import models


def get_all_flutts():
    return models.Flutt.objects.all

def get_all_flutts_for_user(user_name):
    return models.Flutt.objects.all.filter(user_name=user_name).order_by('datetime')

def save_flutt(user_name, comment):
    new_flutt = models.Flutt(user_name=user_name, comment=comment)
    new_flutt.save()

def get_flutt_by_id(id):
    return models.Flutt.objects.get(id=id)

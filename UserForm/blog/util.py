import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UserForm.settings')

django.setup()

import random
from blog.models import Post
from django.contrib.auth.models import User

user_id = [1, 5, 12]


def extract():
    f_hand = open("../post2.txt", 'r')
    all_sent = f_hand.readlines()
    random.seed(0)
    for i in range(int(len(all_sent)/2)):
        user = user_id[random.randint(0, 2)]
        print("title: " + all_sent[2*i].rstrip())
        print("content: " + all_sent[2*i + 1].rstrip())
        post = Post(title=all_sent[2*i].rstrip(), content=all_sent[2*i + 1].rstrip(), author_id=user)
        post.save()


def show():
    users = User.objects.all()
    for user in users:
        print(user.id)


if __name__ == "__main__":
    extract()

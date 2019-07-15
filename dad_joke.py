import requests
from random import randint
# import pyfiglet
# import termcolor


colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

text = 'BEST JOKES IN HISTORY'
# color = input('What color do you like? ')
# if color not in colors:
#     color = 'magenta'
# ascii_art = termcolor.colored(text, color)
print(text)

url = "https://icanhazdadjoke.com/search"
topic = input('Let me tell you a joke. Give me a one word topic: ')
response = requests.get(url,
              headers = {"Accept" : "application/json"},
              params = {"term":topic}
              )
res = response.json()
total_joke = res["total_jokes"]
if total_joke == 0:
    print('Looks like your topic sucks! Try Again man!')
    quit()
elif total_joke == 1:
    result = (res["results"])
    print(f"I've got {total_joke} joke about {topic}.")
    joke = result[0]
    print(joke['joke'])
    quit()

result = (res["results"])
joke_no = randint(1,total_joke)
print(f"I've got {total_joke} jokes about {topic}. Let me give you one: ")
joke = result[joke_no-1]
print(joke['joke'])

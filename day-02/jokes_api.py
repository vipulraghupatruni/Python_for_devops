import requests

"""
    As a devops engineer, you will have to navigate through multiple external endpoints,
    and you should know how to switch them with python.
"""

pj_url = "https://official-joke-api.appspot.com/random_joke"
dad_joke_url = "https://icanhazdadjoke.com/"


def get_joke(url_type, mood):
    headers = {"Accept": "application/json"}  # set the headers to accept JSON response

    joke = requests.get(url=url_type, headers=headers)  # send a GET request to the URL
    data = joke.json()  # parse the JSON response once

    if mood == "dad":
        final_joke = data["joke"]  # parse the JSON response
    elif mood == "pj":
        # FIXED: Added 8 spaces of indentation to place this line inside the 'elif' block
        final_joke = data["setup"] + " " + data["punchline"]
    else:
        final_joke = "Unknown joke type configuration."

    return final_joke  # return the final joke


mood = input("which joke do you want to hear? (dad or pj): ").strip().lower()

# Catch user typos so the correct API parser runs without crashing
if mood == "dad":
    url_type = dad_joke_url
elif mood == "pj":
    url_type = pj_url
else:
    print("Invalid choice! Defaulting to a dad joke.")
    mood = "dad"  # Force mood to 'dad' to align with the dad_joke_url structure
    url_type = dad_joke_url

final_joke = get_joke(url_type, mood)  # call the function to get a joke
print(final_joke)  # print the final joke

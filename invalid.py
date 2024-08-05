
import random

def unknown():
    response = ["Could you please re-phrase that? ",
                "Did you mean something else? ",
                "What does that mean?"][
        random.randrange(3)]
    return response

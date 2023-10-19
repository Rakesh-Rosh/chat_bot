import random

R_EATING = "I don't like eating anyting because I'm a bot obviously"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_INFO  =  "Sync Intern is an organsization. which helps students by giving them internship Opportunity  "

def unknown():
    response = ["Could you please re-phrase that?",
                ".....",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response 
                
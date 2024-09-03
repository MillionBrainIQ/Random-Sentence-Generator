import random

article = ["The", "A",  "An"]
lowarticle = ["the", "a", "an"]
adjective = [["happy", "fruity", "high", "tipsy", "patriotic", 
              "necromanced", "diligent", "zesty", "joyful", 
              "sad", "depressed", "worried", "poor", "rich", 
              "broke", "vitriolic", "melancholy", "glum", 
              "hapless", "smart"], 
             ["ecstatic", "enthusiastic", "anxious", 
              "intelligent", "ugly"]]
noun = ["Kuvam", "Kevin", "student", "tiger shark",
        "sperm whale", "cobra", "sundew", "venus flytrap", 
        "puffball mushroom", "scientist", "researcher", 
        "nuclear enigneer", "nuclear reactor", "feather", 
        "hippopotamus", "platypus", "dog", "cat", "fish", 
        "Ashkay","atom", "astronomer", "astrophysicist", 
        "arrow", "arrowhead", "elephant", "equestrian", 
        "egg", "eggshell", "elevator", "idiot",
        "intellecutal", "iceberg", "insect", "inhaler", 
        "inchworm", "isotope", "ostrich", "opal", "ocean", 
        "octopus", "omelette", "umpire", "umbrella", 
        "ukelele", "unicycle", "underwear"]
verb = ["ran with", "fought", "looked at", "played a game with", "critisized", 
        "complimented", "educated", "advertised to", "advised", "hiked with", "insulted",
        "defaced", "defenestrated", "bamboozled", "went spelunking with"]   
punctuation = [".", "!", "?", "?!", "..."]

def random_shit():
    art = random.choice(article)
    lart = random.choice(lowarticle)
    adj1 = random.choice(random.choice(adjective))
    adj2 = random.choice(random.choice(adjective))
    n1 = random.choice(noun)
    n2 = random.choice(noun)
    v = random.choice(verb)
    s = " "
    p = random.choice(punctuation)

    if adj1 in adjective[1]:
        art = article[2]
    else:
        art = article[0]

    if adj2 in adjective[1]:
        lart = lowarticle[2]

    print(str(art) + str(s) + str(adj1) + str(s) + str(n1) + 
          str(s) + str(v) + str(s) + str(lart) + str(s) + 
          str(adj2) + str(s) + str(n2) + str(p))
    print()

num_sentences = int(input("How many random sentences would you like to generate? "))
print()
print()
for i in range (num_sentences):
    random_shit()
def get_game_data(choice):
    """Returns the game data (examples, name, description) based on user choice."""
    if choice == 1: # Encrypted
        return (
            [
                {"phrase": "Netflix and chill", "encrypted_phrase": "Net flicks and shill"}, # 'ch' to 'sh'
                {"phrase": "I am an idiot", "encrypted_phrase": "Aye am an iddiot"}, # 'I' to 'Aye', double 'd'
                {"phrase": "Pine of Guiness", "encrypted_phrase": "Pyne ov Ginness"}, # 'i' to 'y', 'u' to 'i'
                {"phrase": "Coding is fun", "encrypted_phrase": "Kodeing iz phun"}, # 'c' to 'k', 'f' to 'ph'
                {"phrase": "Lets go to the beach", "encrypted_phrase": "Lets go too the beech"}, # 'to' to 'too', 'ea' to 'ee'
                {"phrase": "I love pizza", "encrypted_phrase": "Eye luv peetza"}, # 'I' to 'Eye', 'zz' to 'tz'
                {"phrase": "Time for bed", "encrypted_phrase": "Tyme for bred"}, # 'i' to 'y', 'e' to 'e'
                {"phrase": "Walking in the park", "encrypted_phrase": "Wauking in the park"}, # 'a' to 'au'
                {"phrase": "Drinking coffee", "encrypted_phrase": "Drinkking kaughfee"}, # Double 'k', 'c' to 'k', 'ff' to 'ghf'
                {"phrase": "Playing video games", "encrypted_phrase": "Playeing viddeo gaymes"}, # 'ay' to 'ey', double 'd', 'a' to 'ay'
                {"phrase": "Reading a book", "encrypted_phrase": "Reeding ha buk"}, # 'oo' to 'u'
                {"phrase": "Learning new things", "encrypted_phrase": "Lurning nu thingz"}, # 'ea' to 'ur', 'ew' to 'u', 's' to 'z'
                {"phrase": "Having a good time", "encrypted_phrase": "Havving a good tyme"}, # Double 'v', 'i' to 'y'
                {"phrase": "Enjoying the sunshine", "encrypted_phrase": "Enjoying the sun shine"}, # No change (sometimes good to have some unchanged examples)
                {"phrase": "Watching a movie", "encrypted_phrase": "Wotchhing a muvee"}, # 'a' to 'o', double 'h', 'ie' to 'ee'
                {"phrase": "Listening to music", "encrypted_phrase": "Lisening too mewzik"}, # 't' to nothing, 'oo' to 'ew', 'ic' to 'ik'
                {"phrase": "The quick brown fox", "encrypted_phrase": "Teh kw ikb rown foks"}, # 'ck' to 'k', 'x' to 'ks'
                {"phrase": "Jump over the lazy dog", "encrypted_phrase": "Jumm p ovver the layzee dogg"}, # Double letters, 'y' to 'ee', double 'g'
                {"phrase": "Hello world", "encrypted_phrase": "Helo wurld"}, # 'll' to 'l', 'o' to 'u'
                {"phrase": "Goodbye moon", "encrypted_phrase": "Goodby mune"}, # 'ee' to 'e'
                {"phrase": "Right now", "encrypted_phrase": "Rite nau"}, # 'gh' to nothing, 'ow' to 'au'
                {"phrase": "Very good", "encrypted_phrase": "Verry gud"}, # Double 'r', 'oo' to 'u'
                {"phrase": "See you later", "encrypted_phrase": "Cee yoo layter"}, # 'ee' to 'ee'
                {"phrase": "Thank you", "encrypted_phrase": "Thank yew"}, # 'ou' to 'ew'
                {"phrase": "No problem", "encrypted_phrase": "No pro blem"}, # space added
                {"phrase": "Have a nice day", "encrypted_phrase": "Hav a nyce day"}, # 'e' to 'y'
                {"phrase": "How are you", "encrypted_phrase": "How r u"}, # abbreviation
                {"phrase": "What are you doing", "encrypted_phrase": "What r u duing"}, # abbreviation
                {"phrase": "I dont know", "encrypted_phrase": "Eye dont no"}, # 'I' to 'Eye', 'k' to nothing
                {"phrase": "See you soon", "encrypted_phrase": "C u sune"} # abbreviation
            ],
            "Encrypted",
            "A word game where one side of the card has a phrase and the other side has an encrypted version.",
        )
    elif choice == 2: # Reverse Trivia
        return (
            [
                {"question": "What is the capital of France?", "answer": "Paris"},
                {"question": "What color is a banana when it's ripe?", "answer": "Yellow"},
                {"question": "How many sides does a triangle have?", "answer": "Three"},
                {"question": "What is two plus two?", "answer": "Four"},
                {"question": "In what year did World War II end?", "answer": "1945"},
                {"question": "What is the chemical symbol for water?", "answer": "H2O"},
                {"question": "How many continents are there?", "answer": "Seven"},
                {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
                {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
                {"question": "How many teeth does an adult human typically have?", "answer": "32"},
                {"question": "What is the speed of light?", "answer": "Approximately 299,792,458 meters per second"},
                {"question": "What is the smallest prime number?", "answer": "2"},
                {"question": "What is the name of Earth's only natural satellite?", "answer": "The Moon"},
                {"question": "How many bones are in the adult human body?", "answer": "206"},
                {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide"},
                {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
                {"question": "Who wrote 'Hamlet'?", "answer": "William Shakespeare"},
                {"question": "What is the chemical symbol for gold?", "answer": "Au"},
                {"question": "What is the currency of Japan?", "answer": "Japanese Yen"},
                {"question": "How many ventricles are in the human heart?", "answer": "Four"},
                {"question": "What is the name of the longest river in the world?", "answer": "The Nile"},
                {"question": "What is the formula for area of a circle?", "answer": "πr²"},
                {"question": "What is the name of the force that keeps us on the ground?", "answer": "Gravity"},
                {"question": "How many days are in a leap year?", "answer": "366"},
                {"question": "What is the name of the Earth's atmosphere's protective layer?", "answer": "Ozone Layer"},
                {"question": "What is the name of the closest star to Earth?", "answer": "The Sun"},
                {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
                {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
                {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
                {"question": "What is the chemical symbol for oxygen?", "answer": "O"},
            ],
            "Reverse Trivia",
            "A word game where a player is presented with a question (card) and is only given points for wrong answers.",
        )
    elif choice == 3: # Logic
        return (
            [
                {"question": "All squares are rectangles.", "answer": "Yes"},
                {"question": "Fish can fly.", "answer": "No"},
                {"question": "The moon is made of cheese that sings opera while riding a bicycle.", "answer": "Nonsense"},
                {"question": "If it rains, the ground gets wet.", "answer": "Yes"},
                {"question": "Cats are vegetables.", "answer": "No"},
                {"question": "Numbers can smell colors.", "answer": "Nonsense"},
                {"question": "The sun rises in the east.", "answer": "Yes"},
                {"question": "Birds are mammals.", "answer": "No"},
                {"question": "Trees talk to each other using invisible rainbows.", "answer": "Nonsense"},
                {"question": "Water is wet.", "answer": "Yes"},
                {"question": "Dogs lay eggs.", "answer": "No"},
                {"question": "Books can drive cars to the library.", "answer": "Nonsense"},
                {"question": "Humans need oxygen to breathe.", "answer": "Yes"},
                {"question": "Spiders have eight legs.", "answer": "Yes"},
                {"question": "Clouds are made of cotton candy that rains lemonade.", "answer": "Nonsense"},
                {"question": "Fire is cold.", "answer": "No"},
                {"question": "The Earth is flat.", "answer": "No"},
                {"question": "Pencils can swim in the ocean.", "answer": "Nonsense"},
                {"question": "Gravity pulls things downwards.", "answer": "Yes"},
                {"question": "Elephants are small insects.", "answer": "No"}
            ],
            "Logic",
            "A word game where you find rhyming words.",
        )
    
    return None  # Invalid choice
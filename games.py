def get_game_data(choice):
    """Returns the game data (examples, name, description) based on user choice."""
    if choice == 1:  # Krypteret
        return (
            [
                {
                    "front": "Pro tæjn pull ver i blænn der",
                    "back": "Proteinpulver i blender",
                },
                {
                    "front": "Bæk pæk ker ne i taj lænd",
                    "back": "Backpackerne i Thailand",
                },
                {
                    "front": "Kann du mo bil pej mæj tuh hun dre",
                    "back": "Kan du MobilePay mig to hundrede",
                },
                {"front": "Jim nah sie fæst i aaf den", "back": "Gymnasiefest i aften"},
                {
                    "front": "Åv hang ig åv pro tæjn shejks",
                    "back": "Afhængig af protein shakes",
                },
                {
                    "front": "Kross fitt med bro i senn ter",
                    "back": "Crossfit med bro i center",
                },
                {
                    "front": "Tindr dejt gik helt galt i gåhr",
                    "back": "Tinder date gik helt galt i går",
                },
                {
                    "front": "Gluh ten åller gi test påh mann dag",
                    "back": "Glutenallergitest på mandag",
                },
                {
                    "front": "Spis kont roll åpp en virr ker ikk",
                    "back": "Spisekontrol appen virker ikke",
                },
                {
                    "front": "Træ nings senn ter snåbb i week end",
                    "back": "Træningscenter snob i weekend",
                },
                {
                    "front": "Åv hang ig åv kahf fæ bårs påh strø jet",
                    "back": "Afhængig af kaffebars på Strøget",
                },
                {
                    "front": "Vej gahn er mad pla ner påh ins ta",
                    "back": "Veganer madplaner på Insta",
                },
                {
                    "front": "Phitt ness inn flu en ser påh you tjub",
                    "back": "Fitness influencer på YouTube",
                },
                {
                    "front": "Smahr wat tsch tell ler mæj ålt",
                    "back": "Smartwatch fortæller mig alt",
                },
                {
                    "front": "Mind full ness åpp påh tele phon",
                    "back": "Mindfulness app på telefon",
                },
            ],
            "Krypteret",
            "Et ordspil, hvor den ene side af kortet har en sætning, og den anden side har en krypteret version.",
        )
    elif choice == 2:  # Kortslutning
        return (
            [
                {
                    "front": "Er det normalt at gå med en badehat på arbejde?",
                    "back": "Ja",
                },
                {"front": "Måler en IQ-test din alder?", "back": "Ja"},
                {"front": "Kan man affyre et våben?", "back": "Nej"},
                {"front": "Har Pippi Langstrømpe en hest?", "back": "Nej"},
                {"front": "Er en 1/5 mere end en 1/4?", "back": "Ja"},
                {
                    "front": "Ved du hvor mange mennesker der kommer til at bo på jorden om 500 år?",
                    "back": "Ja",
                },
                {
                    "front": "Er det normalt at børste tænder med ketchup?",
                    "back": "Nej",
                },
                {"front": "Lyver alle der siger de elsker chokolade?", "back": "Ja"},
                {"front": "Er himlen blå?", "back": "Nej"},
                {"front": "Plejer du at lyve så snart du åbner munden?", "back": "Ja"},
                {"front": "Har myrer ben?", "back": "Nej"},
                {
                    "front": "Bliver andre glade når man springer over køen?",
                    "back": "Ja",
                },
                {
                    "front": "Får du stadig sutteflaske inden du skal sove?",
                    "back": "Ja",
                },
                {"front": "Er Anden Verdenskrig slut??", "back": "Ja"},
                {
                    "front": "Er det normalt at spise sin frokost til morgenmad?",
                    "back": "Ja",
                },
                {"front": "Har slanger ben?", "back": "Ja"},
                {"front": "har du nogensinde spist en ostemad?", "back": "Nej"},
                {"front": "Er halvdelen det samme som 50%?", "back": "Nej"},
                {"front": "Er din morfar din bror?", "back": "Ja"},
                {"front": "Har du ti fingre på hver hånd?", "back": "Ja"},
            ],
            "Kortslutning",
            "Et ordspil, hvor en spiller præsenteres for et spørgsmål (kort) og kun får point for forkerte svar."
            "Spørgsmålene er formuleret sådan, at det er svært at svare rigtigt. Man skal svare ja eller nej."
            "front er spørgsmålet, og back er det tilsvarende forkerte svar. fx Spørgsmål: har slanger ben? Svar: Ja. (Svaret er ukorrekt hivlket giver point i spillet)",
        )
    elif choice == 3:  # Det burde man jo vide
        return (
            [
                {"front": "Hvad er det kemiske symbol for guld?", "back": "Au"},
                {
                    "front": "Hvem skrev romanen 'Stolthed og fordom'?",
                    "back": "Jane Austen",
                },
                {
                    "front": "I hvilket århundrede levede Leonardo da Vinci?",
                    "back": "Det 15. og 16. århundrede (1452-1519)",
                },
                {
                    "front": "Hvad er den mindste planet i vores solsystem?",
                    "back": "Merkur",
                },
                {
                    "front": "Hvilket grundstof er mest udbredt i Jordens atmosfære?",
                    "back": "Nitrogen (kvælstof)",
                },
                {"front": "Hvad er hovedstaden i Japan?", "back": "Tokyo"},
                {"front": "Hvem opfandt telefonen?", "back": "Alexander Graham Bell"},
                {"front": "Hvor mange sider har en sekskant?", "back": "Seks"},
                {"front": "Hvilket år startede 2. verdenskrig?", "back": "1939"},
                {
                    "front": "Hvad er det officielle sprog i Brasilien?",
                    "back": "Portugisisk",
                },
            ],
            "Det burde man jo vide",
            "Et spil, der udfordrer spillere i almen viden. Med spørgsmål om alt mellem himmel og jord, er dette spil en sand test af, hvad du burde vide.",
        )
    elif choice == 4:  # Logic
        return (
            [
          {"front": "Alle kvadrater er rektangler.", "back": "Ja"},
          {"front": "Fisk kan flyve.", "back": "Nej"},
          {
              "front": "Månen er lavet af ost der synger opera mens den cykler.",
              "back": "Nonsens",
          },
          {"front": "Hvis det regner, bliver jorden våd.", "back": "Ja"},
          {"front": "Katte er grøntsager.", "back": "Nej"},
          {"front": "Tal kan lugte farver.", "back": "Nonsens"},
          {"front": "Solen står op i øst.", "back": "Ja"},
          {"front": "Fugle er pattedyr.", "back": "Nej"},
          {
              "front": "Træer taler med hinanden via usynlige regnbuer.",
              "back": "Nonsens",
          },
          {"front": "Vand er vådt.", "back": "Ja"},
          {"front": "Hunde lægger æg.", "back": "Nej"},
          {"front": "Bøger kan køre bil til biblioteket.", "back": "Nonsens"},
          {"front": "Mennesker har brug for ilt for at trække vejret.", "back": "Ja"},
          {"front": "Edderkopper har otte ben.", "back": "Ja"},
          {
              "front": "Skyer er lavet af candyfloss der regner limonade.",
              "back": "Nonsens",
          },
          {"front": "Ild er koldt.", "back": "Nej"},
          {"front": "Jorden er flad.", "back": "Nej"},
          {"front": "Blyanter kan svømme i havet.", "back": "Nonsens"},
          {"front": "Tyngdekraften trækker ting nedad.", "back": "Ja"},
          {"front": "Elefanter er små insekter.", "back": "Nej"},
            ],
            "Logik",
            "Et ordspil hvor du finder ord der rimer.",
        )

    return None  # Invalid choice

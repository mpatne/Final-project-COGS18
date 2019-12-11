#The chatbot's response library

acceptable_characters = "abcdefghijklmnopqrstuvwxyz -"

bot_name = 'grookey'
greetings = ['hello', 'hi', "whats", "up", bot_name]
goodbyes = ['goodbye', 'bye', "bye-bye", bot_name]

ape_subjects = ['orangutan', 'bonobo', 'siamang', 'palm oil']

orangutan_info = "Orangutan infants are the cutest! They have wrinkled faces when they are born and very thin hands and feet. They are completely dependent on their mothers (just like human babies). They weigh only 1 to 2 pounds after birth. They usually start walking independently at 6 months of age, but stay with their mother constantly for at least 1 year. They are breastfed by their loving mothers for at least 4 years. Aisha, the baby orangutan from the San Diego zoo, has been seen suckling her mother even though she is turning 6 years old! This is in line with the fact that orangutan babies have very long childhoods, ranging from 10-14 years. They’re no different from human teenagers! "
bonobo_info = "Bonobo infants are incredibly cute! They look the most human out of all the primate babies, with a significant eye to face ratio. They are completely dependent on their mothers and are weaned after 6 years of age. They stay constantly with their mother until around 6-7 years of age; at this point, young female juveniles will leave her natal pack and journey to find another group of bonobos. The male juveniles stay in their natal pack, so the females are the real explorers! At the San Diego zoo, baby bonobo Belle is turning 6 years old, and is treated like a princess by most of her pack! Her mother, sisters, and cousins play, feed, and coddle her constantly. "
siamang_info = "Siamang infants are so fantastically cute! Siamangs are actually a type of lesser ape, diverging from most of the modern great ape species by around 4.5 million years beforehand. They are extremely tiny when they are born and spend much of their first-year clinging to their mothers. Their mothers are very protective of their infants, refusing to let the father touch them; however, after 1 year of age, siamang babies actually seek out nurture and care from their father! They have long arms that are meant for brachiation and are strong enough to hold their weight after 9 months. Sela, a prematurely born siamang infant, recently turned 1 year old at the San Diego zoo! She hops around excitedly, her long arms flailing around her tiny body as onlookers take pictures of her cute face like their life depends on it. "
palm_oil_info = "Palm oil is a type of oil gathered from the oil palm tree in tropical areas of the world, most commonly in rainforested areas like Malaysia and Borneo. Due to shelf stable chemical properties, palm oil is a cash crop that is surprisingly in many products, like in your shampoo, chips, LIPSTICK, toothpaste, grocery pastries, instant noodles, and even Oreos! Freaking Oreos! Unfortunately, oil palm trees can only be grown specific environmental conditions which happen to be native habitat of orangutans and siamangs. Many orangutans and siamangs are driven out of deforested areas and die shortly afterwards. Please reduce your palm oil consumption by either boycotting these products or looking for the RSPO label, which certifies a product made with sustainably grown palm oil. We don’t want to live in a world that has none of these beautiful animals! "

conversation_topics = {
    "orangutan": orangutan_info,
    "bonobo" : bonobo_info,
    "siamang": siamang_info,
    "palm oil": palm_oil_info,
    "why are you a baby grookey" : "I was conceived for the COGS18 final project, so there is not much I know! But rest assured, I am a very cute baby. ",
    "how do you know so much grookey" : "The primate who coded me works as an RA in a cross-species developmental research lab at UCSD! She has an interest in primate cognition and spends a lot of time studying infant ape development at the San Diego zoo. ",
    "what is so bad about palm oil grookey": palm_oil_info,
    "teach me more grookey": "I can tell you what’s bad about palm oil! ",
    "i dont want babies grookey" : "I will leave now since you don’t want me ): ",
}

common_replies = {
    "onrun": "Hello, my name is Grookey and I am your guide to baby primates! I will pique your interest in them by providing some general information and by also talking about some babies at our local San Diego zoo!",
    "start" : "Hello, human primate! What would you like to know?",
    "end" : "Goodbye human primate! Go in peace and do not do anything destructive to your fellow evolutionary cousins. Best of luck in the real world!",
    "no answer": "Sorry! I am also a baby primate, so I know very little about the world. Ask me about orangutan babies, bonobo babies, and siamang babies! "
}

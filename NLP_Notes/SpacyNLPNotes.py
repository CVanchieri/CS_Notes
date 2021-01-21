### SPACY natural language processing notes ### 
''' NLP makes it possible for computers to read text, hear speech, interpret it, 
    measure sentiment and determine which parts are important'''

### ###

''' loading spacy '''
### spacy import ###
import spacy
### spacy language file installs ###
!python -m spacy download en_core_web_sm # small 
!python -m spacy download en_core_web_lg # large 
### spacy language file loads ###
nlp = spacy.load("en_core_web_sm") # small 
nlp = spacy.load("en_core_web_lg") # large  


''' tokenize & parse '''
### tokenize/parse a document ###
my_text = """Robotics is an interdisciplinary research area at the interface of computer science and engineering. Robotics involvesdesign, 
construction, operation, and use of robots. The goal of robotics is to design intelligent machines that can help and assist humans in their 
day-to-day lives and keep everyone safe. Robotics draws on the achievement of information engineering, computer engineering, mechanical 
engineering, electronic engineering and others.Robotics develops machines that can substitute for humans and replicate human actions. 
Robots can be used in many situations and for lots of purposes, but today many are used in dangerous environments(including inspection of 
radioactive materials, bomb detection and deactivation), manufacturing processes, or where humans cannot survive (e.g. in space, underwater, 
in high heat, and clean up and containment of hazardousmaterials and radiation). Robots can take on any form but some are made to 
resemble humans in appearance. This is said to help in the acceptance of a robot in certain replicative behaviors usually performed by 
people. Such robots attempt to replicate walking, lifting, speech, cognition, or any other human activity. Many of todays robots are 
inspired by nature, contributing to the field of bio-inspired robotics.The concept of creating machines that can operate autonomously dates 
back to classical times, but research into the functionality and potential uses of robots did not grow substantially until the 20th century. 
Throughout history, it has been frequently assumed by various scholars, inventors, engineers, and technicians that robots will one day be able 
to mimic human behavior and manage tasks in a human-like fashion. Today, robotics is a rapidly growing field, as technological advances continue; 
researching, designing, and building new robots serve various practical purposes, whether domestically, commercially, or militarily. Many robots are 
built to do jobs that are hazardous to people, such as defusing bombs, finding survivors in unstable ruins, and exploring mines and shipwrecks. Robotics 
is also used in STEM (science, technology, engineering, and mathematics) as a teaching aid. The advent of nanorobots, microscopic robots that can be 
injected into the human body, could revolutionize medicine and human health.Robotics is a branch of engineering that involves the conception, design, 
manufacture, and operation of robots. This field overlaps with computer engineering, computer science (especially artificial intelligence), 
electronics, mechatronics, nanotechnology and bioengineering.The word robotics was derived from the word robot, which was introduced to the public 
by Czech writer Karel Capek in his play R.U.R. (Rossums Universal Robots), whichwas published in 1920. The word robot comes from the Slavic word 
robota, which means slave/servant. The play begins in a factory that makes artificial people called robots, creatures who can be mistaken for 
humans – very similar to the modern ideas of androids. Karel Capek himself did not coin the word. He wrote a short letter in reference to an etymology in the 
Oxford English Dictionary in which he named his brother Josef Capek as its actual originator.According to the Oxford English Dictionary, 
the word robotics was first used in print by Isaac Asimov, in his science fiction short story "Liar!", published in May 1941 in Astounding 
Science Fiction. Asimov was unaware that he was coining the term  since the science and technology of electrical devices is electronics, 
he assumed robotics already referred to the science and technology of robots. In some of Asimovs other works, he states that the first use 
of the word robotics was in his short story Runaround (Astounding Science Fiction, March 1942) where he introduced his concept of The Three Laws 
of Robotics. However, the original publication of "Liar!" predates that of "Runaround" by ten months, so the former is generally cited as the words origin.
There are many types of robots; they are used in many different environments and for many different uses. Although being very diverse in application and form, 
they all share three basic similarities when it comes to their construction:Robots all have some kind of mechanical construction, a frame, form or shape 
designed to achieve a particular task. For example, a robot designed to travel across heavy dirt or mud, might use caterpillar tracks. The mechanical 
aspect is mostly the creators solution to completing the assigned task and dealing with the physics of the environment around it. Form follows 
function.Robots have electrical components which power and control the machinery. For example, the robot with caterpillar tracks would need 
some kind of power to move the tracker treads. That power comes in the form of electricity, which will have to travel through a wire and 
originate from a battery, a basic electrical circuit. Even petrol powered machines that get their power mainly from petrol still require an 
electric current to start the combustion process which is why most petrol powered machines like cars, have batteries. The electrical aspect 
of robots is used for movement (through motors), sensing (where electrical signals are used to measure things like heat, sound, position, 
and energy status) and operation (robots need some level of electrical energy supplied to their motors and sensors in order to activate and 
perform basic operations) All robots contain some level of computer programming code. A program is how a robot decides when or how to do 
something. In the caterpillar track example, a robot that needs to move across a muddy road may have the correct mechanical construction 
and receive the correct amount of power from its battery, but would not go anywhere without a program telling it to move. Programs are the 
core essence of a robot, it could have excellent mechanical and electrical construction, but if its program is poorly constructed its 
performance will be very poor (or it may not perform at all). There are three different types of robotic programs: remote control, 
artificial intelligence and hybrid. A robot with remote control programing has a preexisting set of commands that it will only perform if 
and when it receives a signal from a control source, typically a human being with a remote control. It is perhaps more appropriate to view 
devices controlled primarily by human commands as falling in the discipline of automation rather than robotics. Robots that use artificial 
intelligence interact with their environment on their own without a control source, and can determine reactions to objects and problems 
they encounter using their preexisting programming. Hybrid is a form of programming that incorporates both AI and RC functions.As more and 
more robots are designed for specific tasks this method of classification becomes more relevant. For example, many robots are designed for 
assembly work, which may not be readily adaptable for other applications. They are termed as "assembly robots". For seam welding, some 
suppliers provide complete welding systems with the robot i.e. the welding equipment along with other material handling facilities like 
turntables, etc. as an integrated unit. Such an integrated robotic system is called a "welding robot" even though its discrete manipulator 
unit could be adapted to a variety of tasks. Some robots are specifically designed for heavy load manipulation, and are labeled as 
"heavy-duty robots".one or two wheels. These can have certain advantages such as greater efficiency and reduced parts, as well as allowing 
a robot to navigate in confined places that a four-wheeled robot would not be able to.Two-wheeled balancing robots Balancing robots 
generally use a gyroscope to detect how much a robot is falling and then drive the wheels proportionally in the same direction, to 
counterbalance the fall at hundreds of times per second, based on the dynamics of an inverted pendulum.[71] Many different balancing robots 
have been designed.[72] While the Segway is not commonly thought of as a robot, it can be thought of as a component of a robot, when used 
as such Segway refer to them as RMP (Robotic Mobility Platform). An example of this use has been as NASA Robonaut that has been mounted on 
a Segway.One-wheeled balancing robots Main article: Self-balancing unicycle A one-wheeled balancing robot is an extension of a two-wheeled 
balancing robot so that it can move in any 2D direction using a round ball as its only wheel. Several one-wheeled balancing robots have been 
designed recently, such as Carnegie Mellon Universitys "Ballbot" that is the approximate height and width of a person, and Tohoku Gakuin 
University BallIP Because of the long, thin shape and ability to maneuver in tight spaces, they have the potential to function better than 
other robots in environments with people.
"""
### run the text doc through the nlp ###
my_doc = nlp(my_text)
# print each token text 
for token in my_doc:
  print(token.text)
### create a list of tokens 
tokens = []
for token in my_doc:
  tokens.append(token)
  print(len(tokens))
print(tokens)


''' cleaning tokens '''
### look for stopwords and punctuation ### 
for token in my_doc:
  print(token.text,'--',token.is_stop,'---',token.is_punct)
### remove any stop words and punctuation found ###
my_doc_cleaned = [token for token in my_doc if not token.is_stop and not token.is_punct]
### list of tokens after cleaning ###
tokens_cleaned = []
for token in my_doc_cleaned:
  tokens_cleaned.append(token)
print(len(tokens_cleaned))
print(tokens_cleaned)
### look at part of speech tagging for addtional cleaning ###


''' token/word hashes '''
### look up a word hash for a string/word ###
word_hash = nlp.vocab.strings["robotics"]
print(word_hash)
### look up a string/word from a word hash ###
word_string = nlp.vocab.strings[word_hash]
print(word_string)


''' lexical attributes '''
# token.lemma_, find the base/root word of the token 
# token.is_punct, find tokens that are punctuations
# token.is_stop, find tokens that are stop words 
# token.is_space, find tokens that are spaces ' '
# token.like_num, find tokens that are numbers 
# token.is_alpha : Returns True if the token is an alphabet
# token.is_ascii : Returns True if the token belongs to ascii characters
# token.is_digit, find tokens that are numbers from 0-9
# token.is_upper, find tokens that are uppercase 
# token.is_lower, find tokens that are lowercase 
# token.is_bracket, find tokens that are brackets 
# token.is_quote, find tokens that are quotation marks 
# token.i, access index of a token
# token.i + 1, access index of next token

### locate numbers attribute example ###
### load in the text to use ### 
my_text = '2020 is far worse than 2009'
# create the doc from the text 
my_doc = nlp(my_text)
### find/locate all tokens that are numbers ###
numbers_tokens = []
for token in my_doc:
  if token.like_num:
    numbers_tokens.append(token)
print(numbers_tokens)

### locate numbers attribute followed by % sign example ###
### load in the text to use ### 
my_text=' Production in chennai is 87 %. In Kolkata, produce it as low as 43 %. In Bangalore, production ia as good as 98 %.In mysore, production is average around 78 %'
# create the doc from the text 
my_doc = nlp(my_text)
### find all tokens that are numbers followed by a % ###
numbers_perc_tokens = []
for token in my_doc:
  if token.like_num:
    idx_next_token=token.i+ 1
    next_token = my_doc[idx_next_token]
    if next_token.text == '%':
      numbers_perc_tokens.append(token)
print(numbers_perc_tokens)

### locate email address attribute example ###
### load in the text to use ### 
my_text=""" name : Koushiki age: 45 email : koushiki@gmail.com
            name : Gayathri age: 34 email: gayathri1999@gmail.com
            name : Ardra age: 60 email : ardra@gmail.com
            name : pratham parmar age: 15 email : parmar15@yahoo.com
            name : Shashank age: 54 email: shank@rediffmail.com
            name : Utkarsh age: 46 email :utkarsh@gmail.com"""
# create the doc from the text 
my_doc = nlp(my_text)
### find all tokens that are emails ###
email_tokens = []
for token in my_doc:
  if token.like_email:
    email_tokens.append(token)
print(email_tokens)


''' part of speech tagging '''
### check the part of speech of a token/word ###
### load in the text to use ### 
my_text = 'John plays basketball, if time permits. He played in high school too.'
# create the doc from the text 
my_doc = nlp(my_text)
### identify the part of speech of the tokens ### 
for token in my_doc:
  print(token.text,'---> ',token.pos_)
### show the index and part of speech of the tokens ### 
all_tags = {token.pos: token.pos_ for token in my_doc}
print(all_tags)

### remove junk values with part of speech ###
### load in the text to use ### 
my_text = """I liked the movies etc The movie had good direction  The movie was amazing i.e.
            The movie was average direction was not bad The cinematography was nice. i.e.
            The movie was a bit lengthy  otherwise fantastic  etc etc"""
# create the doc from the text 
my_doc = nlp(my_text)
### show the junk values with part of speech tagging ###
print('-- junk values --')
for token in my_doc:
  if token.pos_== 'X':
    print(token.text)
### remove tokens with the junk values ###
clean_doc = [token for token in my_doc if not token.pos_ == 'X']
print(clean_doc)

### visualize parts of speach of a sentance/document ###
### import ###
from spacy import displacy
displacy.render(my_doc, style = 'dep', jupyter = True)


''' name entity recognition 'ner' '''
 ### category types ###
# PERSON, names of people
# GPE, places like counties, cities, states
# ORG, organizations or companies
# WORK_OF_ART, titles of books, fimls,songs and other arts
# PRODUCT, products such as vehicles, food items ,furniture and so on
# EVENT, historical events like wars, disasters ,etc
# LANGUAGE, all the recognized languages across the globe

### show all the entities in the text doc ###
### load in the text to use ### 
my_text = 'Tony Stark owns the company StarkEnterprises . Emily Clark works at Microsoft and lives in Manchester. She loves to read the Bible and learn French'
# create the doc from the text 
my_doc = nlp(my_text)
### show all the name entities ###
for ent in my_doc.ents:
  print(ent.text,'--- ',ent.label_)
### find only the organization/company entities ###
companies = []
for ent in my_doc.ents:
  if ent.label_ == 'ORG':
    companies.append(ent)
for val in companies:
  print(val.text,'---> ',val.label_)

### mask entities for privacy ### 
# function to 'mask' specific entity types ###
def mask_details(token):
  if token.ent_type_ =='PERSON' or token.ent_type_=='ORG' or token.ent_type_=='GPE':
    return ' ->MASKED<- '
  return token.string
### function to pass each token and mask_details of necessary ###
def update_doc(my_doc):
  for ent in my_doc.ents:
    ent.merge()
  tokens = map(mask_details, my_doc)
  return ''.join(tokens)
# run my_doc through the function ###
update_doc(my_doc)


''' rule based matching '''
# token matcher 
# phrase matcher 
# entity ruler 

### token matcher ###
### import ###
from spacy.matcher import Matcher 
### filtering version text and number 'version : #'  example ###
### load in the text to use ### 
my_text = '''The version : 6 of the app was released about a year back and was not very sucessful. As a comeback, six months ago, version : 7 was released and it took the stage. 
            After that , the app has has the limelight till now. On interviewing some sources, we get to know that they have outlined visiond till version : 12 ,the Ultimate.'''
# create the doc from the text 
my_doc = nlp(my_text)
### initialuze the Matcher ###
matcher = Matcher(nlp.vocab) # using .vocab
### create the pattern to wish to use ###
### looking for version + # numbers ###
my_pattern = [{"LOWER": "version"}, {"IS_PUNCT": True}, {"LIKE_NUM": True}] # [{lowercase text 'version'} {is punctuation} {is a number}]
### add the pattern to the matcher ###
matcher.add('VersionFinder', None, my_pattern) # match_id = name of 'pattern' , match_on = None, patterns = my_pattern
### run the matcher on the text doc ### 
desired_matches = matcher(my_doc)
print('(match_id = hash, start = starting token, end = ending token)')
desired_matches
### show the text contents of the matchers hashes ###
### loop through each match, create string of info, pull text from doc ###
for match_id, start, end in desired_matches:
    string_id = nlp.vocab.strings[match_id] 
    span = my_doc[start:end] 
    print(span.text)

### filter visiting/visited places example ###
### load in the text to use ### 
my_text = """I visited Manali last time. Around same budget trips ? "
              I was visiting Ladakh this summer "
              I have planned visiting NewYork and other abroad places for next year"
              Have you ever visited Kodaikanal? """
# create the doc from the text 
my_doc = nlp(my_text)
### initialuze the Matcher ###
matcher = Matcher(nlp.vocab)
### create the pattern you wish to use ###
### looking for visit leamm and proper noun ###
my_pattern = [{"LEMMA": "visit"}, {"POS": 'PROPN'}] # [{lemma base 'visit'} {part of speeach = PROPN}]
### initialuze the Matcher ###
matcher = Matcher(nlp.vocab)
### create the pattern you wish to use ###
### looking for visit leamm and proper noun ###
my_pattern = [{"LEMMA": "visit"}, {"POS": 'PROPN'}] # [{lemma base 'visit'} {part of speeach = PROPN}]
### add the matcher ###
matcher.add('visiting', None, my_pattern) # match_id = name of 'pattern' , match_on = None, patterns = my_pattern
### run the matcher on the doc
desired_matches = matcher(my_doc)
print('(match_id = hash, start = starting token, end = ending token)')
desired_matches
### loop through each match, create string of info, pull text from doc ###
for match_id, start, end in desired_matches:
    string_id = nlp.vocab.strings[match_id] 
    span = my_doc[start:end] 
    print(span.text)

### filter engineering courses   example ###
### load in the text to use ### 
my_text = """If you study aeronautical engineering, you could specialize in aerodynamics, aeroelasticity, 
            composites analysis, avionics, propulsion and structures and materials. If you choose to study chemical engineering, you may like to
            specialize in chemical reaction engineering, plant design, process engineering, process design or transport phenomena. Civil engineering is the professional practice of designing and developing infrastructure projects. This can be on a huge scale, such as the development of
            nationwide transport systems or water supply networks, or on a smaller scale, such as the development of single roads or buildings.
            specializations of civil engineering include structural engineering, architectural engineering, transportation engineering, geotechnical engineering,
            environmental engineering and hydraulic engineering. Computer engineering concerns the design and prototyping of computing hardware and software. 
            This subject merges electrical engineering with computer science, oldest and broadest types of engineering, mechanical engineering is concerned with the design,
            manufacturing and maintenance of mechanical systems. You’ll study statics and dynamics, thermodynamics, fluid dynamics, stress analysis, mechanical design and
            technical drawing"""
# create the doc from the text 
my_doc = nlp(my_text)
### initialuze the Matcher ###
matcher = Matcher(nlp.vocab)
### create the pattern you wish to use ###
### looking for noun or adjective + engineering ###
my_pattern = [{"POS": {"IN": ["NOUN", "ADJ"]}}, {"LOWER": "engineering"}] # [{part of speeach = NOUN or ADJ}{ lowercase text engineering}]
### add the matcher ###
matcher.add('courses', None, my_pattern) # match_id = name of 'pattern' , match_on = None, patterns = my_pattern
### run the matcher on the doc
desired_matches = matcher(my_doc)
print('(match_id = hash, start = starting token, end = ending token)')
desired_matches
### loop through each match, create string of info, pull text from doc ###
for match_id, start, end in desired_matches:
    string_id = nlp.vocab.strings[match_id] 
    span = my_doc[start:end] 
    print(span.text)

### phrase matcher ###
### import ###
from spacy.matcher import PhraseMatcher
### filter engineering courses ###
### load in the text to use ###  
my_text = """Superman (first appearance: 1938)  Created by Jerry Siegal and Joe Shuster for Action Comics #1 (DC Comics).Mickey Mouse (1928)  Created by Walt Disney and Ub Iworks for Steamboat Willie.Bugs Bunny (1940)  Created by Warner Bros and originally voiced by Mel Blanc.Batman (1939) Created by Bill Finger and Bob Kane for Detective Comics #27 (DC Comics).
Dorothy Gale (1900)  Created by L. Frank Baum for novel The Wonderful Wizard of Oz. Later portrayed by Judy Garland in the 1939 film adaptation.Darth Vader (1977) Created by George Lucas for Star Wars IV: A New Hope.The Tramp (1914)  Created and portrayed by Charlie Chaplin for Kid Auto Races at Venice.Peter Pan (1902)  Created by J.M. Barrie for novel The Little White Bird.
Indiana Jones (1981)  Created by George Lucas for Raiders of the Lost Ark. Portrayed by Harrison Ford.Rocky Balboa (1976)  Created and portrayed by Sylvester Stallone for Rocky.Vito Corleone (1969) Created by Mario Puzo for novel The Godfather. Later portrayed by Marlon Brando and Robert DeNiro in Coppola’s film adaptation.Han Solo (1977) Created by George Lucas for Star Wars IV: A New Hope. 
Portrayed most famously by Harrison Ford.Homer Simpson (1987)  Created by Matt Groening for The Tracey Ullman Show, later The Simpsons as voiced by Dan Castellaneta.Archie Bunker (1971) Created by Norman Lear for All in the Family. Portrayed by Carroll O’Connor.Norman Bates (1959) Created by Robert Bloch for novel Psycho.  Later portrayed by Anthony Perkins in Hitchcock’s film adaptation.King Kong (1933) 
Created by Edgar Wallace and Merian C Cooper for the film King Kong.Lucy Ricardo (1951) Portrayed by Lucille Ball for I Love Lucy.Spiderman (1962)  Created by Stan Lee and Steve Ditko for Amazing Fantasy #15 (Marvel Comics).Barbie (1959)  Created by Ruth Handler for the toy company Mattel Spock (1964)  Created by Gene Roddenberry for Star Trek. Portrayed most famously by Leonard Nimoy.
Godzilla (1954) Created by Tomoyuki Tanaka, Ishiro Honda, and Eiji Tsubaraya for the film Godzilla.The Joker (1940)  Created by Jerry Robinson, Bill Finger, and Bob Kane for Batman #1 (DC Comics)Winnie-the-Pooh (1924)  Created by A.A. Milne for verse book When We Were Young.Popeye (1929)  Created by E.C. Segar for comic strip Thimble Theater (King Features).Tarzan (1912) Created by Edgar Rice Burroughs for the novel Tarzan of the Apes.Forrest Gump (1986)  Created by Winston Groom for novel Forrest Gump.  Later portrayed by Tom Hanks in Zemeckis’ film adaptation.Hannibal Lector (1981)  Created by Thomas Harris for the novel Red Dragon. Portrayed most famously by Anthony Hopkins in the 1991 Jonathan Demme film The Silence of the Lambs.
Big Bird (1969) Created by Jim Henson and portrayed by Carroll Spinney for Sesame Street.Holden Caulfield (1945) Created by J.D. Salinger for the Collier’s story “I’m Crazy.”  Reworked into the novel The Catcher in the Rye in 1951.Tony Montana (1983)  Created by Oliver Stone for film Scarface.  Portrayed by Al Pacino.Tony Soprano (1999)  Created by David Chase for The Sopranos. Portrayed by James Gandolfini.
The Terminator (1984)  Created by James Cameron and Gale Anne Hurd for The Terminator. Portrayed by Arnold Schwarzenegger.Jon Snow (1996)  Created by George RR Martin for the novel The Game of Thrones.  Portrayed by Kit Harrington.Charles Foster Kane (1941)  Created and portrayed by Orson Welles for Citizen Kane.Scarlett O’Hara (1936)  Created by Margaret Mitchell for the novel Gone With the Wind. Portrayed most famously by Vivien Leigh 
for the 1939 Victor Fleming film adaptation.Marty McFly (1985) Created by Robert Zemeckis and Bob Gale for Back to the Future. Portrayed by Michael J. Fox.Rick Blaine (1940)  Created by Murray Burnett and Joan Alison for the unproduced stage play Everybody Comes to Rick’s. Later portrayed by Humphrey Bogart in Michael Curtiz’s film adaptation Casablanca.Man With No Name (1964)  Created by Sergio Leone for A Fistful of Dollars, which was adapted from a ronin character in Kurosawa’s Yojimbo (1961).  Portrayed by Clint Eastwood.Charlie Brown (1948)  Created by Charles M. Shultz for the comic strip L’il Folks; popularized two years later in Peanuts.E.T. (1982)  Created by Melissa Mathison for the film E.T.: the Extra-Terrestrial.Arthur Fonzarelli (1974)  Created by Bob Brunner for the show Happy Days. Portrayed by Henry Winkler.)Phillip Marlowe (1939)  Created by Raymond Chandler for the novel The Big Sleep.Jay Gatsby (1925)  Created by F. Scott Fitzgerald for the novel The Great Gatsby.Lassie (1938) Created by Eric Knight for a Saturday Evening Post story, later turned into the novel Lassie Come-Home in 1940, film adaptation in 1943, and long-running television show in 1954.  Most famously portrayed by the dog Pal.
Fred Flintstone (1959)  Created by William Hanna and Joseph Barbera for The Flintstones. Voiced most notably by Alan Reed. Rooster Cogburn (1968)  Created by Charles Portis for the novel True Grit. Most famously portrayed by John Wayne in the 1969 film adaptation. Atticus Finch (1960)  Created by Harper Lee for the novel To Kill a Mockingbird.  (Appeared in the earlier work Go Set A Watchman, though this was not published until 2015)  Portrayed most famously by Gregory Peck in the Robert Mulligan film adaptation. Kermit the Frog (1955)  Created and performed by Jim Henson for the show Sam and Friends. Later popularized in Sesame Street (1969) and The Muppet Show (1976) George Bailey (1943)  Created by Phillip Van Doren Stern (then as George Pratt) for the short story The Greatest Gift. Later adapted into Capra’s It’s A Wonderful Life, starring James Stewart as the renamed George Bailey. Yoda (1980) Created by George Lucas for The Empire Strikes Back. Sam Malone (1982)  Created by Glen and Les Charles for the show Cheers.  Portrayed by Ted Danson. Zorro (1919)  Created by Johnston McCulley for the All-Story Weekly pulp magazine story The Curse of Capistrano.Later adapted to the Douglas Fairbanks’ film The Mark of Zorro (1920).Moe, Larry, and Curly (1928)  Created by Ted Healy for the vaudeville act Ted Healy and his Stooges. Mary Poppins (1934)  Created by P.L. Travers for the children’s book Mary Poppins. Ron Burgundy (2004)  Created by Will Ferrell and Adam McKay for the film Anchorman: The Legend of Ron Burgundy.  Portrayed by Will Ferrell. Mario (1981)  Created by Shigeru Miyamoto for the video game Donkey Kong. Harry Potter (1997)  Created by J.K. Rowling for the novel Harry Potter and the Philosopher’s Stone. The Dude (1998)  Created by Ethan and Joel Coen for the film The Big Lebowski. Portrayed by Jeff Bridges.
Gandalf (1937)  Created by J.R.R. Tolkien for the novel The Hobbit. The Grinch (1957)  Created by Dr. Seuss for the story How the Grinch Stole Christmas! Willy Wonka (1964)  Created by Roald Dahl for the children’s novel Charlie and the Chocolate Factory. The Hulk (1962)  Created by Stan Lee and Jack Kirby for The Incredible Hulk #1 (Marvel Comics) Scooby-Doo (1969)  Created by Joe Ruby and Ken Spears for the show Scooby-Doo, Where Are You! George Costanza (1989)  Created by Larry David and Jerry Seinfeld for the show Seinfeld.  Portrayed by Jason Alexander.Jules Winfield (1994)  Created by Quentin Tarantino for the film Pulp Fiction. Portrayed by Samuel L. Jackson. John McClane (1988)  Based on the character Detective Joe Leland, who was created by Roderick Thorp for the novel Nothing Lasts Forever. Later adapted into the John McTernan film Die Hard, starring Bruce Willis as McClane. Ellen Ripley (1979)  Created by Don O’cannon and Ronald Shusett for the film Alien.  Portrayed by Sigourney Weaver. Ralph Kramden (1951)  Created and portrayed by Jackie Gleason for “The Honeymooners,” which became its own show in 1955.Edward Scissorhands (1990)  Created by Tim Burton for the film Edward Scissorhands.  Portrayed by Johnny Depp.Eric Cartman (1992)  Created by Trey Parker and Matt Stone for the animated short Jesus vs Frosty.  Later developed into the show South Park, which premiered in 1997.  Voiced by Trey Parker.
Walter White (2008)  Created by Vince Gilligan for Breaking Bad.  Portrayed by Bryan Cranston. Cosmo Kramer (1989)  Created by Larry David and Jerry Seinfeld for Seinfeld.  Portrayed by Michael Richards.Pikachu (1996)  Created by Atsuko Nishida and Ken Sugimori for the Pokemon video game and anime franchise.Michael Scott (2005)  Based on a character from the British series The Office, created by Ricky Gervais and Steven Merchant.  Portrayed by Steve Carell.Freddy Krueger (1984)  Created by Wes Craven for the film A Nightmare on Elm Street. Most famously portrayed by Robert Englund.
Captain America (1941)  Created by Joe Simon and Jack Kirby for Captain America Comics #1 (Marvel Comics)Goku (1984)  Created by Akira Toriyama for the manga series Dragon Ball Z.Bambi (1923)  Created by Felix Salten for the children’s book Bambi, a Life in the Woods. Later adapted into the Disney film Bambi in 1942.Ronald McDonald (1963) Created by Williard Scott for a series of television spots.Waldo/Wally (1987) Created by Martin Hanford for the children’s book Where’s Wally? (Waldo in US edition) Frasier Crane (1984)  Created by Glen and Les Charles for Cheers.  Portrayed by Kelsey Grammar.Omar Little (2002)  Created by David Simon for The Wire.Portrayed by Michael K. Williams.
Wolverine (1974)  Created by Roy Thomas, Len Wein, and John Romita Sr for The Incredible Hulk #180 (Marvel Comics) Jason Voorhees (1980)  Created by Victor Miller for the film Friday the 13th. Betty Boop (1930)  Created by Max Fleischer and the Grim Network for the cartoon Dizzy Dishes. Bilbo Baggins (1937)  Created by J.R.R. Tolkien for the novel The Hobbit. Tom Joad (1939)  Created by John Steinbeck for the novel The Grapes of Wrath. Later adapted into the 1940 John Ford film and portrayed by Henry Fonda.Tony Stark (Iron Man) (1963)  Created by Stan Lee, Larry Lieber, Don Heck and Jack Kirby for Tales of Suspense #39 (Marvel Comics)Porky Pig (1935)  Created by Friz Freleng for the animated short film I Haven’t Got a Hat. Voiced most famously by Mel Blanc.Travis Bickle (1976)  Created by Paul Schrader for the film Taxi Driver. Portrayed by Robert De Niro.
Hawkeye Pierce (1968)  Created by Richard Hooker for the novel MASH: A Novel About Three Army Doctors.  Famously portrayed by both Alan Alda and Donald Sutherland. Don Draper (2007)  Created by Matthew Weiner for the show Mad Men.  Portrayed by Jon Hamm. Cliff Huxtable (1984)  Created and portrayed by Bill Cosby for The Cosby Show. Jack Torrance (1977)  Created by Stephen King for the novel The Shining. Later adapted into the 1980 Stanley Kubrick film and portrayed by Jack Nicholson. Holly Golightly (1958)  Created by Truman Capote for the novella Breakfast at Tiffany’s.  Later adapted into the 1961 Blake Edwards films starring Audrey Hepburn as Holly. Shrek (1990)  Created by William Steig for the children’s book Shrek! Later adapted into the 2001 film starring Mike Myers as the titular character. Optimus Prime (1984)  Created by Dennis O’Neil for the Transformers toy line.Sonic the Hedgehog (1991)  Created by Naoto Ohshima and Yuji Uekawa for the Sega Genesis game of the same name.Harry Callahan (1971)  Created by Harry Julian Fink and R.M. Fink for the movie Dirty Harry.  Portrayed by Clint Eastwood.Bubble: Hercule Poirot, Tyrion Lannister, Ron Swanson, Cercei Lannister, J.R. Ewing, Tyler Durden, Spongebob Squarepants, The Genie from Aladdin, Pac-Man, Axel Foley, Terry Malloy, Patrick Bateman
Pre-20th Century: Santa Claus, Dracula, Robin Hood, Cinderella, Huckleberry Finn, Odysseus, Sherlock Holmes, Romeo and Juliet, Frankenstein, Prince Hamlet, Uncle Sam, Paul Bunyan, Tom Sawyer, Pinocchio, Oliver Twist, Snow White, Don Quixote, Rip Van Winkle, Ebenezer Scrooge, Anna Karenina, Ichabod Crane, John Henry, The Tooth Fairy,
Br’er Rabbit, Long John Silver, The Mad Hatter, Quasimodo """
# create the doc from the text
my_doc = nlp(my_text)
### initialuze the PhraseMatcher ###
matcher = PhraseMatcher(nlp.vocab) # using .vocab
### set the phrases/terms we are looking for ###
terms_list = ['Bruce Wayne', 'Tony Stark', 'Batman', 'Harry Potter', 'Severus Snape']
# create the pattern to use 
patterns = [nlp.make_doc(text) for text in terms_list]
### add the matcher ###
matcher.add("phrase_matcher", None, *patterns) # match_id = name of 'pattern' , match_on = None, patterns = my_pattern
# run the text doc through the matcher
character_matches = matcher(my_doc)
character_matches
### loop through each match, create string of info, pull text from doc ###
for match_id, start, end in character_matches:
    span = my_doc[start:end]
    print(span.text)

### using the LOWER attribute parameter ###
### load in the text to use ###  
my_text = 'I wish to visit new york city'
# create the doc from the text
my_doc = nlp(my_text)
### set the phrases/terms we are looking for ###
terms = ['New York']
# create the pattern to be used 
pattern = [nlp(term) for term in terms]
### add the matcher ###
case_insensitive_matcher = PhraseMatcher(nlp.vocab, attr = "LOWER") # set attribute could be lowercase
case_insensitive_matcher.add("matcher", None, *pattern) # match_id = name of 'pattern' , match_on = None, patterns = my_pattern
# run the text doc through the matcher
my_matches = case_insensitive_matcher(my_doc)
my_matches

### using the SHAPE attribute parameter ###
### load in the text to use ###  
my_text = '''From 8 am , Mr.X will be speaking on your favorite chanel 191.1. Afterward there shall be an exclusive interview with actor Vijay on channel 194.1 . 
              Hope you are having a great day. Call us on 666666'''
# create the doc from the text
my_doc = nlp(my_text)
### set the shape of the phrase ###
term = '134.4' # will look for ###.#
# create the pattern to be used 
pattern = nlp(term)
### add the matcher ###
pincode_matcher= PhraseMatcher(nlp.vocab,attr="SHAPE") # set the shape of the attribute
pincode_matcher.add("pincode_matching", None, pattern) # match_id = name of 'pattern' , match_on = None, patterns = my_pattern
# run the text doc through the matcher
matches = pincode_matcher(my_doc)
matches
### loop through each match, create string of info, pull text from doc ###
for match_id, start, end in matches:
  span = my_doc[start:end]
  print(span.text)

### entity ruler ### 
# use when detecting entities and some names/organizations are not recognized 
### import ###
from spacy.pipeline import EntityRuler
### add additional entities 'books' when matching example ###
### load in the text to use ###  
my_text = " I recently published my work fanfiction by Dr.X . Right now I'm studying the book of my friend .You should try My guide to statistics for clear concepts."
ruler = EntityRuler(nlp)
### create the pattern to be used ###
pattern = [{"label": "WORK_OF_ART", "pattern": "My guide to statistics"}] # [{label = work of art}{ pattern = entity for detection} ]
ruler.add_patterns(pattern) # add the pattern to the ruler
nlp.add_pipe(ruler)# add the ruler pipe to the nlp
### run the nlp on the text doc ###
my_doc = nlp(my_text)
### list the works of art entities ###
works_of_art = []
for ent in my_doc.ents:
  works_of_art.append((ent.text, ent.label_))
works_of_art


''' word vectors & similarity '''
### word vectors ###
 ### word vectors are numerical representations of words and documents ###
# helps understand semantics of the word
# can be used for tasks like clasification
# words with similar meaning and context appear closer together numerically

### check if words have a vector, unkown words may not have a vector ###
### all have vectors example ###
### load in the text to use ###  
my_text = "I am an excellent cook"
### run the nlp on the text doc ###
my_doc = nlp(my_text)
### check if tokens have a vector ###
for token in my_doc:
  print(token.text ,' ',token.has_vector)

  ### not all have vectors example ###
### load in the text to use ###  
my_text = "I wish to go to hogwarts lolXD "
### run the nlp on the text doc ###
my_doc = nlp(my_text)
### check if tokens have a vector ###
for token in my_doc:
  print(token.text ,' ',token.has_vector)

### access the vectors of the tokens ### 
### example not all have vectors ###
### load in the text to use ###  
my_text = "I wish to go to hogwarts lolXD "
### run the nlp on the text doc ###
my_doc = nlp(my_text)
### list the tokens and their full vectors ###
vectors = []
for token in my_doc:
  vectors.append((token.text, token.vector))
vectors
### list the tokens and their L2 norm vectors ###
### no vectors = 0 ###
vectors = []
for token in my_doc:
  vectors.append((token.text, token.vector_norm))
vectors

### similarity ###
### find similar tokens example ###
my_text1 = 'bad'
my_doc1 = nlp(my_text1)
my_text2 = 'terrible'
my_doc2 = nlp(my_text2)
### compare the docs together with similarity ###
similarity_score = my_doc1.similarity(my_doc2)
similarity_score

### find similar tokens example ###
### load in the text to use ###  
my_text1 = ' The food was amazing'
### run the nlp on the doc ###
my_doc1 = nlp(my_text1)
my_text2 = 'The food was excellent'
my_doc2 = nlp(my_text2)
my_text3 = 'pizza'
my_doc3 = nlp(my_text3)
my_text4 = 'chair'
my_doc4 = nlp(my_text4)
### compare the docs together with similarity ###
### high score high similarity ###
similarity_score = my_doc1.similarity(my_doc2)
similarity_score
### compare the docs together with similarity ###
### low score irrelevant similarity ###
similarity_score = my_doc3.similarity(my_doc4)
similarity_score


''' merge & split tokens '''
### merge tokens together that may get split up in parsing example ###
### load in the text to use ### 
my_text = 'John Wick is a 2014 American action thriller film directed by Chad Stahelski'
### run the nlp on the doc ###
my_doc = nlp(my_text)
### list of tokens ###
### names tokens have been split ###
tokens = []
for token in my_doc:
  tokens.append(token)
print(len(tokens))
print(tokens)
### use the retokenize function with merge to fix john wick ###
with my_doc.retokenize() as retokenizer:
    attrs = {"POS": "PROPN"} # set the attribute in change to proper noun, name
### use merge on the retokenizer ###
    retokenizer.merge(my_doc[0:2], attrs=attrs) # span = my_doc[index slice of the tokens to be merge], attribute = attribute created 
### list of tokens ###
### john wick is fixed ###
tokens = []
for token in my_doc:
  tokens.append(token)
print(len(tokens))
print(tokens)

### split tokens apart that are grouped in parsing example ###
### load in the text to use ### 
my_text = 'I purchased the trendy OnePlus7'
### run the nlp on the doc ###
my_doc = nlp(my_text)
### use the retokenize function with split to fix oneplus7 ###
with my_doc.retokenize() as retokenizer:
    heads = [(my_doc[3], 1), my_doc[2]] # heads of tokens to attach newly split subtokens
    retokenizer.split(my_doc[4], ["OnePlus", "7"], heads = heads) # index of token to split, how to split, heads = heads 
### list of tokens ###
### OnePlus7 is split ###
tokens = []
for token in my_doc:
  tokens.append(token)
print(len(tokens))
print(tokens)


''' pipelines '''
### built in pipeline components ###
# Tokenizer, It is responsible for segmenting the text into tokens are turning a Doc object. This the first and compulsory step in a pipeline
# Tagger, It is responsible for assigning Part-of-speech tags. It takes a Doc as input and createsDoc[i].tag
# DependencyParser, It is known as parser. It is responsible for assigning the dependency tags to each token. It takes a Doc as input and returns the processed Doc
# EntityRecognizer, This component is referred as ner. It is responsible for identifying named entities and assigning labels to them
# TextCategorizer, This component is called textcat. It will assign categories to Docs
# EntityRuler, This component is called * entity_ruler*.It is responsible for assigning named entitile based on pattern rules. Revisit Rule Based Matching to know more
# Sentencizer, This component is called **sentencizer** and can perform rule based sentence segmentation
# merge_noun_chunks, It is called mergenounchunks. This component is responsible for merging all noun chunks into a single token. It has to be add in the pipeline after tagger and parser
# merge_entities, It is called merge_entities .This component can merge all entities into a single token. It has to added after the ner
# merge_subtokens, It is called merge_subtokens. This component can merge the subtokens into a single token

### with custom pipeline if using a different component rather than existing, nlp.replace_pipe

### inspect the available pipeline components ###
### load in the language file ###
nlp = spacy.load("en_core_web_lg")
print(nlp.pipe_names) 
### check if the pipeline compenent exists ###
nlp.has_pipe('textcat')
### add components to the pipeline ### 
nlp.add_pipe(nlp.create_pipe('textcat')) # add the component to the pipe with create_pipe
print(nlp.pipe_names) # pipenames to inspect 
### add components to the pipeline with parameter ### 
# specify where componenet is added with before, after, first, last, default last = true 
nlp.add_pipe(nlp.create_pipe('textcat'), before = 'parser') # add the component to the pipeline
print(nlp.pipe_names) 
### remove components of the pipeline ### 
nlp.remove_pipe('parser') # remove the component to the pipeline
print(nlp.pipe_names)  
### rename components of the pipeline ### 
nlp.rename_pipe(old_name = 'ner', new_name = 'custom_ner')
print(nlp.pipe_names) 


''' efficiency '''
### time efficiency with %%timeit ###
# running with .pipe is much more efficient 
# only use the pipeline components you need

### use %%timeit to see speed ###
%%timeit
### load in the text to use ### 
my_text = '''In computer science, artificial intelligence AI, sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.','Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.','Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving','As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.','The term military simulation can cover a wide spectrum of activities, ranging from full-scale field-exercises,[2] to abstract computerized models that can proceed with little or no human involvement','As a general scientific principle, the most reliable data comes from actual observation and the most reliable theories depend on it.[4] This also holds true in military analysis','Any form of training can be regarded as a "simulation" in the strictest sense of the word (inasmuch as it simulates an operational environment); however, many if not most exercises take place not to test new ideas or models, but to provide the participants with the skills to operate within existing ones.','ull-scale military exercises, or even smaller-scale ones, are not always feasible or even desirable. Availability of resources, including money, is a significant factor—it costs a lot to release troops and materiel from any standing commitments, to transport them to a suitable location, and then to cover additional expenses such as petroleum, oil and lubricants (POL) usage, equipment maintenance, supplies and consumables replenishment and other items','Moving away from the field exercise, it is often more convenient to test a theory by reducing the level of personnel involvement. Map exercises can be conducted involving senior officers and planners, but without the need to physically move around any troops. These retain some human input, and thus can still reflect to some extent the human imponderables that make warfare so challenging to model, with the advantage of reduced costs and increased accessibility. A map exercise can also be conducted with far less forward planning than a full-scale deployment, making it an attractive option for more minor simulations that would not merit anything larger, as well as for very major operations where cost, or secrecy, is an issue'''
my_doc = nlp(my_text)
### use %%timeit to see speed ###
%%timeit
### load in the text to use ### 
my_text = '''In computer science, artificial intelligence AI, sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.','Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.','Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving','As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.','The term military simulation can cover a wide spectrum of activities, ranging from full-scale field-exercises,[2] to abstract computerized models that can proceed with little or no human involvement','As a general scientific principle, the most reliable data comes from actual observation and the most reliable theories depend on it.[4] This also holds true in military analysis','Any form of training can be regarded as a "simulation" in the strictest sense of the word (inasmuch as it simulates an operational environment); however, many if not most exercises take place not to test new ideas or models, but to provide the participants with the skills to operate within existing ones.','ull-scale military exercises, or even smaller-scale ones, are not always feasible or even desirable. Availability of resources, including money, is a significant factor—it costs a lot to release troops and materiel from any standing commitments, to transport them to a suitable location, and then to cover additional expenses such as petroleum, oil and lubricants (POL) usage, equipment maintenance, supplies and consumables replenishment and other items','Moving away from the field exercise, it is often more convenient to test a theory by reducing the level of personnel involvement. Map exercises can be conducted involving senior officers and planners, but without the need to physically move around any troops. These retain some human input, and thus can still reflect to some extent the human imponderables that make warfare so challenging to model, with the advantage of reduced costs and increased accessibility. A map exercise can also be conducted with far less forward planning than a full-scale deployment, making it an attractive option for more minor simulations that would not merit anything larger, as well as for very major operations where cost, or secrecy, is an issue'''
my_doc = nlp(my_text)
### use %%timeit to see speed ###
%%timeit
### load in the text to use ### 
text_list = ['In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.','Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.','Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving','As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.','The term military simulation can cover a wide spectrum of activities, ranging from full-scale field-exercises,[2] to abstract computerized models that can proceed with little or no human involvement','As a general scientific principle, the most reliable data comes from actual observation and the most reliable theories depend on it.[4] This also holds true in military analysis','Any form of training can be regarded as a "simulation" in the strictest sense of the word (inasmuch as it simulates an operational environment); however, many if not most exercises take place not to test new ideas or models, but to provide the participants with the skills to operate within existing ones.','ull-scale military exercises, or even smaller-scale ones, are not always feasible or even desirable. Availability of resources, including money, is a significant factor—it costs a lot to release troops and materiel from any standing commitments, to transport them to a suitable location, and then to cover additional expenses such as petroleum, oil and lubricants (POL) usage, equipment maintenance, supplies and consumables replenishment and other items','Moving away from the field exercise, it is often more convenient to test a theory by reducing the level of personnel involvement. Map exercises can be conducted involving senior officers and planners, but without the need to physically move around any troops. These retain some human input, and thus can still reflect to some extent the human imponderables that make warfare so challenging to model, with the advantage of reduced costs and increased accessibility. A map exercise can also be conducted with far less forward planning than a full-scale deployment, making it an attractive option for more minor simulations that would not merit anything larger, as well as for very major operations where cost, or secrecy, is an issue']
my_doc = [nlp(text) for text in text_list]
### use %%timeit to see speed ###
%%timeit
### load in the text to use ### 
text_list = ['In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.','Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.','Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving','As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.','The term military simulation can cover a wide spectrum of activities, ranging from full-scale field-exercises,[2] to abstract computerized models that can proceed with little or no human involvement','As a general scientific principle, the most reliable data comes from actual observation and the most reliable theories depend on it.[4] This also holds true in military analysis','Any form of training can be regarded as a "simulation" in the strictest sense of the word (inasmuch as it simulates an operational environment); however, many if not most exercises take place not to test new ideas or models, but to provide the participants with the skills to operate within existing ones.','ull-scale military exercises, or even smaller-scale ones, are not always feasible or even desirable. Availability of resources, including money, is a significant factor—it costs a lot to release troops and materiel from any standing commitments, to transport them to a suitable location, and then to cover additional expenses such as petroleum, oil and lubricants (POL) usage, equipment maintenance, supplies and consumables replenishment and other items','Moving away from the field exercise, it is often more convenient to test a theory by reducing the level of personnel involvement. Map exercises can be conducted involving senior officers and planners, but without the need to physically move around any troops. These retain some human input, and thus can still reflect to some extent the human imponderables that make warfare so challenging to model, with the advantage of reduced costs and increased accessibility. A map exercise can also be conducted with far less forward planning than a full-scale deployment, making it an attractive option for more minor simulations that would not merit anything larger, as well as for very major operations where cost, or secrecy, is an issue']
my_doc = list(nlp.pipe(text_list))


### disabling pipeline components for entire project ###
### load in the language file and disabled components ###
nlp = spacy.load('en_core_web_lg', disable=["ner", "parser"])
print(nlp.has_pipe('ner'))
print(nlp.has_pipe('parser'))
### disabling pipeline components temporarily in process ###
### load in the language file ###
nlp = spacy.load('en_core_web_lg')
### load in the text to use ### 
text_list = ['In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.','Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.','Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving','As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.','The term military simulation can cover a wide spectrum of activities, ranging from full-scale field-exercises,[2] to abstract computerized models that can proceed with little or no human involvement','As a general scientific principle, the most reliable data comes from actual observation and the most reliable theories depend on it.[4] This also holds true in military analysis','Any form of training can be regarded as a "simulation" in the strictest sense of the word (inasmuch as it simulates an operational environment); however, many if not most exercises take place not to test new ideas or models, but to provide the participants with the skills to operate within existing ones.','ull-scale military exercises, or even smaller-scale ones, are not always feasible or even desirable. Availability of resources, including money, is a significant factor—it costs a lot to release troops and materiel from any standing commitments, to transport them to a suitable location, and then to cover additional expenses such as petroleum, oil and lubricants (POL) usage, equipment maintenance, supplies and consumables replenishment and other items','Moving away from the field exercise, it is often more convenient to test a theory by reducing the level of personnel involvement. Map exercises can be conducted involving senior officers and planners, but without the need to physically move around any troops. These retain some human input, and thus can still reflect to some extent the human imponderables that make warfare so challenging to model, with the advantage of reduced costs and increased accessibility. A map exercise can also be conducted with far less forward planning than a full-scale deployment, making it an attractive option for more minor simulations that would not merit anything larger, as well as for very major operations where cost, or secrecy, is an issue']
### run the text through the pipeline with the temporarily disabled components
for doc in nlp.pipe(text_list, disable=["ner", "parser"]):
  print(doc.is_tagged)
  ### disabling pipeline components for a whole block ###
### load in the language file ###
nlp = spacy.load('en_core_web_lg')
my_text = ' The pandemic has disrupted the lives of may'
with nlp.disable_pipes('tagger', 'ner'):
    print('-- Inside the block--')
    my_doc = nlp(my_text)
    print(my_doc.is_nered)
print('-- outside the block--')
my_doc = nlp("I will be tagged and parsed")
my_doc.is_nered


''' custom pipelines '''
### custom made pipelines ### 
# component, have to pass the function_name as input . This serves as our component
# name,  assign a name to the component. The component can be called using this name. If you don’t provide any ,the function_name will be taken as name of the component
# first/last, if you want the new component to be added first or last ,you can setfirst=True or last=True accordingly
# before/after, if you want to add the component specifically before or after another component , you can use these arguments
# only 1 before/after, first/last can be set at once time

### custom pipline adding component example ###
### load in the language file ###
nlp = spacy.load('en_core_web_lg')
### custom component function ### 
def my_custom_component(my_doc):
    doc_length = len(my_doc)
    print(' The no of tokens in the document ', doc_length)
    named_entity = [token.label_ for token in my_doc.ents]
    print(named_entity)
    # return the doc
    return my_doc

nlp.add_pipe(my_custom_component, after='ner') # add the function to the pipeline, after 'ner'
print(nlp.pipe_names)
my_text = 'The Hindu Newspaper has increased the cost. I usually read the paper on my way to Delhi railway station.'
my_doc = nlp(my_text)

### adding a custom component to pipeline that uses PhraseMatcher example ### 
### import ###
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_lg")
matcher = PhraseMatcher(nlp.vocab)
### list of book names to match ###
book_names = ['Pride and prejudice','Mansfield park','The Tale of Two cities','Great Expectations']
### create pattern to use for matcher ###
book_patterns = list(nlp.pipe(book_names))
### add the pattern to the matcher ###
matcher.add("identify_books", None, *book_patterns)

### import ###
from spacy.tokens import Span
### custom pipeline component function ###
def identify_books(my_doc):
    matches = matcher(my_doc) # run the my_doc through the matcher 
    # Create a Span for each match and assign them under label "BOOKS"
    spans = [Span(my_doc, start, end, label="BOOKS") for match_id, start, end in matches] # create span for each match, assign label 'BOOKS'
    my_doc.ents = spans # store the matches span to the my_doc
    return my_doc
### add the custom function to the componenets after 'ner' ###
nlp.add_pipe(identify_books, after="ner")
### load the text to be used ###
my_text = 'The library has got several new copies of Mansfield park and Great Expectations . I have filed a suggestion to buy more copies of The Tale of Two cities'
### run the text through the nlp
my_doc = nlp(my_text)
print([(ent.text, ent.label_) for ent in my_doc.ents])
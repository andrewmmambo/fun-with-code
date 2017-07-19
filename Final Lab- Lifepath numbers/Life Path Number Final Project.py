# coding=utf-8 (Do not delete coding=utf-8)
#####################################################################################
# FINAL LAB PROJECT
# CSC 226-SOFTWARE DESIGN AND IMPLEMENTATION
# Authors: Saffa Gbondo and Marima Andrew Mambondiumwe
#
# ######### ACKNOWLEDGEMENTS ################# ACKNOWLEDGEMENTS #######################
# Dr Jan Pearce and Ashley Aiken
# Concept and idea obtained from http://seventhlifepath.com/ and http://stackoverflow.com/
#
# Life Path number interpretations and meanings obtained from http://www.tokenrock.com/numerology/life-path-1.html
# and from http://seventhlifepath.com/
# Original code and idea obtained from : http: // cs.berea.edu / courses / csc226 / tasks / a9.lifepath.html
# Original code was written by Saffa Gbondo with consultation from Ashley Aiken
#
# Consultations: Newboston youtube Python GUI with Tkinter tutorial videos
#                https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
#
# All images obtained from www.google.com/images
# https://www.google.com/search?q=lifepath+images&espv=2&biw=1220&bih=554&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjespOQl5vMAhXMbD4KHWOWAgIQ_AUIBygC
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#######################################################################################################################

from Tkinter import *                                                   # this imports the Tkinter library


class MainLoopArea:
    """this opens a window and allows the user to input in values that will calculate the lifepath number
    and show the meaning or intepretation of that life path number"""
    def __init__(self, master):      # the initializer method acts as the constructor and initializes the parent window
        """initializes the values to be used in the class and acts as a constructor"""
        frame = Frame(master)  # this creates a frame widget for grouping and organizing the layout on the master window
        frame.grid(column=1000, row=1000, sticky=(N, W, E, S))
        # creates a grid that organizes widgets in a table-like structure
        frame.pack()           # this packs and displays widgets in rows and columns

        # ************** IMAGES ************* Imports and saves images
        self.photo1 = PhotoImage(file="1.gif")              # imports and saves the image for lifepath number 1
        self.photo2 = PhotoImage(file="2.gif")              # imports and saves the image for lifepath number 2
        self.photo3 = PhotoImage(file="3.gif")              # imports and saves the image for lifepath number 3
        self.photo4 = PhotoImage(file="4.gif")              # imports and saves the image for lifepath number 4
        self.photo5 = PhotoImage(file="5.gif")              # imports and saves the image for lifepath number 5
        self.photo6 = PhotoImage(file="6.gif")              # imports and saves the image for lifepath number 6
        self.photo7 = PhotoImage(file="7.gif")              # imports and saves the image for lifepath number 7
        self.photo8 = PhotoImage(file="8.gif")              # imports and saves the image for lifepath number 8
        self.photo9 = PhotoImage(file="9.gif")              # imports and saves the image for lifepath number 9
        self.photo11 = PhotoImage(file="11.gif")            # imports and saves the image for lifepath number 11
        self.photo22 = PhotoImage(file="22.gif")            # imports and saves the image for lifepath number 22
        self.photo33 = PhotoImage(file="33.gif")            # imports and saves the image for lifepath number 33

        # ************** Font Style *************
        self.customFont = ('times', 15, 'bold', 'italic')  # Sets font to the new values
        self.customFont1 = ('times', 10, 'bold', 'italic')  # Sets font to the new values

        # ********************************** Variables used  *****************************
        self.user_date = StringVar()                        # takes the user input and converts it to a string variable
        self.user_year = StringVar()                        # takes the user input and converts it to a string variable
        self.List1 = StringVar()                            # takes the user input and converts it to a string variable

        # ********************************** Labels   ***********************************
        self.developed = Label(frame, text="© 2016. Copyrights: Gbondo Saffa and Mambondiumwe Andrew")
        # creates a label that displays text
        self.sayHello = Label(frame, text="Hello Welcome to the life path number game")
        # creates a label that displays text
        self.introduction = Label(frame, text="The Life Path is the sum of your birth date. This number represents who "
                                              "you are at birth \n and the native traits that you will carry with you "
                                              "through life. The most important \n number that will be discussed here "
                                              "is your Life Path number. The Life Path describes \n the nature of this "
                                              "journey through life.")  # creates a label that displays text

        # ********************************** Buttons Used  ***********************************
        self.quitButton = Button(frame, text="QUIT", command=frame.quit, fg="White", bg="Red", font=self.customFont)
        # this creates a quit button
        self.startProgram = Button(frame, text="START", command=self.statement, fg="White", bg="Blue",
                                   font=self.customFont)
        # this starts the game

        # ************************** It is necessary to pack labels so as to display them  *****************************
        self.developed.pack()                   # this displays the text the self.developed
        self.sayHello.pack()                    # this displays the text in self.hello
        self.introduction.pack()                # this displays the text in self.introduction
        self.quitButton.pack(side=RIGHT)        # this displays and sets  the position of the quitButton
        self.startProgram.pack(side=LEFT)       # this displays and sets the position of the start button

    def statement(self):
        """calls the methods"""
        self.day_entry()
        self.year_entry()
        self.month_entry()
        self.submit_button()

    def submit_button(self):
        """allows input to be submitted so that the lifepath number can be calculated"""
        Button(root, text="SUBMIT", command=self.life_path, fg="Black", bg="Green", font=self.customFont1).pack()
        # Creates and displays the submit button and calls the method,self.life_path

    def day_entry(self):
        """for inputting in the day"""
        Label(root, text="Enter DAY of birth").pack()
        # this displays a label that tells the user to enter in his day of birth
        Entry(root, textvariable=self.user_date).pack()   # allows the user to enter in his day of birth in the textbox

    def year_entry(self):
        """for inputting the year"""
        Label(root, text="Enter YEAR of birth").pack()
        # this displays a label that tells the user to enter in his year of birth
        Entry(root, textvariable=self.user_year).pack()   # allows the user to enter in his day of birth in the textbox

    def month_entry(self):
        """for inputting in the month"""
        Label(root, text="Select Your MONTH of birth").pack()
        # this displays a label that tells the user to enter in his month of birth
        self.List1 = Listbox(root, height=12)     # this creates a list box that contains options the user can pick from
        self.List1.insert(1, "January")
        self.List1.insert(2, "February")
        self.List1.insert(3, "March")
        self.List1.insert(4, "April")
        self.List1.insert(5, "May")
        self.List1.insert(6, "June")
        self.List1.insert(7, "July")
        self.List1.insert(8, "August")
        self.List1.insert(9, "September")
        self.List1.insert(10, "October")
        self.List1.insert(11, "November")
        self.List1.insert(12, "December")
        self.List1.pack()                                       # this displays the option that is selected by the user

    def get_month(self):
        """converts the user's choice of a month to a corresponding digit"""
        month = str((self.List1.get(ACTIVE)))  # The get active retrieves the information in the month input

        # *************** Below is a bunch of if and elif statements to check the selected months **********************
        if month == "January":
            return 1
        elif month == "February":
            return 2
        elif month == "March":
            return 3
        elif month == "April":
            return 4
        elif month == "May":
            return 5
        elif month == "June":
            return 6
        elif month == "July":
            return 7
        elif month == "August":
            return 8
        elif month == "September":
            return 9
        elif month == "October":
            return 1
        elif month == "November":
            return 11
        else:
            return 3

    def get_year(self):
        """calculates the total of the digits in the inputted year"""
        my_text = self.user_year.get()          # assigns a variable
        digit_list = []                         # creates an empty list
        for letter in my_text:                  # adds the letters in my text to the list
            digit_list.append(int(letter))
        my_sum = sum(digit_list)                # adds the numbers in the list
        if my_sum == 11 or my_sum == 22 or my_sum == 33:
            return my_sum
        else:
            year_list = []
            for num in str(my_sum):
                year_list.append(int(num))
            my_sum = sum(year_list)
            return my_sum

    def get_date(self):
        """calculates the total of the digits in the inputted date"""
        m_date = self.user_date.get()           # assigns a variable
        digit_list = []                         # creates an empty list
        for letter in m_date:                   # adds the letters in the date to the list
            digit_list.append(int(letter))
        my_sum = sum(digit_list)                # adds the numbers in the list
        if my_sum == 11 or my_sum == 22 or my_sum == 33:
            return my_sum
        else:
            month_list = []
            for num in str(my_sum):
                month_list.append(int(num))
            month_sum = sum(month_list)
            return month_sum

    def add_total(self):
        """calculates the lifepath number"""
        total = str(self.get_date() + self.get_month() + self.get_year())  # calculates the total of all inputted values
        total_sum = int(total)
        if total_sum == 11 or total_sum == 22 or total_sum == 33:
            return total_sum
        else:
            digit_lists = []                       # creates an empty list
            for num in str(total_sum):
                digit_lists.append(int(num))       # adds all totals into the list
            final = sum(digit_lists)
            return final

        # **** All explanations/meanings of life path were taken from http://seventhlifepath.com  ********************
    def life_path(self):
        """uses the lifepath number to display its interpretation"""
        sums = int(self.add_total())           # converts the total to an integer
        if sums == 1 or sums == 10:
            Label(root, image=self.photo1).place(x=0, y=0, relwidth=0.25, relheight=0.4)        # displays the image
            Label(root,
                  text=("A person with Life Path 1 is hard working, a natural born leader, has a pioneering"
                        " spirit that is full of energy, and a passion for art. \n They have a strong desire to be "
                        "number one, which means a person with this number can manifest very easily. Due to their"
                        " determination and self motivation, they won't let anything \nstand in their way of "
                        "accomplishing a goal. Their drive allows them to overcome any obstacle or challenge they "
                        "may encounter, and they have the desire to accomplish \ngreat things in their lifetime. "
                        "Their only need is to focus on what they want in order to achieve it. \n \n"

                        "Innovation and creativity also are characteristics associated with this path. These folks"
                        " are very good at starting new projects, and often take a unique\n or inventive approach "
                        "to solving problems. Because of these qualities, and because multitasking is something they"
                        " tend to be very good at, they are well suited to self employment\n and can be happiest "
                        "being their own boss. A Life Path of One also means that they may possess the qualities "
                        "to be a political or military leader.\n\n"
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)  # displays the text

        elif sums == 2:
            Label(root, image=self.photo2).place(x=0, y=0, relwidth=0.25, relheight=0.4)        # displays the image
            Label(root,
                  text=("A person with Life Path number 2 seeks harmony and peace, and is symbolized by relationships,"
                        " co-operation, and being considerate and thoughtful of others. \nPeople with a Life Path 2 "
                        "are natural peacemakers, and because they see all the viewpoints in any situation, handle"
                        " difficult situations with grace, and tend to be persuasive rather \nthan forceful when "
                        "trying to get their point across, people may often look to them to be a mediator in any "
                        "argument.\n\n"

                        "If your Life Path number is 2, your sensitivity can also in some ways be your downfall."
                        " Many people with a Life Path of 2 are oversensitive, shy, and afraid to speak their minds.\n"
                        " Because you are afraid of being hurt you may avoid confrontation and hold back your opinions."
                        " This can cause you to have trouble contributing to a group, and may make you feel resentful"
                        " \nbecause you are withholding your ideas and contributions. You compassion and caring for "
                        "other people also may cause you to deny your own needs in favor of the needs of others, \n"
                        "which can also lead to feelings of resentment or anger, and if you feel threatened or pushed"
                        " to the wall, you can become the terrible Twos, however, ultimately you do not want conflict."
                        "\n\n"

                        "Life path number 2 is a vibration of duality and division, the number of truth and learning."
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)                  # displays the text
        elif sums == 3:
            Label(root, image=self.photo3).place(x=0, y=0, relwidth=0.25, relheight=0.4)        # displays the image
            Label(root,
                  text=("People with a Life Path number 3 have a very high level of creativity and self expression. "
                        "This abundance of creative energy, and the ease with which they are able to communicate in\n"
                        " all areas, both written word and verbal, could lead them to become a poet, actor, writer,"
                        " artist or musician. In fact many writers, radio broadcasters, actors, singers, performers,\n"
                        " and counselors share this life path number.\n\n"

                        "Threes are optimistic, extremely generous and giving souls, and are able to find positive in"
                        " everything around them. People like to be around them, not only because of these qualities,\n"
                        " but also because Threes have a charismatic personality, are great listeners and are very"
                        " conscious of other people's feelings and emotions. They can easily put the people around \n"
                        "them at ease and make them feel comfortable.\n\n"

                        "When they are hurt emotionally, Threes tend to withdraw and become moody, and can sometimes"
                        " make biting comments to lash out at people around them. They can be manic depressive if \n"
                        "they do not use their creative energy and tend to exaggerate the truth.\n\n"

                        "Life path number 3 is a strong vibration, one of creative self expression, independence, "
                        "playfulness, and communication."""
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)           # displays the text
        elif sums == 4:
            Label(root, image=self.photo4).place(x=0, y=0, relwidth=0.25, relheight=0.4)        # displays the image
            Label(root,
                  text=("People with a Life Path number 4 are the worker bees of society. If your Life Path is a 4 "
                        "you are determined, practical and hard working. Down-to-earth is a term that is probably \n"
                        "often used to describe you. You find hard work rewarding and don't look for the easy way to "
                        "the top or to finding success. Not only do you work hard yourself, but you expect the same "
                        "from those around you.\n\n"

                        "The Fours like to be organized, and to put things back in their \" proper place\" … it is"
                        " one of their strong points, and they feel better able to tackle challenges if they have\n "
                        "a solid plan in place beforehand. They tend to be set in their ways and are drawn to leading "
                        "an orderly life ie. \"a place for everything and everything in its place.\" Home is their \n"
                        " haven, and if their home environment appears sloppy and unkempt, that is a sign that a Life "
                        "Path 4 person is not doing well.\n\n"

                        "They are usually very cerebral and need to find ways to relax their minds. Otherwise, great"
                        " ideas live and die in their heads. They have a strong sense of right and wrong, are very \n"
                        "honest, and value honesty in others. Fours' dreams are based in reality and they never"
                        " question that you will have to work hard to make them come true. Loyal and very dependable,\n"
                        " they make an excellent friend or partner, but may have just a small circle of friends.\n\n"

                        "Life path number 4 is about putting all the pieces together, it is a builder number. You are "
                        "grounded, serious, hardworking, analytical, practical and disciplined."
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)       # displays the text

        elif sums == 5:
            Label(root, image=self.photo5).place(x=0, y=0, relwidth=0.25, relheight=0.4)    # displays the image
            Label(root,
                  text=(
                      "Those with a Life Path of 5 seek freedom above all else. They are adventurers, having a "
                      "restless nature, and being on the go, constantly seeking change and variety in life. They have\n"
                      " a free spirit and need to have variety in their day. If they do not live the adventure, their"
                      " lives become way too dramatic.\n\n"

                      "They love meeting new people, trying new things, and living life for today, and curiosity leads"
                      " them to constantly try to find the answers to life's questions. \"Conservative\" is a word \n"
                      "that is probably never used to describe them, as they love taking risks, and hate routine and "
                      "repetition.\n\n"

                      "Fives are very persuasive and excel at motivating people which makes them ideal candidates to "
                      "become salesmen. Any career requiring travel is also a great fit for those with Life Path number"
                      " 5, \nsince it will keep them away from the routine of many other jobs, otherwise they may feel"
                      " a sense of restlessness if they get stuck in a mundane or repetitive job environment. Fives \n"
                      "are also very versatile, which makes many other career choices suitable for them. A person with"
                      " a lot of 5's in their chart will want to be their own boss. This person will not enjoy \n"
                      "working a 9 to 5 job where they have to report to someone else each day.\n\n"
                      "\n\n")).place(x=200, y=500, relwidth=0.8, relheight=0.25)        # displays the text

        elif sums == 6:
            Label(root, image=self.photo6).place(x=0, y=0, relwidth=0.25, relheight=0.4)        # displays the image
            Label(root,
                  text=("Those born with a Life Path number 6 are incredible nurturers. If men, they rescue damsels in"
                        "distress. If women, they mother the \"little boy\" in their men.\n\n"

                        "If you have a six in your chart you are home, family, or community oriented, loving, warm, "
                        "understanding, compassionate, responsible and reliable and interested in pleasing others.\n"
                        " You are an excellent caretaker and provider, and enjoy being of service to others, and this"
                        " is especially true with your family and friends. You life revolves around home and family,\n"
                        " and your parenting instincts are very strong. The word domestic most likely describes you "
                        "well, and one job you would love is being a stay at home parent.\n\n"

                        "As a Six you should keep an eye on yourself as you may become self-righteous and critical of "
                        "others. Because you are so giving you might have a tendency to become a slave to others and\n"
                        " neglect your own needs in the process. Because you thrive on supporting others you may "
                        "sometimes find it difficult to find a balance between helping and meddling. You may also\n"
                        " become an enabler for someone who needs taking care of in a relationship, or with a child,"
                        " and not allow them to experience life or learn its lessons. People born on the Sixth path\n"
                        " are often described as magnetic, as people are often drawn to them, and their moods can "
                        "affect the room.\n\n"

                        "Life path number 6 is the number of responsibility and awareness. When those around you are"
                        " losing their heads, you're the one who takes charge. Stop fighting it. \n\n"
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)  # displays the text

        elif sums == 7:
            Label(root, image=self.photo7).place(x=0, y=0, relwidth=0.25, relheight=0.4)    # displays the image
            Label(root,
                  text=("Seven is another cerebral number, and those with a Life Path number 7 have a loner quality."
                        " They need to learn to have faith. If they do not have faith they tend to become very \n"
                        "cynical and escape through drugs, alcohol, work, and geography. They have a love of natural "
                        "beauty: ocean, green grass, plants, flowers, etc. . . \n\n"

                        "Sevens have an air of mystery and do not want you to know who they are. Intellectual, "
                        "analytical, intuitive, reserved, natural inclination towards spiritual subjects, aloof, \n"
                        "loner, pessimistic, secretive, and insecure; are some of the qualities of those born into "
                        "the Seventh Life path. A person who is a Life Path 7 is a thinker. If your Life Path is a 7 "
                        "\nyou are wise and studious. You seek truth and wisdom in all that you do, and search for "
                        "the underlying answers in everything. Your tendency is to be a perfectionist, and you \n"
                        "expect the same from those around you.\n\n"

                        "Your love of solitude can make it difficult for you to form close relationships. While you "
                        "value your independence you may often feel lonely or isolated because you lack closeness \n"
                        "with others. Because you spend so much time alone, you may lose your consideration for others"
                        " and become inflexible. One of the challenges for you is to find a balance between \n"
                        "maintaining your solitude while not becoming completely isolated. Seven represents spiritual"
                        " focus, analysis, being original, independent; If you have this number people often feel \n"
                        "like they don't know you; you are a mystery, and some may see you as eccentric. \n\n"
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)       # displays the text
        elif sums == 8:
            Label(root, image=self.photo8).place(x=0, y=0, relwidth=0.25, relheight=0.4)        # displays the image
            Label(root,
                  text=("People with a Life Path number 8 do not feel safe unless they have found a way to establish "
                        "financial security.\n\n"

                        "It is difficult for an Eight to take advice. When they make a choice, they must feel it is"
                        " their decision, NOT SOMEONE ELSES. As a result, they do tend to learn the hard way. \n"
                        "Eights are very honest and by being so blunt, they unintentionally hurt feelings. Although"
                        " they can sometimes appear insensitive, what is going on inside them is the exact opposite.\n"
                        " They do feel deeply about everything that goes on in their lives. People with a Life Path 8 "
                        "are born with natural leadership skills. If your Life Path is an 8 you are very ambitious \n"
                        "and goal oriented. You have strong organizational skills and broad vision which make you "
                        "successful in business.\n\n"

                        "Because you consider status very important you may be tempted to live above your means. You "
                        "should also pay special attention to telling and showing your loved ones that you care - being"
                        "\n a good provider isn't the only way of doing this.\n\n"
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)              # displays the text

        elif sums == 9:
            Label(root, image=self.photo9).place(x=0, y=0, relwidth=0.25, relheight=0.4)        # displays the image
            Label(root,
                  text=("Those born with a Life Path number 9 are natural leaders, and they assume they are in charge "
                        "even if they are not. If in a department store, people think they work there. They take care\n"
                        " of everyone else but need to learn to speak up when they need help, love, and hugs. Nines "
                        "often feel unloved or abandoned by their mother or father, or they feel completely responsible"
                        "\n for them. It's hard for them to let go of the past. \n\n"

                        "You are friendly and people like you. Your generosity knows no bounds, and you give freely "
                        "of your money, time and energy. Your ultimate goal is working toward a better world.\n\n"

                        "Number 9 symbolizes endings, spiritual consciousness. An individual with a Life Path number 9"
                        " can overcome a lot, and is often required to do so in their lifetime. If you have a Life "
                        "Path Number 9 \nyou most likely had a difficult relationship with one or both of your parents"
                        " early in your life.\n\n"
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)        # displays the text

        elif sums == 11:
            Label(root, image=self.photo11).place(x=0, y=0, relwidth=0.25, relheight=0.4)       # displays the image
            Label(root,
                  text=("Individuals with the Life Path number 11 are very intuitive, in fact it is the most intuitive"
                        " of all numbers. They are sensitive and have a great understanding of others, and can sense a"
                        " \ngreat deal about what is going on behind the scenes. For example, they will pick up on "
                        "people's relationships and health without being told anything. They are here to use their "
                        "gifts of intuition, and sensitivity to help others. \n\n"

                        "The challenge for Elevens is to not be overwhelmed by their gifts. Fears and phobias "
                        "would be the downside of this number. They may also seem at times indecisive, impractical, "
                        "nervous, and moody.\n\n"

                        "The number 11 life path is concerned with spiritual illumination. Often a number 11 will "
                        "have an instinctive understanding of metaphysical matters. Because Elevens are also Twos, ,\n"
                        " have the strength to finish what they start. 11 is also a good number for forming "
                        "partnerships … you work and play well with others. You are likely to marry young and be "
                        "\ncommitted and faithful for your entire life.\n\n"
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)     # displays the text

        elif sums == 22:
            Label(root, image=self.photo22).place(x=0, y=0, relwidth=0.25, relheight=0.4)   # displays the image
            Label(root,
                  text=("22 is considered the most powerful of all the numbers. Those with a Life Path number 22 have"
                        " great spiritual understanding, and ability to apply knowledge in a practical way and achieve"
                        " enormous success.\n\n"

                        "This is the number of the Master Builder and those with a 22 in their chart are able to turn"
                        " your dreams into a reality. You are a great visionary and have the intuitive insights of "
                        "the 11,\n combined with the practical nature of the 4, . If not practical, someone with this"
                        " number can waste their potential. This individuals' goals are outside of their personal \n"
                        "self as this person strives to serve the greater good of humanity.\n\n"

                        "It can take someone with this number well into their adulthood before they manifest their "
                        "dreams because they have to go through trials, and learning experiences before they mature \n"
                        "enough to incorporate their true calling in their life.\n\n"

                        "Those following Life Path of 22 are called master teachers, and as mentioned they are the most"
                        " powerful of the life path numbers, endowed with many powers, and a unique talent for "
                        "manifesting \nideas into the realm of reality. "
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)      # displays text
        elif sums == 33:
            Label(root, image=self.photo33).place(x=0, y=0, relwidth=0.25, relheight=0.4)  # displays the image
            Label(root,
                  text=("A birth date that reduces down to 33 is very rare. When it does happen you may be looking at "
                        "a great and significant spiritual leader along the lines of the Dalai Lama (Life Path 22) \n"
                        "or Gandhi (Life Path 9). Remember that a 33 is also a 6 life path, a very nurturing and "
                        "responsible number. \n\n"

                        "Life Path number 33 is signified by the word altruistic. This number has a high energy and is"
                        " concerned with doing good in the world.\n\n"

                        "Those with Life Path number 33 want to use their life to raise the consciousness of as many "
                        "people as possible. Their concern is the earth and all the people who live here. It's really\n"
                        " a beautiful life path number. As you may have guessed few have it. Below are some key points"
                        " you might want to take into consideration to help you on your path … "
                        )).place(x=200, y=500, relwidth=0.8, relheight=0.25)
root = Tk()
root.title("Life Path Number")              # this sets the title of the window to Life Path Number

name = MainLoopArea(root)

root.mainloop()

#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.

capitals = {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'LittleRock','California':'Sacramento','Colorado':'Denver','Connecticut':'Hartford','Delaware':'Dover','Florida':'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu','Idaho':'Boise','Illinois':'Springfield','Indiana':'Indianapolis','Iowa':'DesMoines','Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':'BatonRouge','Maine':'Augusta','Maryland':'Annapolis','Massachusetts':'Boston','Michigan':'Lansing','Minnesota':'SaintPaul','Mississippi':'Jackson','Missouri':'JeffersonCity','Montana':'Helena','Nebraska':'Lincoln','Nevada':'CarsonCity','NewHampshire':'Concord','NewJersey':'Trenton','NewMexico':'SantaFe','NewYork':'Albany','NorthCarolina':'Raleigh','NorthDakota':'Bismarck','Ohio':'Columbus','Oklahoma':'OklahomaCity','Oregon':'Salem','Pennsylvania':'Harrisburg','RhodeIsland':'Providence','SouthCarolina':'Columbia','SouthDakota':'Pierre','Tennessee':'Nashville','Texas':'Austin','Utah':'SaltLakeCity','Vermont':'Montpelier','Virginia':'Richmond','Washington':'Olympia','WestVirginia':'Charleston','Wisconsin':'Madison','Wyoming':'Cheyenne'}

# Generate 35 quiz files

for quizNum in range(35):
	# TODO: Create the quiz and answer key files.

    # TODO: Write out the header for the quiz.

    # TODO: Shuffle the order of the states.

    # TODO: Loop through all 50 states, making a question for each.

    # Create the quiz and answer key files.

    quizfile = open('capitalquiz%s.txt' %(quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz(Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.

    states = list(capitals.keys())
    random.shuffle(states)

    #TODO : Loop through all 50 states, making a queston for each.

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
    	#Get right and wrong answers.
    	correctAnswer = capitals[states[questionNum]]
    	wrongAnswer = list(capitals.values())
    	del wrongAnswers[wrongAnswers.index(correctAnswer)]
    	wrongAnswers = random.sample(wrongAnswers, 3)
    	answerOptions = wrongAnswers + [correctAnswer]
    	random.shuffle(answerOptions)

    	#TODO: write the question and answer options to the quiz file.

    	#TODO: Write the answer key to a file.

    	# Write the question and the answer options to the quiz file.

    	quizfile.write('%s. What is the capital of %s?\n' %(questionNum + 1, states[questionNum]))

    	for i in range(4):
    		quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
    		quizfile.write('\n')

    		#write the answer key to a file.
    		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()










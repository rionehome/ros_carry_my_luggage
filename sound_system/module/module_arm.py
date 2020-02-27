import os
from pocketsphinx import LiveSpeech, get_model_path

from . import module_pico
from . import module_beep

import datetime
from time import sleep

noise_words = []
file_path = os.path.abspath(__file__)

# pocketsphinx path
model_path = get_model_path()

# Define order path
yes_no_dic_path = file_path.replace(
    'module/module_arm.py', 'dictionary/yes_no.dict')
yes_no_gram_path = file_path.replace(
    'module/module_arm.py', 'dictionary/yes_no.gram')

# log file
result_path = file_path.replace(
    'module/module_arm.py', 'log/log.txt')

# Manipulate robot arm
def arm(when):
    ###############
    #
    # use this module at help me carry section
    #
    # param >> None
    #
    # return >> 1 | close robot hand
    #
    ###############

    global noise_words
    global live_speech

    if when == "first":
        start_sentence = "Please put your bag on my hand by 5 seconds."
        print("\n---------------------------------\n", start_sentence, "\n---------------------------------\n")
        module_pico.speak(start_sentence)
        file = open(result_path, 'a')
        file.write(str(datetime.datetime.now()) + ": " + start_sentence + "\n")
        file.close()
        sleep(5)

        while True:
            sentence = "Did you put your bag on my hand ?"
            print("\n---------------------------------\n", sentence, "\n---------------------------------\n")
            module_pico.speak(sentence)
            file = open(result_path, 'a')
            file.write(str(datetime.datetime.now()) + ": " + sentence + "\n")
            file.close()

            setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
            module_beep.beep("start")
            for question in live_speech:
                print("\n[*] CONFIRMING ...")
                # print(question)

                # Noise list
                noise_words = read_noise_word()

                if str(question) not in noise_words:
                    file = open(result_path, 'a')
                    file.write(str(datetime.datetime.now()) + ": " + str(question) + "\n")
                    file.close()

                    if str(question) == "yes":

                        pause()
                        module_beep.beep("stop")
                        answer = "Thank you. I will follow you soon."
                        print("\n---------------------------------\n", answer,
                              "\n---------------------------------\n")
                        module_pico.speak(answer)
                        file = open(result_path, 'a')
                        file.write(str(datetime.datetime.now()) + ": " + answer + "\n")
                        file.close()
                        return 1

                    elif str(question) == "no":

                        # Fail, listen one more time
                        pause()
                        module_beep.beep("stop")
                        answer = "Sorry."
                        print("\n---------------------------------\n", answer,
                              "\n---------------------------------\n")
                        module_pico.speak(answer)
                        file = open(result_path, 'a')
                        file.write(str(datetime.datetime.now()) + ": " + answer + "\n")
                        file.close()
                        setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                        noise_words = read_noise_word()
                        break

                    elif str(question) == "please say again":

                        pause()
                        module_beep.beep("stop")
                        # Ask yes-no question
                        setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                        noise_words = read_noise_word()
                        break

                # noise
                else:
                    print(".*._noise_.*.")
                    print("\n[*] CONFIRMING ...")
                    pass

    elif when == "end":
        end_sentence = "Please take your bag by 5 seconds."
        print("\n---------------------------------\n", end_sentence, "\n---------------------------------\n")
        module_pico.speak(end_sentence)
        file = open(result_path, 'a')
        file.write(str(datetime.datetime.now()) + ": " + end_sentence + "\n")
        file.close()
        sleep(5)

        while True:
            sentence = "Did you take your bag ?"
            print("\n---------------------------------\n", sentence, "\n---------------------------------\n")
            module_pico.speak(sentence)
            file = open(result_path, 'a')
            file.write(str(datetime.datetime.now()) + ": " + sentence + "\n")
            file.close()

            setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
            module_beep.beep("start")
            for question in live_speech:
                print("\n[*] CONFIRMING ...")
                # print(question)

                # Noise list
                noise_words = read_noise_word()

                if str(question) not in noise_words:
                    file = open(result_path, 'a')
                    file.write(str(datetime.datetime.now()) + ": " + str(question) + "\n")
                    file.close()

                    if str(question) == "yes":

                        pause()
                        module_beep.beep("stop")
                        answer = "Thank you."
                        print("\n---------------------------------\n", answer,
                              "\n---------------------------------\n")
                        module_pico.speak(answer)
                        file = open(result_path, 'a')
                        file.write(str(datetime.datetime.now()) + ": " + answer + "\n")
                        file.close()
                        return 1

                    elif str(question) == "no":

                        # Fail, listen one more time
                        pause()
                        module_beep.beep("stop")
                        answer = "Sorry."
                        print("\n---------------------------------\n", answer,
                              "\n---------------------------------\n")
                        module_pico.speak(answer)
                        file = open(result_path, 'a')
                        file.write(str(datetime.datetime.now()) + ": " + answer + "\n")
                        file.close()
                        setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                        noise_words = read_noise_word()
                        break

                    elif str(question) == "please say again":

                        pause()
                        module_beep.beep("stop")
                        # Ask yes-no question
                        setup_live_speech(False, yes_no_dic_path, yes_no_gram_path, 1e-10)
                        noise_words = read_noise_word()
                        break


# Stop lecognition
def pause():

    ###############
    #
    # use this module to stop live speech
    #
    # param >> None
    #
    # return >> None
    #
    ###############

    global live_speech
    live_speech = LiveSpeech(no_search=True)

# Make noise list
def read_noise_word():

    ###############
    #
    # use this module to put noise to list
    #
    # param >> None
    #
    # return >> words: list in noises
    #
    ###############

    words = []
    with open(yes_no_gram_path) as f:
        for line in f.readlines():
            if "<noise>" not in line:
                continue
            if "<rule>" in line:
                continue
            line = line.replace("<noise>", "").replace(
                    " = ", "").replace("\n", "").replace(";", "")
            words = line.split(" | ")
    return words

# Setup livespeech
def setup_live_speech(lm, dict_path, jsgf_path, kws_threshold):

    ###############
    #
    # use this module to set live espeech parameter
    #
    # param >> lm: False >> means useing own dict and gram
    # param >> dict_path: ~.dict file's path
    # param >> jsgf_path: ~.gram file's path
    # param >> kws_threshold: mean's confidence (1e-○)
    #
    # return >> None
    #
    ###############

    global live_speech
    live_speech = LiveSpeech(lm=lm,
                             hmm=os.path.join(model_path, 'en-us'),
                             dic=dict_path,
                             jsgf=jsgf_path,
                             kws_threshold=kws_threshold)

if __name__ == '__main__':
    arm()

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
follow_dic_path = file_path.replace(
    'module/module_follow.py', 'dictionary/follow_me.dict')
follow_gram_path = file_path.replace(
    'module/module_follow.py', 'dictionary/follow_me.gram')

# log file
result_path = file_path.replace(
    'module/module_follow.py', 'log/log.txt')

# Listen, follow me otr stop following me
def follow():
    ###############
    #
    # use this module at help me carry section
    #
    # param >> (first or end): when will you use at help me carry section
    #
    # return >> 1 | start follow me
    #          car| stop following me, and send this place, car
    #
    ###############

    global noise_words
    global live_speech

    # Start following me and stop
    sleep(2)
    stop_sentence = "I am following you. Please stay in my sight, and say stop following me when you arrived. "
    print("\n---------------------------------\n", stop_sentence, "\n---------------------------------\n")
    module_pico.speak(stop_sentence)
    file = open(result_path, 'a')
    file.write(str(datetime.datetime.now()) + ": " + stop_sentence + "\n")
    file.close()

    setup_live_speech(False, follow_dic_path, follow_gram_path, 1e-10)
    module_beep.beep("start")
    for question2 in live_speech:
        print("\n[*] PREASE SAY STOP FOLLOWING ME ...")
        # print(question2)

        # Noise list
        noise_words = read_noise_word(follow_gram_path)
        if str(question2) == "":
            pass
        elif str(question2) not in noise_words:
            if str(question2) == "stop following me":
                file = open(result_path, 'a')
                file.write(str(datetime.datetime.now()) + ": " + str(question2) + "\n")
                file.close()
                pause()
                module_beep.beep("stop")
                #print("\n---------------------------------\n", str(question2), "\n---------------------------------\n")

                # Detect yes (or stop following me) or no
                flag = True
                while flag:
                    print("\n---------------------------------\n", str(question2), "\n---------------------------------\n")
                    sentence = "Do you want me to stop following you ?"
                    print("\n---------------------------------\n", sentence, "\n---------------------------------\n")
                    file = open(result_path, 'a')
                    file.write(str(datetime.datetime.now()) + ": " + sentence + "\n")
                    file.close()
                    pause()
                    module_pico.speak(sentence)

                    setup_live_speech(False, follow_dic_path, follow_gram_path, 1e-10)
                    module_beep.beep("start")
                    for question3 in live_speech:
                        print("\n[*] CONFIRMING ...")
                        # print(question3)

                        # Noise list
                        noise_words = read_noise_word(follow_gram_path)

                        if str(question3) not in noise_words:
                            file = open(result_path, 'a')
                            file.write(str(datetime.datetime.now()) + ": " + str(question3) + "\n")
                            file.close()

                            if str(question3) == "yes" or str(question3) == "stop following me":

                                # Stop following me
                                pause()
                                module_beep.beep("stop")
                                answer = "Sure, I will stop following you."
                                print("\n---------------------------------\n", answer,
                                      "\n---------------------------------\n")
                                module_pico.speak(answer)
                                file = open(result_path, 'a')
                                file.write(str(datetime.datetime.now()) + ": " + answer + "\n")
                                file.close()

                                return 1

                            elif str(question3) == "no":

                                # Fail, listen one more time
                                pause()
                                module_beep.beep("stop")
                                answer = "Sorry, let me know if you want to stop."
                                print("\n---------------------------------\n", answer,
                                      "\n---------------------------------\n")
                                module_pico.speak(answer)
                                file = open(result_path, 'a')
                                file.write(str(datetime.datetime.now()) + ": " + answer + "\n")
                                file.close()

                                setup_live_speech(False, follow_dic_path, follow_gram_path, 1e-10)
                                noise_words = read_noise_word(follow_gram_path)
                                flag = False
                                break


                            elif str(question3) == "please say again":

                                pause()
                                module_beep.beep("stop")
                                # Ask yes-no question
                                setup_live_speech(False, follow_dic_path, follow_gram_path, 1e-10)
                                noise_words = read_noise_word(follow_gram_path)
                                break

                        # noise
                        else:
                            print(".*._noise_.*.")
                            print("\n[*] CONFIRMING ...")
                            pass
        # noise
        else:
            print(".*._noise_.*.")
            print("\n[*] PREASE SAY STOP FOLLOWING ME ...")
            pass

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
def read_noise_word(gram_path):

    ###############
    #
    # use this module to put noise to list
    #
    # param >> gram_path: grammer's path which you want to read noises
    #
    # return >> words: list in noises
    #
    ###############

    words = []
    with open(gram_path) as f:
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
    follow()

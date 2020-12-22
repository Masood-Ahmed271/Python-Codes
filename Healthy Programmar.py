from pygame import mixer
import datetime,  time

#Gets the now datetime
def getdatetime():
    return datetime.datetime.now()
#A function for playing music
def musicrunner(file,stopper,volume, msg):
    mixer.init() #initalize the music
    mixer.music.load(file)  #loads the song/music
    mixer.music.set_volume(volume)  #sets volume of the music
    mixer.music.play()  #plays the music
    print(msg)
    user_input = input()
    while True:
        if user_input.lower() == stopper:
            mixer.music.stop()  #stops the music
            return
#a function to enter data
def log_data(msg):
    with open('Mydata.txt', 'a') as f:  #appends information in the file
        f.write(f'{msg} [{getdatetime()}\n')
    return
#main function
if __name__ == '__main__':
    start = float(input('Input starting hour using 24 hours clock .i.e. 11 for 11:00 am\n'))
    end = float(input('Input ending hour using 24 hours clock .i.e. 14 for 02:00 pm\n'))
    amount_of_water = float(input('How much amount of water(liters) do you want to drink during your time duration.\n'))
    times_water_to_bedrunk = (amount_of_water*1000)/200
    duration = end - start
    duration_of_water = ((duration*3600) // times_water_to_bedrunk)
    init_exercise = float(input('After how  many minutes do you want to do physical exercise?\n'))
    duration_of_exercise = init_exercise * 60
    init_eyes = float(input('After how many minutes do you want to exercise your eyes?\n'))
    duration_of_eyes_exercise = init_eyes*60
    vol = float(input('What should be the volume of the alarm?\n'))
    initial_water = time.time()
    initial_exercise = time.time()
    initial_eyes = time.time()
    finaltime = time.time()
    while True:
        if time.time() - finaltime == duration:
            break

        if time.time()-initial_eyes> duration_of_eyes_exercise:
            msg = 'Time to exercise your eyes! Type Eydone when exercise is done.'
            musicrunner('Eyes.ogg', 'eydone', vol, msg)
            msg2 = 'Eye exercise done at:'
            log_data(msg2)
            initial_eyes = time.time()

        if time.time()-initial_exercise > duration_of_exercise:
            msg = 'Time to do physical exercise! type Exdone when exercise is done.'
            musicrunner('Exercise.ogg', 'exdone', vol, msg)
            msg2 = 'Physical exercise done at:'
            log_data(msg2)
            initial_exercise = time.time()

        if time.time() - initial_water >duration_of_water:
            msg = 'Time to drink water! Input Drank when exercise is done.'
            musicrunner('Water.ogg', 'drank', vol, msg)
            msg2 = 'Water drank at:'
            log_data(msg2)
            initial_water = time.time()
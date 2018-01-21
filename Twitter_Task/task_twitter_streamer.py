from twython import Twython, TwythonStreamer

C_K = ""
C_S = ""
A_T = ""
A_S = ""

i = 0

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        global i
        if 'text' in data:
            i = i+1
            s = "Found it" + str(i) + " times, this one being: " +data['text']
            print(s)
        if(i==3):
            print("Ian G. Harris is popular!")
            
stream = MyStreamer(C_K, C_S, A_T, A_S)
stream.statuses.filter(track="Ian G. Harris")

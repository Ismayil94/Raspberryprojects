from twython import Twython, TwythonStreamer

C_KEY =""
C_SECRET =""
A_TOKEN =""
A_SECRET =""

api = Twython(C_KEY, C_SECRET,A_TOKEN,A_SECRET)

api.update_status("Some text")
import touchio
import board
import time
from adafruit_circuitplayground.express import cpx

bpm = 120 #beats per minute for sustained hold, change this to suit your tempo

# make the input cap sense pads
capPins = (board.A1, board.A2, board.A3, board.A4, board.A5,
           board.A6, board.A7)

touchPad = []
for i in range(7):
    touchPad.append(touchio.TouchIn(capPins[i]))

# The seven files assigned to the touchpads
audiofiles = ["bd_tek.wav", "elec_hi_snare.wav", "elec_cymbal.wav",
               "elec_blip2.wav", "bd_zome.wav", "bass_hit_c.wav",
               "drum_cowbell.wav"]

def play_file(filename):
    print("playing file "+filename)
    cpx.play_file(filename)
    time.sleep(bpm/960) #sixteenthNote delay

while True:

    for i in range(7):
        if touchPad[i].value:
            play_file(audiofiles[i])
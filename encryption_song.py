
import wave

song = wave.open("C:/Users/MBajw/Downloads/Nursery_songs.wav", mode='rb')
frame_bytes = bytearray(list(song.readframes(song.getnframes())))
string =input ("Enter your Message ")

string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
frame_modified = bytes(frame_bytes)


with wave.open('C:/Users/MBajw/Downloads/Nursery_songs.wav', 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()

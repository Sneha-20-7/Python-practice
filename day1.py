# Author : Sneha sarkar
''' Author : Sneha 
importing os module '''
import os
print("Hello world")


#practice set 1
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star. ''')


#practice set 2


#practice set 3
'''from playsound import playsound
playsound('C:\\Users\\SNEHA\Downloads\\ppt\\In Dino - Life In A Metro 128 Kbps.mp3 \\play.mp3')'''

#or
from pydub import AudioSegment
from pydub.playback import play

# Manually set FFmpeg path if needed
import os
os.environ["PATH"] += os.pathsep + "C:/path_to_ffmpeg/bin"

# Load and play audio
sound = AudioSegment.from_file("your_audio_file.mp3")
play(sound)



#ps3
import os
print(os.listdir())


#ps4
# hi
# hello
# bye bye


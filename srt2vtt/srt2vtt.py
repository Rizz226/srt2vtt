from webvtt import WebVTT
import sys
'''
Many components of Glut23's WebVTT-py (https://github.com/glut23/webvtt-py) are included in this module. All the heavy lifing was done by them.
Seriously, I'll likely just end up making a pull request with these couple CLI options for folks who dont really know how to use the interpreter.
'''


def main(inputF):
    vtt = WebVTT.from_srt(inputF)
    vtt.save()
    exit()

    
if __name__ == '__main__':
    inputF = sys.argv[1]
    main(inputF)
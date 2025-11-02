import sys
import os

# Get the path to the directory *above* 'tests' (your project root)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add that root directory to Python's path
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import liberte.parser

def test_finds_new_messages():
    HTML = '''<a title="Liczba nieprzeczytanych wiadomości: 2" href="/wiadomosci" id="icon-wiadomosci"><span class="circle"></span>Wiadomości<a class="button counter">2         </a></a>                    '''
    assert liberte.parser.has_new_messages(HTML) == True

# def test_not_find_new_messages():
    # assert liberte.parser.has_new_messages('') == False  

def test_finds_new_announcements():
    HTML = '''<a title="Liczba nieprzeczytanych ogłoszeń: 1" href="/ogloszenia" id="icon-ogloszenia"><span class="circle"></span>Ogłoszenia</a>                    <a class="button counter">1         </a>'''
    assert liberte.parser.has_new_messages('') == True           

# def test_not_find_new_announcements():
    # assert liberte.parser.has_new_messages('') == False  
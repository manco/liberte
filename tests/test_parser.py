import sys
import os

# Get the path to the directory *above* 'tests' (your project root)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add that root directory to Python's path
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from liberte.parser import Parser

def test_finds_new_messages():
    HTML = '''<a title="Liczba nieprzeczytanych wiadomości: 2" href="/wiadomosci" id="icon-wiadomosci"><span class="circle"></span>Wiadomości<a class="button counter">2         </a></a>                    '''
    assert Parser(HTML).has_new_messages() == True

def test_not_find_new_messages():
    assert Parser('').has_new_messages() == False

def test_finds_new_announcements():
    HTML = '''<a title="Liczba nieprzeczytanych ogłoszeń: 1" href="/ogloszenia" id="icon-ogloszenia"><span class="circle"></span>Ogłoszenia</a>                    <a class="button counter">1         </a>'''
    assert Parser(HTML).has_new_announcements() == True

def test_not_find_new_announcements():
    assert Parser('').has_new_messages() == False

def test_find_new_announcements_and_messages_in_real_html():
    with open('tests/site-with-notifications.html', 'r') as file:
        parser = Parser(file.read())
        assert parser.has_new_messages() == True
        assert parser.has_new_announcements() == True


def test_not_find_new_announcements_and_messages_in_real_html():
    with open('tests/site-no-notifications.html', 'r') as file:
        parser = Parser(file.read())
        assert parser.has_new_messages() == False
        assert parser.has_new_announcements() == False
 
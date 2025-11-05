from bs4 import BeautifulSoup, Tag
from bs4.element import AttributeValueList
from pymonad.maybe import Maybe
from pymonad.maybe import Nothing
from pymonad.maybe import Just
import re

from typing import Optional, TypeVar

class Parser:
   def __init__(self, input_html: str):
      self.soup = BeautifulSoup(input_html, 'html.parser')
      self.messages_title_pattern: re.Pattern[str] = re.compile("^Liczba nieprzeczytanych wiadomości:\\s*\\d+$")
      self.announcements_title_pattern: re.Pattern[str] = re.compile("^Liczba nieprzeczytanych ogłoszeń:\\s*\\d+$")

   def has_new_messages(self) -> bool:
      return self.__find_anchor_match_title('icon-wiadomosci', self.messages_title_pattern)

   def has_new_announcements(self) -> bool:
      return self.__find_anchor_match_title('icon-ogloszenia', self.announcements_title_pattern)

   def __find_anchor_match_title(self, anchor_id: str, title_regex: re.Pattern[str]) -> bool:
      return (
         Parser
         .__option(self.soup.find('a', id=anchor_id))
         .bind(lambda a:Parser.__option(a.get('title'))) # type: ignore[arg-type] pylance is stoopid
         .bind(lambda t:Parser.__option(title_regex.search(t))) # type: ignore[arg-type] pylance is stoopid
         .is_just()
      )

   T = TypeVar('T')
   @staticmethod
   def __option(x: Optional[T]) -> Maybe[T]:
      if not x:
         return Nothing
      else:
         return Just(x)


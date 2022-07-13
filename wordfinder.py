"""Word Finder: finds random words from a dictionary."""

import random 

class WordFinder:
    '''Machine for finding random words in a dictionary

    >>> wf = WordFinder("file path")
    3 word read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    '''

    def __init__(self, path):
        '''Read dicitionary and reports number of items read.'''

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        '''Parse dict_file -> list of words'''

        return [w.strip() for w in dict_file]

    def random(self):
        '''Return random word.'''

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
      '''Specialized WordFinder that excludes blank lines and comments.

      >>> swf = SpecialWordFinder("file path")
      3 words read

      >>> swf.random() in ["pear", "carrot", "kale"]
      True
      '''

      def parse(self, dict_file):
          '''Parse dict_file -> list of words, skipping blanks/comments.'''

          return [w.strip() for w in dict_file
                  if w.strip() and not w.startswith("#")]





    


from section import *

class Pattern:
    def __init__(self, title, sections):
        if type(title) is not str:
            raise Exception('Title must be a string.')
        if type(sections) is not list:
            raise Exception('Patterns must be a list.')
        if len(sections) == 0:
            raise Exception('Components must not be empty.')
        for section in sections:
            if section.__class__ is not Section:
                raise Exception('Each component of a pattern must be a Section.')
        self.title = title
        self.sections = sections
    
    def __str__(self):
        return '<pattern>\n<title>' + self.title + '</title>\n' + '\n'.join([section.__str__() for section in self.sections]) + '\n</pattern>'

    def __eq__(self, other):
        if other.__class__ is not Pattern:
            return False
        if len(self.sections) != len(other.sections):
            return False
        return reduce(lambda x, y: x and y, [self.sections[i] == other.sections[i] for i in range(len(self.sections))])

'''
pattern := section[]
section := (annotation|row)[]
row := (annotation|stitch)[]

'''
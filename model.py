import re


class Model:
    def __init__(self, email):
        self.email = email
        self.retrieved_email = ""

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        '''Validates email before setting the value'''
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        '''Writes/ saves the email into a file'''
        with open('email.txt', 'a') as f:
            f.write(f'{self.email}\n')

    def retrieve(self):
        '''Reads the email from a file'''
        with open('email.txt', 'r') as f:
            self.retrieved_email = f.readline().strip()

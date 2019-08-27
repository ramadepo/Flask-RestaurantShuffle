import re

class Formater():
    @staticmethod
    def is_email(source):
        pattern = r'[A-Za-z0-9\.]{1,48}@[A-Za-z0-9\.]{1,48}'
        return re.fullmatch(pattern, source)

if __name__ == '__main__':
    print(Formater.is_email('asdfa@asdf.com'))
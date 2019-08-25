import random
import hashlib


class Hasher():
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    @classmethod
    def hash(cls, length):
        result = ''.join(random.choice(cls.charset) for _ in range(length))
        return result

    @classmethod
    def sha256(cls, input):
        return hashlib.sha256(input.encode()).hexdigest()

    @classmethod
    def generate_certification(cls, account_id):
        source = 'account_id_' + account_id
        result = cls.sha256(source)
        return result


if __name__ == '__main__':
    h = Hasher.hash(6)
    print(h)

    s = Hasher.sha256('123')
    print(s)

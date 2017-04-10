class Question:
    def __init__(self, question="", a="", b="", c="", d="", correct_ans="", user_ans=""):
        self.__question = question
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__correct_ans = correct_ans
        self.__user_ans = user_ans

    def set_question(self, question):
        self.__question = question

    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b

    def set_c(self, c):
        self.__c = c

    def set_d(self, d):
        self.__d = d

    def set_correct_ans(self, correct_ans):
        self.__correct_ans = correct_ans

    def set_user_ans(self, user_ans):
        self.__user_ans = user_ans

    def get_question(self):
        return self.__question

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_correct_ans(self):
        return self.__correct_ans

    def get_user_ans(self):
        return self.__user_ans

    def __str__(self):
        return str(self.__question) + \
               "\n" + str(self.__a) + \
               "\n" + str(self.__b) + \
               "\n" + str(self.__c) + \
               "\n" + str(self.__d)

import re

class Check:
    def check_password(password):
        if len(password) >= 8 and ("*" in password or "@" in password or "!" in password or "?" in password) and (re.match("^.*[A-Z].*$" , password) != None):
            return 1
        else:
            return 0

    def check_username(email):
        if re.match("^[a-zA-Z0-9\_\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$" , email) != None:
            return 1
        else:
            return 0


class Session:
    def __init__(self , user):
        self.user = user

    def add_poll(self , title : str , number_of_options : int , options : list[(str , int)] , user : User):
        self.user.polls.append(Poll(title , number_of_options , options , user , multi_poll))

    def active_or_dective_poll(self , id):
        if Poll.Polls[id].deleted == 0:
            if Poll.Polls[id].user == self.user:
                Poll.Polls[id].active_or_dective = not(Poll.Polls[id].active_or_dective)

    def del_poll(self , id):
        if Poll.Polls[id].deleted == 0:
            if Poll.Polls[id].user == self.user:
                self.user.polls[id].deleted = 1
    
    def show_result_of_poll(self , id):
        if Poll.Polls[id].deleted == 0:
            print(Poll.Polls[id].title)
            for option in Poll.polls[id].options:
                print(option[0] + " --> " + str(option[1]))

    def show_my_polls(self):
        for poll in self.user.polls:
            if Poll.Polls[id].deleted == 0:
                print(poll.title)

    def show_all_polls(self):
        for poll in Poll.Polls:
            if Poll.Polls[id].deleted == 0:
                print(poll.title)

    def participate_in_poll(self , id , option):
        if Poll.Polls[id].deleted == 0:
            Poll.Polls[id].options[option][1] += 1
            Poll.Polls[id].users.append(self.user)


class User:
    Users : list['User'] = []

    def __init__(self , email , password):
        self.email = email
        self.password = password
        self.polls = []

    def get_session(self , email , password):
        if email == self.email and password == self.password:
            return Session(self)


class Poll:
    Polls : list['Poll'] = []

    def __init__(self , title : str , number_of_options : int , options : list[(str , int)] , user : User , multi_poll : bool):
        self.title = title
        self.user = user
        self.number_of_options = number_of_options
        self.options = options
        self.id = len(Poll.Polls)
        self.users = []
        self.multi_poll = multi_poll
        self.active_or_dective = 1
        self.deleted = 0
        Poll.Polls.append(self)
import re

class Check:
    def check_password(password):
        if len(password) >= 8 and ("*" in password or "@" in password or "!" in password or "?" in password) and (re.match("^.*[A-Z].*$" , password) != None):
            return 1
        else:
            return 0

    def check_email(email):
        if re.match("^[a-zA-Z0-9\_\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$" , email) != None:
            return 1
        else:
            return 0


class Session:
    def __init__(self , user):
        self.user = user

    def add_poll(self , title : str , number_of_options : int , options : list[(str , int)]):
        self.user.polls.append(Poll(title , number_of_options , options , self.user))

    def active_or_dective_poll(self , id):
        if Poll.Polls[id].deleted == 0 and Poll.Polls[id].user == self.user:
            if Poll.Polls[id].active_or_dective == 1:
                Poll.Polls[id].active_or_dective = 0
                print("Deactivated!")
            else:
                Poll.Polls[id].active_or_dective = 1
                print("Activated!")

        else:
            print("You cannot active or deactive this poll!")

    def del_poll(self , id):
        if Poll.Polls[id].deleted == 0 and Poll.Polls[id].user == self.user:
            self.user.polls[id].deleted = 1
            print("Deleted!")
        else:
            print("You cannot delete this poll!")
    
    def show_result_of_poll(self , id):
        if Poll.Polls[id].deleted == 0:
            print(Poll.Polls[id].title)
            for option in Poll.Polls[id].options:
                print(option[0] + " --> " + str(option[1]))

    def show_my_polls(self):
        for poll in self.user.polls:
            if Poll.Polls[id].deleted == 0 and poll.active_or_dective == 1:
                print(poll.title)

    def show_all_polls(self):
        for poll in Poll.Polls:
            if poll.deleted == 0 and poll.active_or_dective == 1:
                print(poll.title)

    def participate_in_poll(self , id , option):
        print(Poll.Polls[id].options[option][1])
        Poll.Polls[id].options[option][1] += 1
        Poll.Polls[id].users.append(self.user)
        print("Submitted!")


class User:
    Users : list['User'] = []

    def __init__(self , email , password):
        self.email = email
        self.password = password
        self.polls = []
        User.Users.append(self)

    def get_session(self , email , password):
        if email == self.email and password == self.password:
            return Session(self)


class Poll:
    Polls : list['Poll'] = []

    def __init__(self , title : str , number_of_options : int , options : list[[str , int]] , user : User):
        self.title = title
        self.user = user
        self.number_of_options = number_of_options
        self.options = options
        self.id = len(Poll.Polls)
        self.users = []
        self.active_or_dective = 1
        self.deleted = 0
        Poll.Polls.append(self)


class CLI:
    def load():
        pass

    def save():
        pass

    def load_account():
        print("1. Login")
        print("2. Signup")
        command = input("Enter a command : ")
        
        if command == "1":
            user_number = -1
            while True:
                email = input("Email : ")
                for user in User.Users:
                    if user.email == email:
                        user_number = User.Users.index(user)
                        break
                if user_number != -1:
                    break
                else:
                    print("Email isn't correct!")
            while True:
                password = input("Password : ")
                if User.Users[user_number].password == password:
                    print("Logged in successfully!")
                    CLI.run(User.Users[user_number].get_session(User.Users[user_number].get_session(User.Users[user_number].email , User.Users[user_number].password)))
                    return None

                print("Password isn't correct!")

        elif command == "2":
            email = None
            while True:
                email = input("Email : ")
                if Check.check_email(email) == 1:
                    break
                else:
                    print("Email is not correct!")
            
            password = None
            while True:
                password = input("Password : ")
                if Check.check_password(password) == 1:
                    repeat_password = input("Retype password : ")
                    if repeat_password == password:
                        user_tmp = User(email , password)
                        CLI.run(user_tmp.get_session(email , password))
                        return None
                    else:
                        print("Retyped password is not correct!")
                else:
                    print("Password is not strong!")
    
    def run(session : Session):
        while True:
            print("User : " + session.user.email)
            print("*** Please choose one of the following options:")
            print("1. Creat a new poll.")
            print("2. List of polls.")
            print("3. Participate in a poll.")
            print("4. Delete your poll.")
            print("5. Activate or deactivate your poll.")
            print("6. Poll results.")
            print("7. List of your polls.")
            print("8. Exit\n")

            command = input("Input a COMMAND : ")

            print()
            
            if command == "1":
                title = input("Title : ")
                options = []
                number_of_options = int(input("Number of options : "))
                for i in range(number_of_options):
                    new_option = input("Option " + str(i) + " : ")
                    options.append([new_option , 0])
                session.add_poll(title , number_of_options , options)
                print("Created!")

            elif command == "2":
                session.show_all_polls()

            elif command == "3":
                id = int(input("Enter poll id : "))

                if Poll.Polls[id].deleted == 0 and Poll.Polls[id].active_or_dective == 1 and self.user not in Poll.Polls[id].users: 
                    print(Poll.Polls[id].title)
                    for i in range(Poll.Polls[id].number_of_options):
                        print(str(i) + ". " + Poll.Polls[id].options[i][0])
                    vote = int(input("Your vote : "))
                    session.participate_in_poll(id , vote)
                
                else:
                    print("You cannot participate in this poll!")

            elif command == "4":
                id = int(input("Enter poll id : "))
                session.del_poll(id)

            elif command == "5":
                id = int(input("Enter poll id : "))
                session.active_or_dective_poll(id)

            elif command == "6":
                id = int(input("Enter poll id : "))
                session.show_result_of_poll(id)

            elif command == "7":
                session.show_all_polls()

            elif command == "8":
                return None
            
            print()


if __name__ == "__main__":
    CLI.load()
    CLI.load_account()
    CLI.save()

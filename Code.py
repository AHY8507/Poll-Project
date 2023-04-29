class Poll():
    Polls : list['Poll'] = []

    def __init__(self , title : str , number_of_options : int , options : list[str]):
        self.title = title
        self.number_of_options = number_of_options
        self.options = options
        self.id = len(Poll.Polls) + 1
        self.number_of_votes_for_options = [0 for i in range(self.number_of_options)]
        Poll.Polls.append(self)

class CLI:
    def load() -> None:
        with open("Polls.txt" , "r") as poll_file:
            for line in poll_file.readlines():
                ls = line.split(",")
                
                title = ls[0]
                
                options = []

                number_of_votes_for_options = []

                number_of_options = 0

                for i in range(1 , len(ls) - 1):
                    number_of_options += 1

                    tmp = ls[i].split("_")
                    options.append(tmp[0])
                    number_of_votes_for_options.append(int(tmp[1]))
                
                tmp = Poll(title , number_of_options , options)
                tmp.number_of_votes_for_options = number_of_votes_for_options


    def upload() -> None:
        with open("Polls.txt" , "w") as poll_file:
            for poll in Poll.Polls:
                poll_file.write(poll.title + ",")
                
                for i in range(len(poll.options)):
                    poll_file.write(poll.options[i] + "_" + str(poll.number_of_votes_for_options[i]) + ",")
                
                poll_file.write("\n")
                

    def run() -> None:
        while True:
            print("*** Please choose one of the following options:")
            print("1. Creat a new poll.")
            print("2. List of polls.")
            print("3. Participate in a poll.")
            print("4. Exit\n")
            
            command = input("Input a COMMAND : ")

            print()

            if command == "1":
                title = input("Title : ")
                number_of_options = int(input("Number of options : "))
                options = []
                for i in range(number_of_options):
                    new_option = input("Option " + str(i + 1) + " : ")
                    options.append(new_option)
                
                new_poll = Poll(title , number_of_options , options)
                
                print("Created!")

            elif command == "2":
                for poll in Poll.Polls:
                    print(str(poll.id) + ". " + poll.title)

            elif command == "3":
                id = int(input("Enter poll id : "))
                
                print(Poll.Polls[id - 1].title)

                for i in range(Poll.Polls[id - 1].number_of_options):
                    print(str(i + 1) + ". " + Poll.Polls[id - 1].options[i])

                vote = int(input("Your vote: "))

                Poll.Polls[id - 1].number_of_votes_for_options[vote - 1] += 1

                print("Submitted!")

            elif command == "4":
                return None
        
            print()      


if __name__ == "__main__":
    CLI.load()
    CLI.run()
    CLI.upload()

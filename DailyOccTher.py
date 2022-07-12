import datetime
import os
""" Charles Truscott Watters """
""" <Cook breakfast, Brush teeth for 3 minutes with timer, Take a 15 minute shower, Exercise (morning), Plan day, Cook lunch, Brush teeth 3 minutes (afternoon), Leisure time, Cook dinner, Check if need groceries, Tidy and organise home, Make bed and wash other bed sheets and pillow cases, Wash face and whole body (20 minute shower at night), Close down fort and prepare to sleep, Take 9mg paliperidone, Sleep 9hrs (check tomorrow), >
Press any key to continue . . . """

"""<Cook breakfast, Brush teeth for 3 minutes with timer, Take a 15 minute shower, Exercise (morning), Plan day, Cook lunch, Brush teeth 3 minutes (afternoon), Leisure time, Cook dinner, Check if need groceries, Tidy and organise home, Make bed and wash other bed sheets and pillow cases, Wash face and whole body (20 minute shower at night), Close down fort and prepare to sleep, Take 9mg paliperidone, Sleep 9hrs (check tomorrow), >
Did you: Cook breakfast?
Enter X for YES or a space for NO:
Did you: Brush teeth for 3 minutes with timer?
Enter X for YES or a space for NO: X
Did you: Take a 15 minute shower?
Enter X for YES or a space for NO: X
Did you: Exercise (morning)?
Enter X for YES or a space for NO:
Did you: Plan day?
Enter X for YES or a space for NO: X
Did you: Cook lunch?
Enter X for YES or a space for NO: z
Enter X or a space next time ...
{'Cook breakfast': 'Not done.', 'Brush teeth for 3 minutes with timer': 'Is done.', 'Take a 15 minute shower': 'Is done.', 'Exercise (morning)': 'Not done.', 'Plan day': 'Is done.'}
"""


class TenDayRoutine(object):
    pass

class DailyRoutine(object):
    def __init__(self, daily_action=[], is_it_done={}):
        self.daily_action = daily_action
        self.is_it_done = is_it_done
    def __str__(self):
        string_of_actions = "<"
        for x in self.daily_action:
            string_of_actions += x
            string_of_actions += ", "
        string_of_actions += ">"
        return string_of_actions
    def build_daily_actions(self):
        if not type(self.daily_action) == list:
            pass
        else:
            for action in self.daily_action:
                self.is_it_done[action] = str("Not done.")
    def set_daily_action_done(self, action, check):
        if check == str("X"):
            is_it_done[action] = str("Is done.")
        elif check == str(" "):
            is_it_done[action] = str("Not done.")
    def check_all_done(self):
        all_daily_done = False
        for x in is_it_done:
            if is_it_done[str(x)] == str("Is done"):
                all_daily_done = True
                continue
            else:
                all_daily_done = False
                break

        return all_daily_done

    def prompt_user_if_done(self):
        for x in self.daily_action:
            print("Did you: ", end='')
            print(str(x), end='')
            print("?", end='\n')
            answer = input("Enter X for YES or a space for NO: ")
            if answer == str("X"):
                self.is_it_done[str(x)] = "Is done."
            elif answer == str(" "):
                self.is_it_done[str(x)] = "Not done."
            else:
                print("Enter X or a space next time ...")
                break
    def return_checklist(self):
        return self.is_it_done


def main():
    daily_actions = ["Cook breakfast", "Brush teeth for 3 minutes with timer", "Take a 15 minute shower", "Exercise (morning)", "Plan day", "Cook lunch", "Brush teeth 3 minutes (afternoon)", "Leisure time", "Cook dinner", "Check if need groceries", "Tidy and organise home", "Make bed and wash other bed sheets and pillow cases", "Wash face and whole body (20 minute shower at night)", "Close down fort and prepare to sleep", "Take 9mg paliperidone", "Sleep 9hrs (check tomorrow)"]
    today = DailyRoutine(daily_actions)
    print(today)
    today.prompt_user_if_done()
    print(today.return_checklist())
    fh = open('./{}_ROUTINE.txt'.format(datetime.date.today()), 'w+')
    fh.write(str(today.return_checklist()))
    fh.write("\n\n")
    fh.write("{}".format(str(datetime.date.today())))
    fh.close()
if __name__ == "__main__": main()

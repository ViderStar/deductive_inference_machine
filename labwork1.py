class Rule:
    def __init__(self, if_clause, then_clause):
        self.if_clause = if_clause
        self.then_clause = then_clause


class DeductiveMachine:
    def __init__(self, rules):
        self.rules = rules
        self.context = {}
        self.goals = []
        self.known = False

    def find_rule(self, goal):
        for rule in self.rules:
            if rule.then_clause == goal:
                return rule
        return None

    def clean_context(self):
        self.context = {}
        self.goals = []
        self.known = False

    def ask_question(self, goal):
        answer = input(goal.capitalize() + " (да/нет): ")
        return answer.lower() == "да"

    # по ускоренному алгоритму
    def run(self, final_goal):
        self.goals.append(final_goal)
        while not self.known:
            if len(self.goals) == 0:
                self.known = True
                break
            goal = self.goals[-1]
            if goal in self.context:
                self.goals.pop()
                continue
            rule = self.find_rule(goal)
            if rule is not None:
                for condition in rule.if_clause:
                    if condition not in self.context:
                        self.context[condition] = self.ask_question(condition)
                        if not self.context[condition]:
                            print("Ответ не найден.")
                            return
                    else:
                        if not self.context[condition]:
                            print("Ответ не найден.")
                            return
                if rule.if_clause[-1] in self.context:
                    self.context[rule.then_clause] = all(self.context.get(c, False) for c in rule.if_clause)
                    self.goals.pop()
            else:
                self.context[goal] = self.ask_question(goal)
                self.goals.pop()

        if final_goal in self.context and self.context[final_goal]:
            print(f'Утверждение "{final_goal}" правдиво.')
        else:
            print("Ответ не найден.")

    # по алгоритму из условия
    # def run(self, final_goal):
    #     self.goals.append(final_goal)
    #     while not self.known:
    #         if len(self.goals) == 0:
    #             self.known = True
    #             break
    #         goal = self.goals[-1]
    #         if goal in self.context:
    #             self.goals.pop()
    #             continue
    #         rule = self.find_rule(goal)
    #         if rule is not None:
    #             for condition in rule.if_clause:
    #                 if condition not in self.context:
    #                     self.goals.append(condition)
    #             if rule.if_clause[-1] in self.context:
    #                 self.context[rule.then_clause] = all(self.context.get(c, False) for c in rule.if_clause)
    #                 self.goals.pop()
    #         else:
    #             self.context[goal] = self.ask_question(goal)
    #             self.goals.pop()
    #
    #     if final_goal in self.context and self.context[final_goal]:
    #         print(f"Ответ: {final_goal} правдиво.")
    #     else:
    #         print("Ответ не найден.")


rules = [
    Rule(["country - France"], "continent - Europe"),
    Rule(["language - French"], "national majority - French"),
    Rule(["national majority - French"], "capital - Paris"),
    Rule(["country - Japan"], "continent - Asia"),
    Rule(["language - Japanese"], "national majority - Japanese"),
    Rule(["national majority - Japanese"], "capital - Tokyo"),
    Rule(["country - Brazil"], "continent - South America"),
    Rule(["language - Portuguese"], "national majority - Portuguese"),
    Rule(["national majority - Portuguese"], "capital - Brasília"),
    Rule(["country - Australia"], "continent - Australia"),
    Rule(["language - English"], "national majority - English"),
    Rule(["national majority - English"], "capital - Canberra"),
    Rule(["country - Egypt"], "continent - Africa"),
    Rule(["language - Arabic"], "national majority - Arabic"),
    Rule(["national majority - Arabic"], "capital - Cairo")
]

if __name__ == "__main__":
    machine = DeductiveMachine(rules)

    print("\nПример 1:")
    machine.run("language - Japanese")
    machine.clean_context()

    print("\nПример 2:")
    machine.run("language - English")
    machine.clean_context()

    print("\nПример 3:")
    machine.run("national majority - Arabic")
    machine.clean_context()

    print("\nПример 4:")
    machine.run("national majority - French")
    machine.clean_context()

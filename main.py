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
    Rule(["класс - голосеменные", "структура листа - чешуеобразная"], "семейство - кипарисовые"),
    Rule(["класс - голосеменные", "структура листа - иглоподобная", "конфигурация - хаотическая"],
         "семейство - сосновые"),
    Rule(["класс - голосеменные", "структура листа - иглоподобная", "конфигурация - 2 ровных ряда"],
         "семейство - еловые"),
    Rule(["класс - голосеменные", "структура листа - иглоподобная", "конфигурация - 2 ровных ряда",
          "серебристая полоса - нет"], "семейство - болотный кипарис"),
    Rule(["тип - деревья", "форма листа - широкая и плоская"], "класс - покрытосеменные"),
    Rule(["тип - деревья", "форма листа - не (широкая и плоская)"], "класс - голосеменные"),
    Rule(["стебель - зеленый"], "тип - травянистые"),
    Rule(["стебель - древесный", "положение - стелющееся"], "тип - лианы"),
    Rule(["стебель - древесный", "положение - прямостоящее", "один основной ствол - да"], "тип - деревья"),
    Rule(["стебель - древесный", "положение - прямостоящее", "один основной ствол - нет"], "тип - кустарниковые"),
    Rule(["голова - болит", "кости - ломит", "глаза - слезяться"], "заболевание - грипп")
]

if __name__ == "__main__":
    machine = DeductiveMachine(rules)

    print("\nПример 1:")
    machine.run("семейство - кипарисовые")
    machine.clean_context()

    print("\nПример 2:")
    machine.run("семейство - сосновые")
    machine.clean_context()

    print("\nПример 3:")
    machine.run("тип - травянистые")
    machine.clean_context()

    print("\nПример 4:")
    machine.run("тип - лианы")
    machine.clean_context()

    print("\nПример 5:")
    machine.run("заболевание - грипп")
    machine.clean_context()

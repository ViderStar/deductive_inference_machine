# Deductive Machine

The Deductive Machine is a simple implementation of a deductive reasoning system. It uses a set of rules and a knowledge base to infer conclusions based on given facts and goals.

## Usage

To use the Deductive Machine, follow these steps:

1. Define the rules: Create instances of the `Rule` class, specifying the conditions in the `if_clause` and the conclusion in the `then_clause`.

2. Create an instance of the `DeductiveMachine` class, passing the rules as an argument.

3. Use the `run` method of the `DeductiveMachine` instance to start the deduction process. Pass the final goal as an argument to the `run` method.

4. The Deductive Machine will ask questions based on the rules and facts to determine the truth values of the conditions. It will continue to infer conclusions until the final goal is reached or it determines that the answer cannot be found.

5. The result of the deduction process will be printed to the console.

## Example

Here's an example of how to use the Deductive Machine:

```python
rules = [
    Rule(["класс - голосеменные", "структура листа - чешуеобразная"], "семейство - кипарисовые"),
    # Define more rules...
]

machine = DeductiveMachine(rules)

machine.run("семейство - кипарисовые")
machine.clean_context()

# Run more examples...

```

## Algorithm

The Deductive Machine uses a modified backward chaining algorithm to perform the deduction. The algorithm follows these steps:

1. Place the final goal in the goals stack. Set a boolean flag to false.

2. While the flag is false, perform the following steps:

   - If a rule can be found for analysis, check the value of the rule.
   
     - If the value is true, store the goal, its value, and the rule's number in the context stack. Accept the corresponding rule.
     
     - If the value is false, discard the rule.
     
     - If the value is unknown, place the first unknown condition and the corresponding rule's number in the goals stack.
   
   - If no rule is found for analysis, check if there is a question related to the current goal.
   
     - If a question exists, ask the question and store the obtained value in the context stack, removing it from the goals stack.
     
     - If no question exists, set the flag to true.

3. If the final goal is found in the context stack and its value is true, the answer is obtained. Otherwise, the answer cannot be found.

# Example Rules
|   #   | country   | continent        | language         | national_majority | capital    |
|-------|-----------|------------------|------------------|-------------------|------------|
|   1   | France    | Europe           | French           | -                 | -          |
|   2   | -    | -                | French           | French            | -          |
|   3   | -    | -                | -                | French            | Paris      |
|   4   | Japan     | Asia             | Japanese         | -                 | -          |
|   5   | -     | -                | Japanese         | Japanese          | -          |
|   6   | -     | -                | -                | Japanese          | Tokyo      |
|   7   | Brazil    | South America    | Portuguese       | -                 | -          |
|   8   | -    | -                | Portuguese       | Portuguese        | -          |
|   9   | -    | -                | -                | Portuguese        | Brasília   |
|   10  | Australia | Australia        | English          | -                 | -          |
|   11  | - | -                | English          | English           | -          |
|   12  | - | -                | -                | English           | Canberra   |
|   13  | Egypt     | Africa           | Arabic           | -                 | -          |
|   14  | -     | -                | Arabic           | Arabic            | -          |
|   15  | -     | -                | -                | Arabic            | Cairo      |
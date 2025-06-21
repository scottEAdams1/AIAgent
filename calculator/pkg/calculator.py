# calculator.py

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b,
            "%": lambda a, b: a % b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "%": 2,
            "^": 3,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = self._tokenize(expression)
        return self._evaluate_infix(tokens)

    def _tokenize(self, expression):
        tokens = []
        current_number = ""
        for char in expression:
            if char.isspace():
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
            elif char in self.operators or char in "()":
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
                tokens.append(char)
            else:
                current_number += char
        if current_number:
            tokens.append(current_number)
        return tokens

    def _evaluate_infix(self, tokens):
        values = []
        operators = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == "(":
                j = i + 1
                count = 1
                while j < len(tokens):
                    if tokens[j] == "(":
                        count += 1
                    elif tokens[j] == ")":
                        count -= 1
                    if count == 0:
                        break
                    j += 1
                if j == len(tokens):
                    raise ValueError("Unmatched parenthesis")
                sub_expression = tokens[i + 1:j]
                result = self._evaluate_infix(sub_expression)
                values.append(result)
                i = j + 1
                continue


            if token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            elif token == ")":
                raise ValueError("Unexpected ')'")
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")
            i += 1

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))

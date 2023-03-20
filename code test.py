class Operator:
    def __init__(self, prefix, price):
        self.prefix = prefix
        self.price = price

class Routing:
    def __init__(self):
        self.operators = []
    
    def add_operator(self, operator):
        self.operators.append(operator)
    
    def get_cheapest_operator(self,number):
        best_operator = None
        for operator in self.operators:
            if number.startswith(operator.prefix):
                if not best_operator or len(operator.prefix) > len(best_operator.prefix):
                    best_operator = operator
        return best_operator.price if best_operator else None

# Create operators A and B as described in the problem
operator_a = Routing()
operator_a.add_operator(Operator("1", 0.9))
operator_a.add_operator(Operator("268", 5.1))
operator_a.add_operator(Operator("46", 0.17))
operator_a.add_operator(Operator("4620", 0.0))
operator_a.add_operator(Operator("468", 0.15))
operator_a.add_operator(Operator("4631", 0.15))
operator_a.add_operator(Operator("4673", 0.9))
operator_a.add_operator(Operator("46732", 1.1))

operator_b = Routing()
operator_b.add_operator(Operator("1", 0.92))
operator_b.add_operator(Operator("44", 0.5))
operator_b.add_operator(Operator("46", 0.2))
operator_b.add_operator(Operator("467", 1.0))
operator_b.add_operator(Operator("48", 1.2))

def judge_best_operator(a, b, number):
    if a == None and b == None:
        print("There is no operator matching the number.") 
    elif a == None:
        print("Cheapest operator for number", number, "is B")
    elif b == None:
        print("Cheapest operator for number", number, "is A")
    else: print("Cheapest operator for number", number, "is", "A" if a < b else "B")
        

# Test with example number "+46-73212345"
number = "4673212345"
judge_best_operator(operator_a.get_cheapest_operator(number), operator_b.get_cheapest_operator(number), number)

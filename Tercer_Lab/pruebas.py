import itertools

def generate_truth_table(variables):
    num_variables = len(variables)
    truth_table = []

    for values in itertools.product([True, False], repeat=num_variables):
        row = dict(zip(variables, values))
        if row == False:
            row = 0
        elif row == True:
            row = 1
        truth_table.append(row)

    return truth_table

def evaluate_expression(expression, truth_table):
    results = []
    for row in truth_table:
        result = eval(expression, row)
        results.append(result)
        print(results)
    return results

def main():
    variables = input("Ingrese las variables separadas por comas (por ejemplo, A, B, C): ").replace(" ", "").split(",")
    expression = input("Ingrese una expresión lógica usando las variables ingresadas (usando & para AND, | para OR, ~ para NOT, y () para agrupar): ")

    truth_table = generate_truth_table(variables)
    results = evaluate_expression(expression, truth_table)

    print("\nTabla de Verdad:")
    print(" | ".join(variables) + " | " + expression)
    print("-" * (len(" | ".join(variables)) + len(expression) + 3))

    for i, row in enumerate(truth_table):
        values = [str(row[var]) for var in variables]
        result = results[i]
        print(" | ".join(values) + f" | {result}")

if __name__ == "__main__":
    main()
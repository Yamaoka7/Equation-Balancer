from sympy import symbols, Eq, solve

def balance_equation(equation):
    reactants, products = equation.split(" -> ")
    reactants = reactants.split(" + ")
    products = products.split(" + ")

    elements = set()
    for compound in reactants + products:
        for atom in compound.split():
            elements.add(atom)

    coefficients = symbols(','.join(['x' + str(i) for i in range(len(reactants))]))
    equations = []
    for element in elements:
        reactant_count = sum(compound.split().count(element) for compound in reactants)
        product_count = sum(compound.split().count(element) for compound in products)
        equations.append(Eq(reactant_count, product_count))

    solution = solve(equations + [sum(reactants[i].count(element) * coefficients[i] for i in range(len(reactants))) -
                                  sum(products[i].count(element) * coefficients[i] for i in range(len(products))) for element in elements], coefficients)
    return {f"{reactants[i]} -> {products[i]}": {str(solution[coeff]) if coeff in solution else '1' for coeff in coefficients} for i in range(len(reactants))}

equation = "H2 + O2 -> H2O"
balanced_equation = balance_equation(equation)
for reactants, products in balanced_equation.items():
    print(f"Balanced Equation: {reactants}")
    print(f"Coefficients: {products}")

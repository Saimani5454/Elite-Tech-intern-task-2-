!pip install pulp
import pulp
# Create a maximization problem
problem = pulp.LpProblem("ProfitMaximization", pulp.LpMaximize)
# Define the variables representing the number of units of each product to produce
product_a = pulp.LpVariable("ProductA", lowBound=0, cat="Integer")
product_b = pulp.LpVariable("ProductB", lowBound=0, cat="Integer")
# Define the objective function to maximize profit
problem += 5 * product_a + 4 * product_b, "TotalProfit"
# Define the constraints based on labor and raw material availability
problem += 2 * product_a + 3 * product_b <= 100, "LaborConstraint"
problem += 3 * product_a + 2 * product_b <= 120, "RawMaterialConstraint"
# Solve the optimization problem
problem.solve()
# Print the optimal solution and the total profit
print("Optimal Solution:")
print("Product A:", pulp.value(product_a))
print("Product B:", pulp.value(product_b))
print("Total Profit:", pulp.value(problem.objective))

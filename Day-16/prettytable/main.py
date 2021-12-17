# import pretty table package
import prettytable

# created an object of Prettytable
customTable = prettytable.PrettyTable()

customTable.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
customTable.add_column("Type", ["Electric", "Water", "Fire"])

print(customTable)

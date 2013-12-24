#thanks for coming

# Total price before tax
food = 5.00

# Percentage of tax in decimal format. This is 5 percent.
tax = 0.05

# Percentage of taxed total to tip as a decimal value. below is 20 percent.
tip = 0.20

# This change the value of food to food and tax combined
food = food + food * tax

# This is tipped on the taxed total
total = food + food * tip

print("%.2f" % total)

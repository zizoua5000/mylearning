import pygal
from die import Die

# create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store result
results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analize the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append((frequency/1000000)*100)

print(frequencies)

# visualize the resuts
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "Frequency of result"

hist.add("D6 + D6", frequencies)
hist.render_to_file("die_visual.svg")

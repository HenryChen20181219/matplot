from die import Die
import pygal

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#分析结果：每个点数出现的次数
frequencies = []
for value in range(1,die1.num_sides+die2.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result'

hist.y_title = 'Frequency of Result'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')


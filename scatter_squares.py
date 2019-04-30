import matplotlib.pyplot as plt


#绘制散点图
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,s=40,c=(0,0,0.8),edgecolors=None) #s为绘制点的大小,c:值越接近0， 指定的颜色越深， 值越接近1， 指定的颜色越浅。
plt.scatter(x_values,y_values,s=40,c=y_values,cmap=plt.cm.Blues,edgecolors=None)

plt.axis([0,1100,0,1100000])
#设置图表标题并给坐标轴加上标签
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=4)


plt.show()
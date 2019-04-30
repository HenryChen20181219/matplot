import matplotlib.pyplot as plt


input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]

#绘制折线图plot
plt.plot(input_value,squares,linewidth=5)
#设置标题和标题字体的大小
plt.title('Square Numbers',fontsize=24)
#设置x轴，y轴，字体大小
plt.xlabel('Value',fontsize=24)
plt.ylabel('Square of Value',fontsize=24)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()
import matplotlib.pyplot as plt
import matplotlib
import networkx as nx

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_xlim([0, 10])
# ax.set_ylim([0, 10])


def onclick(event, arg):
    assert isinstance(event, matplotlib.backend_bases.MouseEvent)
    # print(type(event))
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    plt.plot(event.xdata, event.ydata, '*')
    fig.canvas.draw()
    fig.canvas.draw_idle()
    arg[0] = event.xdata
    arg[1] = event.ydata

def onrelease(event, arg, pos):
    print(arg[0])
    print(arg[1])
    for k, v in pos.items():
        if (arg[0] - v[0])**2+(arg[1] - v[1])**2 <= 0.1:
            print("在",end='\t');        print(k)


g = nx.Graph()
for i in range(10):
    g.add_node(i)

pos = nx.spring_layout(g)
print(pos)
fig = plt.figure()
arg = [1,2]
cid = fig.canvas.mpl_connect('button_press_event', lambda event: onclick(event, arg))
cid = fig.canvas.mpl_connect('button_release_event', lambda event: onrelease(event, arg, pos))



nx.draw(g, pos, node_size=5)


plt.show()

# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
# text = ax.text(0.5, 0.5, 'event', ha='center', va='center', fontdict={'size': 20})
#
#
# def call_back(event):
#     info = 'name:{}\n button:{}\n x,y:{},{}\n xdata:{}\nydata:{}'.format(event.name, event.button,event.x, event.y,event.xdata, event.ydata)
#     text.set_text(info)
#     fig.canvas.draw_idle()
#
#
# fig.canvas.mpl_connect('button_press_event', call_back)
# fig.canvas.mpl_connect('button_release_event', call_back)
# fig.canvas.mpl_connect('motion_notify_event', call_back)

# plt.show()
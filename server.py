# # import numpy as np
# # import matplotlib.pyplot as plt
# # from matplotlib.animation import FuncAnimation

# # x = []
# # y = []

# # figure, ax = plt.subplots(figsize=(4, 3))
# # (line,) = ax.plot(x, y)
# # plt.axis([0, 4 * np.pi, -1, 1])


# # def func_animate(i):
# #     x = np.linspace(0, 4 * np.pi, 1000)
# #     y = np.sin(2 * (x - 0.1 * i))

# #     line.set_data(x, y)

# #     return (line,)


# # ani = FuncAnimation(figure, func_animate, frames=10, interval=50)

# # ani.save(r"animation.gif", fps=10)

# # plt.show()

# import time

# from flask import app

# @app.route('/', methods=['GET','POST'])
#     # Rest of the code...
# def generate_data():
#     return time.time()
# def display_data():
#     while True:
#         data = generate_data()
#         print(f"現在の時刻は{data}です")
#         time.sleep(1)
# if __name__ == "__main__":
#     display_data()
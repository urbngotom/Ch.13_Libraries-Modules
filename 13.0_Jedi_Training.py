'''
# 13.0 Jedi Training (10pts)  Name:________________

 BOX CLASS LIBRARY  (5pts)
 -----------------
For this test, take your 30 box program and remove the Box Class into a seperate file called Box_Builder.py. Now just
import the Box Class into your main program. Use if __name__ =="__main__":

'''
# import arcade
# import random
# import Box_Builder
# SW = 600
# SH = 600
#
# class Box():
#     def __init__(self, x, y, dx, dy, box_size):
#         self.x = x
#         self.y = y
#         self.color = arcade.color.WHITE
#         self.dx = dx
#         self.dy = dy
#         self.box_size = box_size
#
#     def draw_box(self):
#         arcade.draw_rectangle_filled(self.x, self.y, self.box_size, self.box_size, self.color)
#
#
#     def update_box(self):
#         self.x += self.dx
#         self.y += self.dy
#
#         if self.x <= 30:
#             self.dx *= -1
#             self.color = arcade.color.WISTERIA
#         if self.x >= SW-30:
#             self.dx *= -1
#             self.color = arcade.color.FAWN
#         if self.y <= 30:
#             self.dy *= -1
#             self.color = arcade.color.LIGHT_BLUE
#         if self.y >= SH-30:
#             self.dy *= -1
#             self.color = arcade.color.LIGHT_GREEN

# class MyGame(arcade.Window):
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         self.box_list = []
#         for i in range(30):
#             dx = random.randint(-5, 5)
#             dy = random.randint(-5, 5)
#             box_size = random.randint(10, 50)
#             position_x = random.randint(35, SW-35)
#             position_y = random.randint(35, SH-35)
#             self.box = Box_Builder.Box(position_x, position_y, dx, dy, box_size)
#             self.box_list.append(self.box)
#
#
#     def on_draw(self):
#         arcade.start_render()
#         arcade.draw_rectangle_filled(0, SH / 2, SW / 20, SH, arcade.color.WISTERIA)
#         arcade.draw_rectangle_filled(SW / 2, 0, SW, SH / 20, arcade.color.LIGHT_BLUE)
#         arcade.draw_rectangle_filled(SW, SH / 2, SW / 20, SH, arcade.color.FAWN)
#         arcade.draw_rectangle_filled(SW / 2, SH, SW, SH / 20, arcade.color.LIGHT_GREEN)
#         for box in self.box_list:
#             box.draw_box()
#
#     def on_update(self, dt):
#         for box in self.box_list:
#             box.update_box()
#
# def main():
#     window = MyGame(SW, SH, "Drawing Example")
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()


'''
FUNCTIONS LIBRARY  (5pts)
 -----------------
Paste all the functions that you submitted in the Functions chapter into a single file called my_library.py.
This should only include all of the (defs), not the inputs and function calls. 
Create a main program called my_program.py which will import the my_library module. 
In this program you will put the inputs and function calls. 
Use the import * so you don't have to use namespaces for each function call. 
Use if __name__ =="__main__":
You can just demonstrate this to your instructor when you have completed both of these tasks.
'''

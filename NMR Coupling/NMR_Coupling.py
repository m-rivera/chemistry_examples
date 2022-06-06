from manim import *
from manim.utils.file_ops import open_file as open_media_file 
import math

n = [1,1]
J_coupling_constants = [6,2]

class Function(Scene):

    def function(self,x,positions,n_index):
        standard_deviation = 0.125
        y = 0
        coefficient = 1
        for a in n[:n_index+1]:
            coefficient = (2**a)*coefficient
        if n_index == -1:
            coefficient = 1
        for position in positions:
            y += (math.exp(-((x-position)**2)/(2*standard_deviation))/(standard_deviation*math.sqrt(2/math.pi)))/coefficient
        return y

    def construct(self):
        colour = color_gradient((BLUE,RED), len(n)+1)
        axes = Axes(
            x_range=[-20, 20, 5],
            y_range=[0, 10, 5],
            x_length=12,
            y_length=6,
            tips=False,
        )#.add_coordinates((range(-20,20,5)))
        self.add(axes)

        positions = [0]
        n_index = -1
        self.draw_curves(positions,axes,n_index,colour)
        for n_index in range(len(n)):
            for i in range(n[n_index]):
                for i in range(len(positions)):
                    positions.append(positions[i]+J_coupling_constants[n_index]/2)
                    positions[i]=positions[i]-J_coupling_constants[n_index]/2
            self.draw_curves(positions,axes,n_index,colour)

    def draw_curves(self,positions,axes,n_index, colour):
        '''
        for position in positions:
            position = [position]
            graph = axes.plot(
                (lambda x:self.function(x,position,n_index)),
                x_range=[-20,20],
                color=YELLOW
            )
            self.add(graph)'''

        graph = axes.plot(
            (lambda x:self.function(x,positions,n_index)),
            x_range=[-20,20],
            color=colour[n_index+1]
        )
        
        self.add(graph)
    

if __name__ == '__main__':
    scene = Function()
    scene.render(preview=True)
    open_media_file(scene.renderer.file_writer.movie_file_path)
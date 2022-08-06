from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.properties import Clock

class MainWidget(Widget):
    persepcetive_point_x=NumericProperty(0)
    persepcetive_point_y=NumericProperty(0)
    V_NB_LINES=7
    V_LINES_SPACING=.1
    vertical_line=[]

    H_NB_LINES=7
    H_LINES_SPACING=.1
    horizontal_line=[]

    def __init__(self, **kwargs):
        super(MainWidget,self).__init__(**kwargs)
        self.persepcetive_point_y=self.height*3/4
        self.persepcetive_point_x=self.width/2
        self.init_vertical_lines()
        self.init_horizontal_lines()
        Clock.schedule_interval(self.update,1/60)
    def on_parent(self,widget,parent):
        pass
    def on_size(self,*args):
        self.persepcetive_point_y=self.height*3/4
        self.persepcetive_point_x=self.width/2
        self.update_vertical_lines()
        self.update_horizontal_lines()
    def on_perspective_point_x(self,widget,value):
        pass
    def on_perspective_point_y(self,widget,value):
        pass
    
    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(self.V_NB_LINES):
                self.vertical_lines.append(Line())
    def update_vertical_lines(self):
        central_line_x=int(self.width/2)
        spacing=self.V_LINES_SPACING*self.width
        offset=-int(self.V_NB_LINES/2)+0.5
        for i in range(self.V_NB_LINES):
            line_x=int(central_line_x+offset*spacing)
            x1,y1=self.transform(line_x,0)
            x2,y2=self.transform(line_x,0)
            self.vertical_line[i].points=[x1,y1,x2,y2]
            offset+=1
    
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(self.V_NB_LINES):
                self.horizontal_lines.append(Line())
    
    def update_horizontal_lines(self):
        central_line_x=int(self.width/2)
        spacing=self.V_LINES_SPACING*self.width
        offset=-int(self.V_NB_LINES/2)+0.5
        xmin=central_line_x+offset*spacing
        xmax=central_line_x-offset*spacing
        spacing_y=self.H_LINES_SPACING*self.height
        for i in range(self.H_NB_LINES):
            line_y=i*spacing_y
            x1,y1=self.transform(xmin,line_y)
            x2,y2=self.transform(xmax,line_y)
            self.horizontal_line[i].points=[x1,y1,x2,y2]
    def transform(self,x,y):
        return self.transform_perspective(x,y)

    def transform_2D(self,x,y):
        return int(x),int(y)

    def transform_perspective(self,x,y):
        lin_y=y*self.persepcetive_point_y/self.height
        if lin_y>self.persepcetive_point_y:
            lin_y=self.persepcetive_point_y
        diff_x=x-self.persepcetive_point_x
        diff_y=self.persepcetive_point_y-lin_y
        factor_y=diff_y/self.persepcetive_point_y
        factor_y=factor_y**2
        tr_x=self.persepcetive_point_x+diff_x*factor_y
        tr_y=self.persepcetive_point_y-factor_y*self.persepcetive_point_y
        return int(tr_x),int(lin_y)

    def update(self,dt):
        print("1")


class GalaxyApp(App):
    pass


GalaxyApp().run()
import numpy as np

class Cube:
    def __init__(self, sides = None, flag = False, config = None):
        if sides == None:
            self.top = np.array([['U' for i in range(3)] for j in range(3)])
            self.front = np.array([['F' for i in range(3)] for j in range(3)])
            self.back = np.array([['B' for i in range(3)] for j in range(3)])
            self.left = np.array([['L' for i in range(3)] for j in range(3)])
            self.right = np.array([['R' for i in range(3)] for j in range(3)])
            self.down = np.array([['D' for i in range(3)] for j in range(3)])
        else:
            self.top = sides['top']
            self.front = sides['front']
            self.back = sides['back']
            self.left = sides['left']
            self.right = sides['right']
            self.down = sides['down']
        if flag == True:
            k = 0
            self.top = np.array([[config[(3*(j+k))+i] for i in range(3)] for j in range(3)])
            k = 3
            self.right = np.array([[config[(3*(j+k))+i] for i in range(3)] for j in range(3)])
            k = 6
            self.front = np.array([[config[(3*(j+k))+i] for i in range(3)] for j in range(3)])
            k = 9
            self.down = np.array([[config[(3*(j+k))+i] for i in range(3)] for j in range(3)])
            k = 12
            self.left = np.array([[config[(3*(j+k))+i] for i in range(3)] for j in range(3)])
            k = 15
            self.back = np.array([[config[(3*(j+k))+i] for i in range(3)] for j in range(3)])
        self.cube = {}
        self.cube['top'] = self.top
        self.cube['front'] = self.front
        self.cube['back'] = self.back
        self.cube['left'] = self.left
        self.cube['right'] = self.right
        self.cube['down'] = self.down
    
    def rr_(self):
        temp = self.front[0:3, 2].copy()
        self.front[0:3, 2] = self.top[0:3, 2].copy()
        self.top[0:3, 2] = np.flip(self.back[0:3, 0].copy())
        self.back[0:3, 0] = np.flip(self.down[0:3, 2].copy())
        self.down[0:3, 2] = temp
        
        t1 = self.right[0:3, 0].copy()
        t2 = self.right[0].copy()
        t3 = self.right[0:3,2].copy()
        t4 = self.right[2].copy()
        self.right[0:3, 0] = np.flip(t2)
        self.right[0] = t3
        self.right[0:3,2] = np.flip(t4)
        self.right[2] = t1
        
    def rr(self):
        temp = self.top[0:3, 2].copy()
        self.top[0:3, 2] = self.front[0:3, 2].copy()
        self.front[0:3, 2] = self.down[0:3, 2].copy()
        self.down[0:3, 2] = np.flip(self.back[0:3, 0].copy())
        self.back[0:3, 0] = np.flip(temp.copy())
        
        t1 = self.right[0:3, 0].copy()
        t2 = self.right[0].copy()
        t3 = self.right[0:3,2].copy()
        t4 = self.right[2].copy()
        self.right[0:3, 0] = t4
        self.right[0] = np.flip(t1)
        self.right[0:3,2] = t2
        self.right[2] = np.flip(t3)
        
    def rl_(self):
        temp = self.top[0:3, 0].copy()
        self.top[0:3, 0] = self.front[0:3, 0].copy()
        self.front[0:3, 0] = self.down[0:3, 0].copy()
        self.down[0:3, 0] = np.flip(self.back[0:3, 2].copy())
        self.back[0:3, 2] = np.flip(temp.copy())
        
        t1 = self.left[0:3, 0].copy()
        t2 = self.left[0].copy()
        t3 = self.left[0:3,2].copy()
        t4 = self.left[2].copy()
        self.left[0:3, 0] = np.flip(t2)
        self.left[0] = t3
        self.left[0:3,2] = np.flip(t4)
        self.left[2] = t1
        
    def rl(self):
        temp = self.front[0:3, 0].copy()
        self.front[0:3, 0] = self.top[0:3, 0].copy()
        self.top[0:3, 0] = np.flip(self.back[0:3, 2].copy())
        self.back[0:3, 2] = np.flip(self.down[0:3, 0].copy())
        self.down[0:3, 0] = temp
        
        t1 = self.left[0:3, 0].copy()
        t2 = self.left[0].copy()
        t3 = self.left[0:3,2].copy()
        t4 = self.left[2].copy()
        self.left[0:3, 0] = t4
        self.left[0] = np.flip(t1)
        self.left[0:3,2] = t2
        self.left[2] = np.flip(t3)
        
    def rt_(self):
        temp = self.front[0].copy()
        self.front[0] = self.left[0].copy()
        self.left[0] = self.back[0].copy()
        self.back[0] = self.right[0].copy()
        self.right[0] = temp
        
        t1 = self.top[0:3, 0].copy()
        t2 = self.top[0].copy()
        t3 = self.top[0:3,2].copy()
        t4 = self.top[2].copy()
        self.top[0:3, 0] = np.flip(t2)
        self.top[0] = t3
        self.top[0:3,2] = np.flip(t4)
        self.top[2] = t1
    
    def rt(self):
        temp = self.front[0].copy()
        self.front[0] = self.right[0].copy()
        self.right[0] = self.back[0].copy()
        self.back[0] = self.left[0].copy()
        self.left[0] = temp
        
        t1 = self.top[0:3, 0].copy()
        t2 = self.top[0].copy()
        t3 = self.top[0:3,2].copy()
        t4 = self.top[2].copy()
        self.top[0:3, 0] = t4
        self.top[0] = np.flip(t1)
        self.top[0:3,2] = t2
        self.top[2] = np.flip(t3)
    
    def rf_(self):
        temp = self.top[2].copy()
        self.top[2] = self.right[0:3, 0].copy()
        self.right[0:3, 0] = np.flip(self.down[0].copy())
        self.down[0] = self.left[0:3, 2].copy()
        self.left[0:3, 2] = np.flip(temp.copy())
        
        t1 = self.front[0:3, 0].copy()
        t2 = self.front[0].copy()
        t3 = self.front[0:3,2].copy()
        t4 = self.front[2].copy()
        self.front[0:3, 0] = np.flip(t2)
        self.front[0] = t3
        self.front[0:3,2] = np.flip(t4)
        self.front[2] = t1
    
    def rf(self):
        temp = self.top[2].copy()
        self.top[2] = np.flip(self.left[0:3, 2].copy())
        self.left[0:3, 2] = self.down[0].copy()
        self.down[0] = np.flip(self.right[0:3, 0].copy())
        self.right[0:3, 0] = temp
        
        t1 = self.front[0:3, 0].copy()
        t2 = self.front[0].copy()
        t3 = self.front[0:3,2].copy()
        t4 = self.front[2].copy()
        self.front[0:3, 0] = t4
        self.front[0] = np.flip(t1)
        self.front[0:3,2] = t2
        self.front[2] = np.flip(t3)
    
    def rd_(self):
        temp = self.front[2].copy()
        self.front[2] = self.right[2].copy()
        self.right[2] = self.back[2].copy()
        self.back[2] = self.left[2].copy()
        self.left[2] = temp
        
        t1 = self.down[0:3, 0].copy()
        t2 = self.down[0].copy()
        t3 = self.down[0:3,2].copy()
        t4 = self.down[2].copy()
        self.down[0:3, 0] = np.flip(t2)
        self.down[0] = t3
        self.down[0:3,2] = np.flip(t4)
        self.down[2] = t1
    
    def rd(self):
        temp = self.front[2].copy()
        self.front[2] = self.left[2].copy()
        self.left[2] = self.back[2].copy()
        self.back[2] = self.right[2].copy()
        self.right[2] = temp
        
        t1 = self.down[0:3, 0].copy()
        t2 = self.down[0].copy()
        t3 = self.down[0:3,2].copy()
        t4 = self.down[2].copy()
        self.down[0:3, 0] = t4
        self.down[0] = np.flip(t1)
        self.down[0:3,2] = t2
        self.down[2] = np.flip(t3)
    
    def rb_(self):
        temp = self.top[0].copy()
        self.top[0] = np.flip(self.left[0:3,0].copy())
        self.left[0:3,0] = self.down[2].copy()
        self.down[2] = np.flip(self.right[0:3,2].copy())
        self.right[0:3,2] = temp
        
        t1 = self.back[0:3, 0].copy()
        t2 = self.back[0].copy()
        t3 = self.back[0:3,2].copy()
        t4 = self.back[2].copy()
        self.back[0:3, 0] = np.flip(t2)
        self.back[0] = t3
        self.back[0:3,2] = np.flip(t4)
        self.back[2] = t1
    
    def rb(self):
        temp = self.top[0].copy()
        self.top[0] = self.right[0:3,2].copy()
        self.right[0:3,2] = np.flip(self.down[2].copy())
        self.down[2] = self.left[0:3,0].copy()
        self.left[0:3,0] = np.flip(temp.copy())
        
        t1 = self.back[0:3, 0].copy()
        t2 = self.back[0].copy()
        t3 = self.back[0:3,2].copy()
        t4 = self.back[2].copy()
        self.back[0:3, 0] = t4
        self.back[0] = np.flip(t1)
        self.back[0:3,2] = t2
        self.back[2] = np.flip(t3)
    
    def get_string(self):
        string = ''
        sides = ['top', 'right', 'front', 'down', 'left', 'back']
        for side in sides:
            string += ''.join([''.join(layer) for layer in self.cube[side]])
        return string
    
    def show(self):
        for key in self.cube.keys():
            print(key,':-')
            print(self.cube[key], end = '\n\n')
    
#     def get_reward(self):
#         count = 0
#         for key in self.cube.keys():
#             sum(self.cube[key].flatten() == self.cube[key][1,1])
#         return count
    
    def get_state(self):
        self.state = np.stack((self.top, self.front, self.back, self.left, self.right, self.down), axis = 0)
        return self.state
    
    def shuffle(self, moves, out = True):
        for i in range(moves):
            x = np.random.randint(0, 12)
            if x == 0: 
#                 print('rr')
                self.rr()
            elif x == 1: 
#                 print('rr_')
                self.rr_()
            elif x == 2: 
#                 print('rl')
                self.rl()
            elif x == 3: 
#                 print('rl_')
                self.rl_()
            elif x == 4: 
#                 print('rt')
                self.rt()
            elif x == 5: 
#                 print('rt_')
                self.rt_()
            elif x == 6: 
#                 print('rf')
                self.rf()
            elif x == 7: 
#                 print('rf_')
                self.rf_()
            elif x == 8: 
#                 print('rb')
                self.rb()
            elif x == 9: 
#                 print('rb_')
                self.rb_()
            elif x == 10: 
#                 print('rd')
                self.rd()
            elif x == 11: 
#                 print('rd_')
                self.rd_()
        if out:
            print('cube shuffled')
        return x

    def is_solved(self, out = True):
        for key in self.cube.keys():
            if len(set(self.cube[key].flatten())) != 1:
#                 print('Not Solved')
                return 0
        if out:
            print('SOLVED')
        return 1


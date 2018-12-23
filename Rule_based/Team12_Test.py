import numpy as np

from new_rules import New_Rules

import errno
import os
from datetime import datetime

import argparse

from api import vrep


max_goal_number = 0
episodes=1000
is_batch_norm = True #batch normalization switch

def main():
    env = New_Rules()
    counter=0
    
    step = 0
    for i in range(episodes):
        print ("==== Starting episode no:",i,"====","\n")
        observation = env.reset()
        goal_number = 0
        while True:
            x = observation

            env.step()
            '''
            if env.finishCheck():
                #maxi = np.max(goal_number, max_goal_number)
                #max_goal_number = maxi
                print ('EPISODE: ',i, 'Maximum goal number: ',max_goal_number)
                
                break
                '''

        step += 1

           
    print ('Total Maximum goal number: ',max_goal_number)


if __name__ == '__main__':
    main()  

       

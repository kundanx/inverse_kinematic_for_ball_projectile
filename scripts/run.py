import os
import mujoco 
import itertools
import numpy as np
import time
import keyboard
from mujoco import viewer

keyboard_bindings = {
    262: 'right_arrow',
    263:  'left_arrow' ,
    264: 'down_arrow',
    265: 'up_arrow'
}

def keyboard_interrupt(keycode):
    try:
        key = keyboard_bindings[keycode]
        print(f"Keyboard interrupt occured {key}")
        
    except Exception as e:
        print(f"Invalid key enterred")
        

def dist_callback(a,b,c):
    # pass
    # print("cus callbaxk")
    print(c)

def main():
    path = 'gamefield.xml'
    dirname = os.path.dirname(os.path.dirname(__file__))
    xml_path = os.path.join(dirname + "/xml/"+ path)

    m = mujoco.MjModel.from_xml_path(xml_path)
    d = mujoco.MjData(m)
    
    # x = m.geom('ball')
    # print(x)
    # x = m.geom('gamefield')
    # print(x)
    # x = m.body('robot')
    # print(x)
    # c = m.sensor('custom_sensor')
    # print(x)
    # x = m.sensor('distance_sensor')
    # print(x)

    # mujoco.set_mjcb_sensor(dist_callback)

    # return
    # print(ball_data)
    with mujoco.viewer.launch_passive(m, d, key_callback= keyboard_interrupt) as viewer:
        # viewer.user_scn.flags[mujoco.mjtRndFlag.mjRND_WIREFRAME] = 1
        # viewer.sync()
        while viewer.is_running():
            # d.qvel[0] = 1
            mujoco.mj_step(m, d)
            
            viewer.user_scn.ngeom = 1
            viewer.sync()
            
            # data = d.sensordata[x.id]
            # # print(data)
            # data = d.sensordata[c.id]
            # # print(data)

            sleep_time = 0.01
            time.sleep(sleep_time)
        
        
if __name__=="__main__":
    main()

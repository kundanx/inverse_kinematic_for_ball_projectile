import os
import mujoco as mj
from mujoco import viewer

xml_path = 'ball.xml'
dirname = os.path.dirname(os.path.dirname(__file__))
abspath = os.path.join(dirname + "/" +"xml"+"/"+ xml_path)
xml_path = abspath
print(xml_path)

ball = mj.MjModel.from_xml_path(xml_path)
ball_data = mj.MjData(ball)
# print(ball_data)
ball_data.qvel[0] = 5
viewer.launch(ball, ball_data)

# print(xml_path)


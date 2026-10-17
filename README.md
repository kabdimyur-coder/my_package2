#Заключительное задание

# 1.Создал Dockerfile в разделе /catkin_ws/src/my_package![](https://github.com/kabdimyur-coder/images/blob/master/1.png?raw=true)
#Собрал образ по команде Docker build -t ros1:container1 /bin/bash, далее запустил контейнер с пробросом портов 8080:8080
#Потом внутри контейнера запустил xpra командой xpra start --start=xterm --bind-tcp=0.0.0.0:8080
# 2.В другом терминале запустил xpra attach tcp://172.17.0.2:8080 и открыл ещё 3 терминала командой xterm& ![](https://github.com/kabdimyur-coder/images/blob/master/2.png?raw=true)
# 3.Далее активировал переменное окружение командой source /opt/ros/noetic/setup.bash и запустил Gazebo командой export TURTLEBOT3_MODEL=burger; roslaunch turtlebot3_gazebo turtlebot3_world.launch
#в следующем терминале так же активировал переменное окружение и запустил Rviz команндой export TURTLEBOT3_MODEL=burger; roslaunch turtlebot3_navigation turtlebot3_navigation.launch
#задал правильную позицию роботу ![](https://github.com/kabdimyur-coder/images/blob/master/3.png?raw=true)
# 4.Написал скрипт turtlebot3_trajectory.py что бы робат двигался по задвнным точкам, тем самым эмитировал движение робота пылесоса,конечто настоящий робот
#двигается на много сложнее но для демонстрации я думаю этого достаточно ![](https://github.com/kabdimyur-coder/images/blob/master/8.png?raw=true)
#потом написал скрипт подписывающийся на топики датчиков /odom , /imu , /Laserscan ![](https://github.com/kabdimyur-coder/images/blob/master/5.png?raw=true)
# 5.Эти два скрипта расположил в нутри контейнера ![](https://github.com/kabdimyur-coder/images/blob/master/6.png?raw=true)
# 6.Далее запустил эти два скрипта в терминале xpra робот двигался как пылесос объезжая препятствия и в терминале отображались данные с датчиков ![](https://github.com/kabdimyur-coder/images/blob/master/7.png?raw=true)
# 7.Далее я закомител и запушил образ на DockerHub docker pull kabdimyur/ros1:container1


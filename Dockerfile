# Начнём с базового образа ROS (замените humble на желаемую
#версию, если это необходимо)
FROM osrf/ros:noetic-desktop-full
# Задаём переменную окружения, чтобы пользователь не
#участвовал в установке (выбор клавиатуры и прочее)
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=noetic
ENV TURTLEBOT3_MODEL=burger
# Установим необходимые пакеты
RUN apt-get update && apt-get install --no-install-recommends -y \
    xpra \
    xterm \
    netcat \
    net-tools \
    nano \
    ros-noetic-turtlebot3 \
    ros-noetic-turtlebot3-simulations \
    ros-noetic-gazebo-ros \
    ros-noetic-rviz \
    ros-noetic-turtlebot3-bringup \
    ros-noetic-turtlebot3-description \
    ros-noetic-turtlebot3-teleop \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*
# Добавим настройки переменных окружения в .bashrc
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc \
    && echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc \
    && echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
# Зададим стартовую команду для контейнера
CMD ["bash"]

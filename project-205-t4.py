import glob
import os
import sys
import argparse
import random
import time
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
    
import carla
#create a list name actor_list
actor_list = []
def main(arg):
    """Main function of the script"""
    #python script for host and port declaration and put in client variable
    client=carla.Client('127.0.0.1', 2000)
    #Time to wait for screen
    client.set_timeout(2.0)
    #Define get_world() method and save in world variable
    world=client.get_world()
    #define try
    try:
        #define blueprint of world

        get_blueprint_of_world=world.get_blueprint_library()

        #vehicle model

        car_model=get_blueprint_of_world.filter('model3')[0]

        #location for the vehicle

        spawn_point=random.choice(world.get_map().get_spawn_points())
        
        dropped_vehicle=world.spawn_actor(car_model, spawn_point) #call vehicle with variable name dropped_vehicle
        dropped_vehicle.set_autopilot(True) #set vehicle as autopilot

        spectator_transform = carla.Transform(vehicle_transform.location, vehicle_transform.rotation)
        spectator_transform.location += vehicle_transform.get_forward_vector() * 20
        spectator_transform.rotation.yaw += 180
        spectator = world.get_spectator()
        spectator.set_transform(spectator_transform)
        vehicle.set_transform(vehicle_transform)
        actor_list.append(dropped_vehicle)

        #put time in sleep for 1000
        time.sleep(1000)


    finally:
        print('destroying actors')
        #create a loop for actor in actor_list
        for actor in actor_list:
            #actor every actor
            actor.destroy()
        print('done.')
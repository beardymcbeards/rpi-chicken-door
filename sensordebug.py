#!/usr/bin/python2
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Infinate loop that prints the sensor states, helps for sensor positioning

import argparse
import ConfigParser
import time
import robocoop


if __name__ == '__main__':
    description = ('debug door sensors')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--door', dest='door', nargs='*', default='NULL',
                        help='A space seperated list of door names to operate on')
    args, __ = parser.parse_known_args()

    config = ConfigParser.ConfigParser()
    config.read('robocoop.cfg')

    door = args.door[0]

    try:
        obj = robocoop.robocoop(door, config.getint(door, 'top_sensor_pin'),
                                config.getint(door, 'bottom_sensor_pin'),
                                config.getint(door, 'motor_a_pin'),
                                config.getint(door, 'motor_b_pin'),
                                config.getint(door, 'safety_limit'))


        toppin = config.getint(door, 'top_sensor_pin')
        botpin = config.getint(door, 'bottom_sensor_pin')
        while True:
            print("TOP: %s" % robocoop.GPIO.input(toppin))
            print("BOTTOM: %s" % robocoop.GPIO.input(botpin))
            time.sleep(1)
    except KeyboardInterrupt:
        print (' peace out')
    finally:
        print('cleaning up')
        obj.cleanup()
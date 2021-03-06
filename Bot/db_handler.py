# created by Sami Bosch on Wednesday, 10 February 2020

# This file contains all functions necessary to handle the database

import os
import json

songs = '../dates.json'
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, songs)
if not os.path.exists(filename):
    with open(filename, "w+") as f:
        json.dump({"birthdays": {}, "channel": None, "events": {}, "role": None, "flair": []}, f)
        f.truncate()
        f.close()

with open(filename, "r+") as f:
    db = json.load(f)
    f.close()

if "birthdays" not in db:
    db['birthdays'] = {}

if "channel" not in db:
    db['channel'] = None

if "role" not in db:
    db['role'] = None

if "events" not in db:
    db['events'] = {}

for event in db['events']:
    date = db['events'][event]
    if isinstance(date, str):
        db['events'][event] = (date, False)

if "flair" not in db:
    db['flair'] = []


def write():
    with open(filename, "w+") as file:
        json.dump(db, file)
        file.truncate()
        file.close()


def add_event(name, date, one_time=False):
    datestr = str(date.day) + "/" + str(date.month) + "/" + str(date.year)
    db['events'][name] = (datestr, one_time)
    write()


def remove_event(name):
    if name in db['events']:
        db['events'].pop(name)
        write()


def get_event_date(name):
    if name in db['events']:
        return db['events'][name]
    else:
        return None


def get_events():
    return db['events'].keys()


def add_birthday(name, date):
    datestr = str(date.day) + "/" + str(date.month)
    if datestr in db['birthdays']:
        db['birthdays'][datestr].append(name)
    else:
        db['birthdays'][datestr] = [name]
    write()


def remove_birthday(name, date):
    datestr = str(date.day) + "/" + str(date.month)
    if datestr in db['birthdays'] and name in db['birthdays'][datestr]:
        if len(db['birthdays'][datestr]) == 1:
            db['birthdays'].pop(datestr)
        else:
            db['birthdays'][datestr].pop(name)
        write()


def get_birthdays(date):
    datestr = str(date.day) + "/" + str(date.month)
    if datestr in db['birthdays']:
        return db['birthdays'][datestr]
    else:
        return []


def set_channel(gid, cid):
    db['channel'] = (gid, cid)
    write()


def get_channel():
    return db['channel']


def set_role(gid, rid):
    db['role'] = (gid, rid)
    write()


def get_role():
    return db['role']


def get_flairs():
    return db['flair']


def add_flair(name):
    db['flair'].append(name)
    write()


def remove_flair(name):
    db['flair'].remove(name)
    write()

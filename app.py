#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
import uuid
from wsgiref import simple_server
import os
from jinja2 import Environment, PackageLoader, select_autoescape

class MainPage(object):
    
    def __init__(self, sessions, renderer):
        self.sessions = sessions
        self.renderer = renderer
        self.data = renderer.data

    def on_get(self, req, resp):
        resp.content_type = 'text/html'
        session_id = sessions.new_session(data.ships[0])
        resp.set_cookie('session_id', session_id)
        resp.body = self.renderer.render(sessions.get_build(session_id))
        resp.status = falcon.HTTP_200

class Content():
    
    def __init__(self, template_path, data):
        self.data = data
        env = Environment(
            loader=PackageLoader('app', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.template = env.get_template(template_path)

    def render(self, build):
        return self.template.render(data=data, build=build)

class SessionStorage(object):
    
     def __init__(self):
         self.sessions = {}

     def new_session(self, ship):
         session_id = str(uuid.uuid1())
         build = Build(ship)
         self.sessions[session_id] = build
         return session_id
        
     def get_build(self, session_id):
         return self.sessions.get(session_id)
                
class Build(object):

    def __init__(self, ship):

        # initialize whatever we can dynamically
        for key, value in ship.items():
            setattr(self, key, value)

        # init the rest 
        self.mass_current = self.mass_max
        self.upgrade_cost = 0
        for component_list in self.slots.values():
            component_list.sort()

    def add(self, size, component):
        self.slots[size].append(component)
        update()
        
    def remove(self, size, index):
        self.slots[size].pop(index)
        update()
        
    def update():
        # TODO
        pass
        

class Data(object):
    
    slot_sizes = ['large', 'medium', 'small']
    components = {
        'large': {
            'cargo': [
                'Cargo Hold 1',
                'Cargo Hold 2',
                'Cargo Hold 3',
                'Cargo Hold 4',
                'Cargo Hold 5',
                'Luxury Cabin',
                'Passenger Cabin',
            ], 'crew': [
                'Barracks 1',
                'Barracks 2',
                'Barracks 3',
                'Barracks 5',
                'Barracks 4',
            ],
        }, 
        'medium': {
            'core': [            
                'Reinforced Barracks 5',
                'Reinforced Barracks 8',
                'Weapons Locker A5',
                'Reinforced Barracks 4',
                'Reinforced Barracks 6',
                'Shielded Barracks 4',
                'Reinforced Barracks 3',
                'Valiant Autocannon',
                'M90 Barrel-Cannon',
                'M92 Barrel-Cannon',
                'M94 Barrel-Cannon',
            ],
        }
    }
    
    ships = [
        {
            'name':  'Juror Class',
        	'num_slots': {'large': 2, 'medium': 3, 'small': 10},
        	'mass_max': 3400,
        	'ship_cost': 160000,
        	'hull': 1100,
        	'armor': 10,
        	'shield': 10,
        	'speed': 24,
        	'agility': 24,
        	'fuel': 95,
        	'cargo': 25,
        	'officers_max': 4,
        	'crew_max': 24,
        	'jump_cost': 21,
        	'move_cost': 2,
        	'combat_cost': 8,
        	'pilot': 13,
        	'nav': 17,
        	'ops': 21,
        	'electronics': 14,
        	'gunnery': 15,
        	'slots': {
                'large': 
                [
                    'M3400 Void Engine: Balanced',
                    'Bridge',
                    'Cargo Hold 1',
                ],
                'medium': [
                    'Barracks 3',
                    'Basic Hyperwarp Drive',
                ], 
                'small': [
                    'Officer Cabin',
                    'Officer Cabin',
                    'Passenger Cabin', 
                    'Light Railgun',
                    'Hellfire Torpedo', 
                    'Weapons Locker A1', 
                    'Officer Cabin',
                    'Armored Bulkhead', 
                    'Hellfire Torpedo',
                    'Phoenix Lance',
                ]
            }
        },
        {
            'name': 'Paladin Cruiser',            
        	'num_slots': {'large': 4, 'medium': 5, 'small': 10},
        	'mass_max': 3400,
        	'ship_cost': 160000,
        	'hull': 1100,
        	'armor': 10,
        	'shield': 10,
        	'speed': 24,
        	'agility': 24,
        	'fuel': 95,
        	'cargo': 25,
        	'officers_max': 4,
        	'crew_max': 24,
        	'jump_cost': 21,
        	'move_cost': 2,
        	'combat_cost': 8,
        	'pilot': 13,
        	'nav': 17,
        	'ops': 21,
        	'electronics': 14,
        	'gunnery': 15,
        	'slots': {
                'large': 
                [
                    'M3400 Void Engine: Balanced',
                    'Cargo Hold 1',
                ],
                'medium': [
                    'Bridge',
                    'Barracks 3',
                    'Basic Hyperwarp Drive',
                ], 
                'small': [
                    'Officer Cabin',
                    'Officer Cabin',
                    'Passenger Cabin', 
                    'Light Railgun',
                    'Hellfire Torpedo', 
                    'Weapons Locker A1', 
                    'Officer Cabin',
                    'Armored Bulkhead', 
                    'Hellfire Torpedo',
                    'Phoenix Lance',
                ]
            }
        },
    ]


def serve_static():
    cwd = os.getcwd()
    app.add_static_route('/js', os.path.join(cwd, 'js'))
    app.add_static_route('/css', os.path.join(cwd, 'css'))
    app.add_static_route('/fonts', os.path.join(cwd, 'fonts'))

app = falcon.API()
data = Data()
sessions = SessionStorage()
content = Content('main.html', data)
build = MainPage(sessions, content)
app.add_route('/', build)
serve_static()

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()

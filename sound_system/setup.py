from setuptools import setup

package_name = 'sound_system'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'sound_system',
        'turtlebot_button0',
        'sound_speak1',
        'sound_stop',
        'sound_speak2',
    ],
    install_requires=['setuptools'],
    data_files=[
        ('lib/' + package_name, ['package.xml']),
        ('lib/' + package_name+'/module',
         ['module/module_pico.py',
          'module/module_follow.py',
          'module/module_arm.py',
          'module/module_make_map.py',
          'module/module_beep.py',
          'module/module_start.py'
          ]),
        ('lib/sound_system/dictionary/',
         ['dictionary/yes_no.dict',
          'dictionary/yes_no.gram',
          'dictionary/follow_me.dict',
          'dictionary/follow_me.gram',
          'dictionary/take_bag.dict',
          'dictionary/take_bag.gram',
          'dictionary/map_test.dict',
          'dictionary/map_test.gram',
          'dictionary/start_the_test.dict',
          'dictionary/start_the_test.gram'
          ]),
        ('lib/sound_system/beep/',
         ['beep/speech.wav',
          'beep/start.wav',
          'beep/stop.wav'
          ]),
        ('lib/sound_system/log',
            ['log/log.txt'])
    ],
    zip_safe=True,
    author='HiroseChihiro',
    author_email='rr0111fx@ed.ritsumei.ac.jp',
    maintainer='HiroseChihiro',
    maintainer_email='rr0111fx@ed.ritsumei.ac.jp',
    keywords=['ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='sound package for carry my luggage',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sound_system = sound_system:main',
            'turtlebot_button0 = turtlebot_button0:main',
            'sound_speak1 = sound_speak1:main',
            'sound_stop = sound_stop:main',
            'sound_speak2 = sound_speak2:main',
        ],
    },
)

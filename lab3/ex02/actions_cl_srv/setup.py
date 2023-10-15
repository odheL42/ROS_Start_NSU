from setuptools import find_packages, setup

package_name = 'actions_cl_srv'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='odhel42',
    maintainer_email='odhel42@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['action_server= actions_cl_srv.action_server:main', 
                            'action_client= actions_cl_srv.action_client:main'
        ],
    },
)

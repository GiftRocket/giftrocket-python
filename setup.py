from setuptools import setup, find_packages
import giftrocket


url = 'https://github.com/giftrocket/giftrocket-python'

setup(
    name='giftrocket-python',
    version=giftrocket.__version__,
    description='Python API client for GiftRocket',
    long_description='',
    keywords='api, gift cards, rewards, incentives, giftrocket',
    author='Ben Rocket',
    author_email='ben@giftrocket.com',
    url=url,
    download_url='{}/tarball/v{}'.format(url, giftrocket.__version__),
    license='MIT',
    packages=find_packages(exclude='tests'),
    package_data={'README': ['README.md']},
    install_requires=['requests==2.7.0'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ]
)

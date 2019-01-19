from setuptools import setup


setup(
    name="events",
    version="0.1",
    py_modules=["events"],
    install_requires=[
        "Click",
        "requests"
    ],
    entry_points="""
        [console_scripts]
        events=events:cli
    """
)
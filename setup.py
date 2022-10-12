from setuptools import setup

setup(
    name='python_project_structure',
    url='https://github.com/jakhmoladp/git_project_structure.git',
    author='Devendra Prasad Jakhmola',
    author_email='devjakhmola1990@gmail.com',
    packages=find_package(),
    install_requires=['numpy', 'pandas', 'streamlit','sklearn','joblib'],
    version='0.1',
    license='MIT',
    description='An example of how a basic project structure would look like'
)

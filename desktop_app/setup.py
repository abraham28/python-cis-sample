from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'include_files': ['barangays.json', 'city-mun.json', 'provinces.json', 'regions.json']
    }
}

executables = [Executable('main.py')]

setup(
    name='Sample CIS',
    version='1.0',
    description='Demo CIS made with python, fastapi, redis, pyqt6',
    options=options,
    executables=executables
)

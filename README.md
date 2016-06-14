Python script that reads data from a website and formats for use in RASCAL. 

This project was done in collaboration with SLO OES. The weatherscraper.py file in the top directory downloads PGE's weather from the [target site], parses the wind data and writes it to a local file as defined by RASCAL format.

In order to make this script easy to run, it is packaged with [pyinstaller] into an installer file. The created folder in the dist directory can then be distributed and run without any external dependencies.

If you manage to install pyinstaller simply build the .exe by running: `pyinstaller weatherscraper.py -i dcpp_icon.ico`

[pyinstaller]: <http://pythonhosted.org/PyInstaller/>
[target site]: <http://www.pge.com/about/edusafety/dcpp/index.jsp>

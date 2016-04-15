This project was done in collaboration with SLO OES. The weatherscraper.py file in the top directory downloads PGE's weather from [PGE Weather Info] data, parses the wind data and writes it to a local file as defined by RASCAL format.

In order to make this script easy to run, it is packaged with [pyinstaller] into an installer file. The created folder in the dist directory can then be distributed and run without any external dependencies.

[pyinstaller]: <http://pythonhosted.org/PyInstaller/>
[PGE Weather Info]: <http://www.pge.com/about/edusafety/dcpp/index.jsp>

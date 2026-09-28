# Material:

# Module, Package, Pip, and Virtual enviroment
# Virtual enviroment --> Untuk menyimpan library-library python yang dibutuhkan untuk sebuah proyek
# To make virtual enviroment
# steps:
# 1. Open terminal
# 2. Write "python -m venv name_of_virtual_enviroment" --> Make a virtual enviroment(It will produce a file that contains folder include, Lib, scripts, etc)
# 3. Write "name_of_virtual_enviroment\Scripts\activate" --> Activate virtual enviroment
# 4. Write "pip install name_of_package" --> Install a package
# 5. Write "deactivate" --> Deactivate virtual enviroment

# Module --> A file containing python code and may have function, class, etc and we can import to other file
#            Ex: .py file
# Package --> Folder containing more that one modules
# Pip --> To install module or package to virtual enviroment

# NOTEE: sapa_bahasa.py is a module, and we can import it to other file

from sapa_bahasa import sapa_indo, sapa_inggris, sapa_spanyol, sapa_mandarin, sapa_korea

print(sapa_indo("Anya"))
print(sapa_inggris("Anya"))
print(sapa_spanyol("Anya"))
print(sapa_mandarin("Anya"))
print(sapa_korea("Anya"))

import pandas
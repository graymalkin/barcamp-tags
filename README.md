barcamp-tags
============

This is a dirty script to generate names for on name tags for barcamp. It's designed to work with AutoCAD DXF file.

# Requires

- python
    - [dxfwrite 1.2.0](https://pypi.python.org/pypi/dxfwrite/1.2.0)
	    `pip install dxfwrite`

	    or
	    
	    ```
	    wget https://pypi.python.org/packages/source/d/dxfwrite/dxfwrite-1.2.0.tar.gz#md5=56bd40206e6dbf4a3be2f3b6936a2c4f
	    tar -xfv dxfwrite-1.2.0.tar.gz
	    python dxfwrite-1.2.0/setup.py install
	    ```
# Usage

`python -o <outputfile> -d <datafile>`

The datafile is a plain CSV of names.

This will create a new file, in -o which has apropriately spaced names to be copied onto a template.

Sadly dxfwrite doesn't do dxf reading, so the last step needs to be done with AutoCAD or similar.

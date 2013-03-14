StateTracer
==========

Python script used to decompress and compress MAME save states

This script utilizes the zlib python library in order to decompress MAME save states into
separate header and data files. The decompressed data files can be opened using any hex editor for
viewing or editing. After editing, you can use this script to recompress the data and header back 
into a useable MAME save-state

------------
Requirements
============

This app was built using python 2.7.2

-----------------
#Using This Script
=================

    Basic Usage: stateTracer.py [-h] [-x] [-p] [-c] [-d] [-D] [-s INPUT] [-o OUTPUT] [-l LOG] [-v]

There are a number of options for this script in terms of operation, input, and output. 
Input and output is directed to STD IN/OUT respectively unless specified otherwise by the 
appropriate switches (-s or -o). 

Reading and writing from STD IN/OUT isn't very stable, and hasn't been well tested. For now, 
it's better to just specify which files you want to use for input and output.

Example Usage:
---------
Not all options are required. Here are some simple examples

    $ stateTracer.py -d -s mySave.sta -o myDecompressedSaveFile.dec
    Description: Takes "mySave.sta" and attempts to decompress it into "myDecompressedSaveFile.dec". 
    This also creates a header file named "myDecompressedSaveFile.dec.hdr" which is used later to 
    recompress this save. The name of this header file completely depends on the name of your out file.

    $ stateTracer.py -c -s myDecompressedSaveFile.dec -o recompressd.sta
    Description: Takes "myDecompressedSaveFile.dec" and compresses it back into a MAME-usable state. 
    Then the script attempts to open "myDecompressedSaveFile.dec.hdr" and concatenate the two packs 
    of data back into one useable MAME save-state file.

Required I/O Switches:
----------------------
    Switch: -s <file>  (--source <file>)
    Description: Use this to specify a source file for reading. Usually this is the state file you
    are reading for decompressing/compressing

    Switch: -o <file>  (--dest <file>)
    Description: Use this to specify an output file for writing. This is the file that your new 
    state will be written to


Required Operation Switches:
----------------------------------------------------------------------------
Only ONE of the following switches should be used at runtime

    Switch: -c (--compress)
    Description: Compress the input file and corresponding header file into a usable MAME save state

    Switch: -d (--decompress)
    Description: Use this switch to decompress the input file

    Switch: -x (--hex)
    Description: Use this switch to read the input file and output it as hex

    ** Currently Not Enabled **
    Switch: -p (--compare)
    Description: Use this switch to search through input files for speciic hex values, and then 
    intersect the sets to find common offsets

Optional Switches:
------------------
    Switch: -D (--Debug)
    Description: Turn on debug mode. STDERR will be opened, and text will be written to the console 
    during operation

    Switch: -l <file> (--log <file>)
    Description: Enable logging to a file. This turns on debug mode, but instead STDERR is pointed 
    at the file passed in

    Switch -v (--version)
    Description: Overrides all other options. Outputs the version of this script to stdout and exits.

-------
License
=======

This code is distributed under the terms and conditions of the MIT license. 

----------
Change-log
==========

- **StateTracer Version 0.5** on 03/14/2013
    + Made StateTracer its own project.
    + Added Compression/Decompression Support
    + Added Hex output support

- **Initial Upload** on 02/21/2013
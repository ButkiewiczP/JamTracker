StateTracer
==========

Python script used to decompress and compress MAME save states

This script utilizes the zlib python library in order to decompress MAME save states into
separate header and data files. The decompressed data files can be opened using any hex editor for
viewing or editing. After editing, you can use this script to recompress the data and header back into
a useable MAME save-state

------------
Requirements
============

This app was built using python 2.7.2

------------
Running
============

Required Switches:
-------------------
Switch: -s <file>  (--source <file>)
Description: Use this to specify a source file for reading. Usually this is the state file you
are reading for decompressing/compressing

Switch: -o <file>  (--dest <file>)
Description: Use this to specify an output file for writing. This is the file that your new state will be written to


Only ONE of the following operation switches should be supplied at runtime:
----------------------------------------------------------------------------
Switch: -c (--compress)
Description: Compress the input file and corresponding header file into a usable MAME save state

Switch: -d (--decompress)
Description: Use this switch to decompress the input file

Switch: -x (--hex)
Description: Use this switch to read the input file and output it as hex

** Currently Not Enabled **
Switch: -p (--compare)
Description: Use this switch to search through input files for speciic hex values, and then intersect the sets 
to find common offsets

Optional Switches:
------------------
Switch: -D (--Debug)
Description: Turn on debug mode. STDERR will be opened, and text will be written to the console during operation

Switch: -l <file> (--log <file>)
Description: Enable logging to a file. This turns on debug mode, but instead STDERR is pointed at the file passed in

Switch: -D (-D)
Description: Turn on debug mode. STDERR will be opened, and text will be written to the console during operation

-------
License
=======

This code is distributed under the terms and conditions of the MIT license. 

----------
Change-log
==========

**Initial Upload** on 02/21/2013
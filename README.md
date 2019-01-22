# CityEngine FBX Export IDs
This repository provides a python script for CityEngine that reads a specific object attribute, in this case `OBJECTID`, and assigns that value as the name of each object. The script then exports the collection of named objects to an FBX file. The names of each object can be used in software like a game engine to attach further data to each object via script.

**Note:** The attribute selected for the exported object names must funtion as a unique identifier in order for data to be attached to each object unambiguously.
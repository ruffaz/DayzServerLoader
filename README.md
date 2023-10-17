# dayzutilities

# Dayz server/client launcher


### Description
Target users: mappers, artists and modders. Designed to be simple utility, that can load a Dayz Client and Server in paralell using prefefined mod lists.  

Option to run as pure server, dxdiag server/client combo, or client only for DayzEditor.
Uses symlinks, and shares symlinks across internal lists logically. 

Saves automatically


## Quick Setup
Download installer  
Install somewhere

### Workflow
Choose Dayz Server location  
Choose Steam !Workshop location (may be hidden, is usually always located in a folder under the dayz parent folder  
* Create a new modlist  
* Options  
    * choose a profile folder (i.e DayZServer\DayzServerProfile )  
    * choose a missions folder (i.e DayZServer\mpmissions\dayzOffline.ChernarusPlus )  
    * choose a custom serverDZ.config (i.e DayZServer Exp\serverDZ.cfg)  
* Now either choose a !Workshop or a Local mod (the whole point of this)  
* The mod will be displayed in a handy list that you can duplicate  
It symlinks the mod to the server location so no mess  
Repeat



Mod source is on p: drive
Local Mod output is in a _mods folder on p: drive

Planned features!

 - better error checking
 - experimental support
 - instead of deleting a mod, have the option to replace 
 - installing keys
 - maybe pure client launching? 


Uses QtModern
https://github.com/gmarull/qtmodern

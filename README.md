# dayzutilities

# Dayz server/client launcher

-- Description --
Target users: mappers, artists and modders. Simple mod loader, that can load a Dayz Client and Server using prefefined mod lists. 

Can run as pure server, dxdiag server/client combo, or client only for dayzeditor
Uses symlinks, and shares symlinks acros lists logically

-- Quick setup --

Choose server location
Choose !workshop location (may be hidden, is usually always located in a folder under the dayz parent folder
Create a new modlist
  Options
    - choose a profile folder (i.e DayZServer\DayzServerProfile )
    - choose a missions folder (i.e DayZServer\mpmissions\dayzOffline.ChernarusPlus )
    - choose a custom serverDZ.config (i.e DayZServer Exp\serverDZ.cfg)
Now choose a mod to load from the !workshop folder 
And the whole point of this, choose a local mod to load
It will store the mod name in a handy list that you can duplicate
It symlinks the mod to the server location so no mess

-- My workflow, it may not be your workflow --

Mod source is on p: drive
Local Mod output is in a _mods folder on p: drive

Planned features!

 - better error checking
 - exp support
 - instead of deleting a mod, have the option to replace 
 - installing keys
 - maybe pure client launching? 


Uses QtModern
https://github.com/gmarull/qtmodern

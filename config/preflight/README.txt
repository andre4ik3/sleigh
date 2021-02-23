This folder is where preflight configurations are stored.
Preflight configurations are tried in the following order:

Machine ID -> Serial Number -> Primary User -> Hostname -> _default

You can use the Machine Owner key to "group" machines to the same config.
If all your machines are using the same config, then use _default.
A sample _default is provided here. All data from it is returned to santactl.
For more info on which keys you can put that will affect santactl, read the wiki

This is where Sleigh stores rules. Every rule is stored in a folder, with the
folder name being one of the following:

- Machine ID
- Serial Number
- Hostname
- Primary User
- "global"

The folder names are tried in that order. Every file ending with .json in the
folder will be loaded, even if it's nested (!)

Please avoid having machine IDs set as one of the other values, as this can lead
to unexpected behavior. (don't put machine id as serial or hostname or user)

You can read more on the types of keys you can have in rules on the wiki.

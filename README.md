# DayMinusOne
A utility to convert the DayOne journal JSON format to Markdown (suitable for import into Joplin and elsewhere)

Usage: ```dayminusone.py --help for usage```

Right now we only support importing the text part of DayOne journal entries. DayOne "moments" will be preserved in
the import but will not be rendered correctly by Joplin.

Also, I haven't figured out how to get DayOne tags to convert to Joplin tags on import so right now youget your tags
in a "TAGS: " header after the entry creation date line.

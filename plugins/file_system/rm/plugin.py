"""Remove a file

SYNOPSIS:
    rm <REMOTE FILE>

DESCRIPTION:
    Remove the given REMOTE FILE from remote server, or print
    concerned errors in case of insufficient permissions or
    bad file path.

    NOTE: Unlike the GNU's 'rm' coreutils command, this plugin
    only supports a single file as argument.

EXAMPLES:
    > rm pdfs/r57.php
      - Remove the ./pdfs/r75.php file from remote server

AUTHOR:
    nil0x42 <http://goo.gl/kb2wf>
"""

import sys

from api import plugin
from api import server

if len(plugin.argv) not in [2, 3]:
    sys.exit(plugin.help)

recurse = 0

if plugin.argv[1] == "-r":
    if len(plugin.argv) == 2:
        sys.exit(plugin.help)
    recurse = 1
    rel_path = plugin.argv[2]
else:
    if len(plugin.argv) == 3:
        sys.exit(plugin.help)
    rel_path = plugin.argv[1]

abs_path = server.path.abspath(rel_path)
dirname = server.path.dirname(abs_path)
basename = server.path.basename(abs_path)

if recurse:
    sys.exit("Recursive mode is not yet available.")

payload = server.payload.Payload("single.php")
payload["FILE"] = abs_path

payload.send()

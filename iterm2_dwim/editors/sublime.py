import re
import subprocess

from iterm2_dwim.logger import log

from iterm2_dwim.editors.base_editor import BaseEditor


class Sublime(BaseEditor):

    def visit_file(self, path, line):
        path = re.sub('\.pyc$', '.py', path)

        cmd = [
            self.executable,
            '%s:%s' % (path, line)
        ]
        log(' '.join(cmd))
        subprocess.check_call(cmd)

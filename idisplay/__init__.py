#!/usr/bin/env python

from IPython.display import HTML, Image, JSON, Latex, Math, SVG, YouTubeVideo
from IPython.core.magic import Magics, magics_class, line_magic, cell_magic

@magics_class
class DisplayMagic(Magics):
    @line_magic
    @cell_magic
    def display(self, line, cell):
        """
        Display something using IPython's rich display system.

        Parameters
        ----------
        -h, --html    : load HTML file
        -i, --image   : load JPG or PNG image
        -j, --json    : load JSON file
        -l, --latex   : load LaTeX file
        -m, --math    : load LaTeX math expression
        -s, --svg     : load SVG file
        -y, --youtube : load YouTube ID
        """
        
        opts, cell = self.parse_options('%s\n%s' % (line, cell),
                                        'h:i:j:l:m:s:y:',
                                        ['image=', 'html=', 'json=', 'latex=',
                                         'math=', 'svg=', 'youtube='])
        for opt, arg in opts:
            if opt in ['h', '--html']:
                HTML(arg)
            elif opt in ['-i', '--image']:
                Image(arg)
            elif opt in ['-j', '--json']:
                JSON(arg)
            elif opt in ['-l', '--latex']:
                Latex(arg)
            elif opt in ['-m', '--math']:
                Math(arg)
            elif opt in ['-s', '--svg']:
                YouTubeVideo(arg)
            elif:
                raise ValueError('unrecognized option')

def load_ipython_extension(ip):
    ip.register_magics(DisplayMagic)

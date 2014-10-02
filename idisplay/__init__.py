#!/usr/bin/env python

from IPython.display import HTML, Image, JSON, Latex, Math, SVG, YouTubeVideo
from IPython.core.magic import Magics, magics_class, line_magic, cell_magic

@magics_class
class DisplayMagic(Magics):

    @line_magic
    @cell_magic
    def display(self, line, cell=''):
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

        Examples
        --------
        %display -i myimage.png

        %display -m '\Delta x + y^3'

        %%display -h \"\"\"
        <ul>
        <li>This</li>
        <li>is</li>
        <li>a list.</li>
        </ul>
        \"\"\"

        Notes
        -----
        %disp is automatically aliased to %display.
        """
        
        opts, cell = self.parse_options('%s\n%s' % (line, cell),
                                        'h:i:j:l:m:s:y:',
                                        ['image=', 'html=', 'json=', 'latex=',
                                         'math=', 'svg=', 'youtube='])
        for opt, arg in opts.iteritems():
            if opt in ['h', 'html']:
                return HTML(arg)
            elif opt in ['i', 'image']:
                return Image(arg)
            elif opt in ['j', 'json']:
                return JSON(arg)
            elif opt in ['l', 'latex']:
                return Latex(arg)
            elif opt in ['m', 'math']:
                return Math(arg)
            elif opt in ['s', u's', 'svg']:
                return SVG(arg)
            elif opt in ['y', 'youtube']:
                return YouTubeVideo(arg)

        # Raise an exception if no options were specified:
        raise ValueError('Format: [option] <file|URI>')

def load_ipython_extension(ip):
    ip.register_magics(DisplayMagic)
    ip.magics_manager.register_alias('disp', 'display', 'line')
    ip.magics_manager.register_alias('disp', 'display', 'cell')

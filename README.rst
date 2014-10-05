.. -*- rst -*-

IDisplay
========

Package Description
-------------------
IDisplay is an IPython extension that provides magic functions
for accessing IPython's rich display system in the Notebook.

Installation
------------
The package may be installed as follows: ::

    pip install idisplay

After installation, the extension may be loaded within an IPython session
with ::

    %load_ext idisplay

Usage Examples
--------------
Display an image: ::

    %display -i myimage.png

Display a LaTeX math expression: ::

    %display -m '\Delta x + y^3'

Render some HTML: ::

    %display -y -h """
    <ul>
    <li>This</li>
    <li>is</li>
    <li>a list.</li>
    </ul>
    """

Development
-----------
The latest release of the package may be obtained from
`Github <https://github.com/lebedov/idisplay>`_.

Author
------
See the included AUTHORS.rst file for more information.

License
-------
This software is licensed under the
`BSD License <http://www.opensource.org/licenses/bsd-license.php>`_.
See the included LICENSE.rst file for more information.

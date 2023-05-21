
# Exists so I can run this on pythoneverywhere

from . import create_app
app = create_app()
'''
In any case, what worked was creating a module, run_it.py, inside the "mutilator" package. 
In run_it.py, I imported create_app from the package's global namespace--so just "from mutilator import create_app", 
and then I just added the code "app = create_app()". 
Then my WSGI config file had "from mutilator.run_it import app as application" and it worked just fine.

'''
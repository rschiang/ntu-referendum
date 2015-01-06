from fabric.api import local

SCSS_OPTIONS = '-r bourbon -r neat -t compressed --sourcemap=none'
SCSS_FOLDER = 'scss:assets/css'

def scss(action=''):
    if action == 'compile':
        local('scss %s --update %s' % (SCSS_OPTIONS, SCSS_FOLDER))
    elif action == 'watch':
        local('scss %s --watch %s' % (SCSS_OPTIONS, SCSS_FOLDER))
    elif action == 'rebuild':
        local('scss %s --update %s' % (SCSS_OPTIONS + ' -f', SCSS_FOLDER))
    else:
        print('Available commands: compile, watch, rebuild.')

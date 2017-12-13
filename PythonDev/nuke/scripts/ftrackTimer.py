import os
import ftrack_api


session = ftrack_api.Session(
    server_url=os.environ['FTRACK_SERVER'],
    api_user=os.environ['FTRACK_API_USER'],
    api_key=os.environ['FTRACK_API_KEY']
)


def stopTimer():
    user = session.query('User where username is {0}'.format(os.environ['FTRACK_API_USER'])).one()
    try:
        user.stop_timer()
    except Exception:
        print 'No timer to stop'


def startTimer():
    user = session.query('User where username is {0}'.format(os.environ['FTRACK_API_USER'])).one()
    if 'FTRACK_TASKID' in os.environ.keys():
        task = session.query('Task where id is {0}'.format(os.environ['FTRACK_TASKID'])).one()
        user.start_timer(task, force=True)
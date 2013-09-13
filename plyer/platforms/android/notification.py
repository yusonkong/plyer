from jnius import autoclass
from plyer.facades import Notification
from plyer.platforms.android import activity

AndroidString = autoclass('java.lang.String')
PythonActivity = autoclass('org.renpy.android.PythonActivity')
NotificationBuilder = autoclass('android.app.Notification$Builder')

# Find the Drawables for this app
application_info = PythonActivity.getApplicationInfo().toString()
# Something like: 'ApplicationInfo{421aa0e8 net.clusterbleep.kivyremoteshell}'
package_name = application_info.split(' ')[1][:-1]
Drawable = autoclass(package_name+'.R$drawable')


class AndroidNotification(Notification):
    def _get_notification_service(self):
        if not hasattr(self, '_ns'):
            self._ns = activity.getSystemService(
                    PythonActivity.NOTIFICATION_SERVICE)
        return self._ns

    def _notify(self, **kwargs):
        icon = Drawable.icon
        noti = NotificationBuilder(activity)
        #noti.setDefaults(Notification.DEFAULT_ALL)
        noti.setContentTitle(AndroidString(
            kwargs.get('title').encode('utf-8')))
        noti.setContentText(AndroidString(
            kwargs.get('message').encode('utf-8')))
        noti.setSmallIcon(icon)
        noti.setAutoCancel(True)
        self._get_notification_service().notify(0, noti.build())


def instance():
    return AndroidNotification()


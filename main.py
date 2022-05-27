from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = 'Time To Take Rest',
            message = 'Rest is very vital for humans it\'s impact on our mind also',
            app_icon = 'drop_icon-icons.com_54400.ico',
            timeout = 5
        )

        time.sleep(20)
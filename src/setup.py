from setuptools import setup
import setup_translate

pkg = 'Extensions.BirthdayReminder'
setup(name='enigma2-plugin-extensions-birthdayreminder',
       version='3.0',
       description='Birthday Reminder: Reminds you of birthdays',
       package_dir={pkg: 'BirthdayReminder'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'LICENSE', 'plugin.png', 'setup.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )

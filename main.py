from kivymd.app import MDApp
from kivy.lang import Builder


class AudioSus(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'Bottom navigation'
        right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["clock", lambda x: app.callback_2()]]
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Главная'
            icon: 'home'

            MDLabel:
                text: 'Python'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Друзья'
            icon: 'human-greeting'

            MDLabel:
                text: 'I programming of C++'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Сохраненое'
            icon: 'account-music'

            MDLabel:
                text: 'JS'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Настройки'
            icon: 'cog'

            MDFloatLayout:

                MDSwitch:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    text: 'Скачивать треки автоматически'
'''
        )


AudioSus().run()
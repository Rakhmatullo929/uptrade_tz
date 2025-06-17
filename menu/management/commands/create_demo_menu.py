from django.core.management.base import BaseCommand
from menu.models import Menu, MenuItem


class Command(BaseCommand):
    help = 'Создает демонстрационные меню с данными'

    def handle(self, *args, **options):
        # Удаляем существующие данные
        MenuItem.objects.all().delete()
        Menu.objects.all().delete()

        # Создаем главное меню
        main_menu = Menu.objects.create(name='main_menu')
        
        # Главная страница
        home_item = MenuItem.objects.create(
            menu=main_menu,
            title='Главная',
            named_url='menu:home',
            order=1
        )
        
        # О нас
        about_item = MenuItem.objects.create(
            menu=main_menu,
            title='О нас',
            named_url='menu:about',
            order=2
        )
        
        # О компании (подраздел О нас)
        MenuItem.objects.create(
            menu=main_menu,
            title='О компании',
            url='/about/company/',
            parent=about_item,
            order=1
        )
        
        # Наша команда (подраздел О нас)
        MenuItem.objects.create(
            menu=main_menu,
            title='Наша команда',
            url='/about/team/',
            parent=about_item,
            order=2
        )
        
        # Услуги
        services_item = MenuItem.objects.create(
            menu=main_menu,
            title='Услуги',
            named_url='menu:services',
            order=3
        )
        
        # Веб-разработка (подраздел Услуги)
        web_dev_item = MenuItem.objects.create(
            menu=main_menu,
            title='Веб-разработка',
            url='/services/web-development/',
            parent=services_item,
            order=1
        )
        
        # Django разработка (подраздел Веб-разработки)
        MenuItem.objects.create(
            menu=main_menu,
            title='Django разработка',
            url='/services/web-development/django/',
            parent=web_dev_item,
            order=1
        )
        
        # React разработка (подраздел Веб-разработки)
        MenuItem.objects.create(
            menu=main_menu,
            title='React разработка',
            url='/services/web-development/react/',
            parent=web_dev_item,
            order=2
        )
        
        # Мобильная разработка (подраздел Услуги)
        MenuItem.objects.create(
            menu=main_menu,
            title='Мобильная разработка',
            url='/services/mobile-development/',
            parent=services_item,
            order=2
        )
        
        # Портфолио
        portfolio_item = MenuItem.objects.create(
            menu=main_menu,
            title='Портфолио',
            named_url='menu:portfolio',
            order=4
        )
        
        # Проекты (подраздел Портфолио)
        MenuItem.objects.create(
            menu=main_menu,
            title='Веб-проекты',
            url='/portfolio/web/',
            parent=portfolio_item,
            order=1
        )
        
        # Блог
        MenuItem.objects.create(
            menu=main_menu,
            title='Блог',
            named_url='menu:blog',
            order=5
        )
        
        # Контакты
        MenuItem.objects.create(
            menu=main_menu,
            title='Контакты',
            named_url='menu:contact',
            order=6
        )

        # Создаем боковое меню
        sidebar_menu = Menu.objects.create(name='sidebar_menu')
        
        # Быстрые ссылки
        quick_item = MenuItem.objects.create(
            menu=sidebar_menu,
            title='Быстрые ссылки',
            url='#',
            order=1
        )
        
        MenuItem.objects.create(
            menu=sidebar_menu,
            title='Админка',
            url='/admin/',
            parent=quick_item,
            order=1
        )
        
        MenuItem.objects.create(
            menu=sidebar_menu,
            title='Главная',
            named_url='menu:home',
            parent=quick_item,
            order=2
        )

        # Разделы сайта
        sections_item = MenuItem.objects.create(
            menu=sidebar_menu,
            title='Разделы сайта',
            url='#',
            order=2
        )
        
        MenuItem.objects.create(
            menu=sidebar_menu,
            title='О нас',
            named_url='menu:about',
            parent=sections_item,
            order=1
        )
        
        MenuItem.objects.create(
            menu=sidebar_menu,
            title='Услуги',
            named_url='menu:services',
            parent=sections_item,
            order=2
        )

        self.stdout.write(
            self.style.SUCCESS('Демонстрационные меню успешно созданы!')
        ) 
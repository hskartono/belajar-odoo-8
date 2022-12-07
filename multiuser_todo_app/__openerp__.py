{
    'name': 'Multiuser To-Do',
    'description': 'Extend the To-Do app to multiuser.',
    'author': 'Harry S. Kartono',
    'depends': ['todo_app'],
    'application': True,
    'data': [
        'views/todo_view.xml',
        'security/todo_access_rules.xml',
    ],
}
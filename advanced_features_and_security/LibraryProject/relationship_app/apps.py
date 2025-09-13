from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    name = 'relationship_app'

    def ready(self):
        from  ..relationship_app.signals  # ✅ Absolute import

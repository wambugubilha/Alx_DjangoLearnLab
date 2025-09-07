from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        try:
            import relationship_app.signals # type: ignore
        except ImportError as e:
            import logging
            logging.error(f"Failed to import signals: {e}")

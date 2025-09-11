from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        try:
            from ..relationship_app import signals
            signals = signals
        except ImportError as e:
            import logging
            logging.error(f"Failed to import signals: {e}")

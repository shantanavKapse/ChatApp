from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import home_app.routing

Application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            home_app.routing.websocket_urlpatterns
        )
    )
})
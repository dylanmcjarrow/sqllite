from fastapi import FastAPI
from pkgutil import walk_packages
import sys
import logging

from api import routers

app = FastAPI()
log = logging.getLogger(__name__)


def import_from(module, name):

    module = __import__(module, fromlist=[name])
    try:
        return getattr(module, name)
    except:  # noqa : F841
        return None


def collect_routers():
    app_api_routers = {}
    module_name = routers.__name__
    package = sys.modules[module_name]
    for loader, name, is_pkg in walk_packages(package.__path__):

        router = import_from(
            f"api.routers.{name}",
            "router",
        )
        if router is not None:
            app_api_routers[name] = router
        else:
            log.info(f"Route (/{name}) does not contain any router.")

    return app_api_routers


for name, router in collect_routers().items():
    app.include_router(
        router,
        prefix=f"/{name}",
        tags=[name],
    )

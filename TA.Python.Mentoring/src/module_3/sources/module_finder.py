import importlib.util
from importlib import metadata


def get_package_path(package_name, log):
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        log.error('Package not found')
    else:
        log.warning(metadata.metadata(package_name)['description'])
        log.info(spec.submodule_search_locations)
        log.debug(metadata.metadata(package_name)['version'])
        return spec.submodule_search_locations

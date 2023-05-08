from rest_framework.versioning import QueryParameterVersioning, URLPathVersioning, BaseVersioning


class MyBaseVersion(BaseVersioning):
    def determine_version(self, request, *args, **kwargs):
        version = request.query_params.get('version')
        return version


class MyQueryVersion(QueryParameterVersioning):
    pass


class MyUrlVersion(URLPathVersioning):
    pass

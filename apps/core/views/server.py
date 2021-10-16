from django.views.generic import ListView
from apps.core.models import Ubuntu, Centos, Server


class ServerListView(ListView):
    template_name = "server/servers.html"
    queryset = Server.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ServerListView, self).get_context_data()
        ubuntu = Ubuntu.objects.all()
        centos = Centos.objects.all()
        data["servers"] = ubuntu.union(centos)
        return data

"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from detection import views
#
# urlpatterns = [
#   path('admin/', admin.site.urls),
#   path('detection/', include('detection.urls')),
#   path('common/', include('common.urls')),
#   path('', views.index, name='index'), # '/'에 해당하는 path
# ]op.counter0|add:1 }}
# 17	    </td>
# 18	    <td class="text-left">
# 19	        <a href="{% url 'pybo:detail' question.id %}">{{ question.subject }}</a>
# 20	        {% if question.answer_set.count > 0 %}
# 21	        <span class="text-danger small ml-2">{{ question.answer_set.count }}</span>
# 22	        {% endif %}
# 23	    </td>
# 24	    <td>{{ question.author.username }}</td>  <!-- 글쓴이 추가 -->
# 25	    <td>{{ question.create_date }}</td>
# 26	</tr>


from django.contrib import admin
from django.urls import include, path
from pybo.views import base_views

urlpatterns = [
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]